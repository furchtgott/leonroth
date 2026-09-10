#!/usr/bin/env ruby
# Validate editorial/publication metadata without altering or publishing content.
require 'yaml'
require 'date'
require 'pathname'

module WorksValidation
  STATUSES = %w[forthcoming in_progress scan_checked verified].freeze

  def self.read(path)
    source = File.read(path)
    match = source.match(/\A---\s*\n(.*?)\n---\s*\n/m)
    raise 'Missing YAML front matter' unless match

    data = YAML.safe_load(match[1], permitted_classes: [Date, Time])
    raise 'Front matter must be a mapping' unless data.is_a?(Hash)

    data
  end

  def self.metadata_errors(data, root)
    errors = []
    errors << 'title is required' if data['title'].to_s.strip.empty?
    errors << 'layout must be work' unless data['layout'] == 'work'
    unless data['permalink'].to_s.match?(%r{\A/works/[a-z0-9]+(?:-[a-z0-9]+)*/\z})
      errors << 'permalink must be a stable /works/lowercase-slug/ URL'
    end
    errors << 'unknown or missing digitization_status' unless STATUSES.include?(data['digitization_status'])
    published = data.fetch('published', false)
    errors << 'published must be a YAML boolean' unless [true, false].include?(published)
    if published == true && data['digitization_status'] != 'verified'
      errors << 'published works must have verified status'
    end
    if data['digitization_status'] == 'verified'
      errors << 'verified works require reviewed_by' if data['reviewed_by'].to_s.strip.empty?
      begin
        Date.iso8601(data.fetch('reviewed_on', '').to_s)
      rescue ArgumentError
        errors << 'verified works require an ISO reviewed_on date'
      end
      unless data['reviewed_revision'].to_s.match?(/\A[0-9a-f]{40}\z/)
        errors << 'verified works require the full reviewed content commit SHA'
      end
      record = File.expand_path(data['review_record'].to_s, root)
      unless record.start_with?(File.join(root, '_docs') + '/') && File.file?(record)
        errors << 'verified works require an existing review_record under _docs/'
      end
    end
    if data['pdf'] && !data['pdf'].empty?
      pdf = File.expand_path(data['pdf'].delete_prefix('/'), root)
      unless data['pdf'].start_with?('/') && pdf.start_with?(root + '/') && File.file?(pdf)
        errors << 'pdf must reference an existing repository scan'
      end
    end
    errors
  end

  def self.check(root)
    errors = []
    urls = {}
    paths = Dir.glob(File.join(root, '_works', '*.{md,html}')).sort
    paths.each do |path|
      name = Pathname.new(path).relative_path_from(Pathname.new(root)).to_s
      begin
        data = read(path)
        metadata_errors(data, root).each { |error| errors << "#{name}: #{error}" }
        url = data['permalink']
        errors << "#{name}: duplicate permalink #{url}" if urls.key?(url)
        urls[url] = name
      rescue StandardError => e
        errors << "#{name}: #{e.message}"
      end
    end
    [paths.size, errors]
  end
end

if $PROGRAM_NAME == __FILE__
  root = File.expand_path('..', __dir__)
  count, errors = WorksValidation.check(root)
  abort errors.join("\n") unless errors.empty?
  puts "Works metadata: #{count} work(s), no errors."
end
