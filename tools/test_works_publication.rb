#!/usr/bin/env ruby
# Exercise real Jekyll output with temporary fixtures, without touching source works.
require 'jekyll'
require 'tmpdir'
require 'fileutils'
require_relative 'check_works'

root = File.expand_path('..', __dir__)
def assert(condition, message)
  raise message unless condition
end

Dir.mktmpdir('leonroth-publication-') do |tmp|
  source = File.join(tmp, 'source')
  FileUtils.mkdir_p([source, File.join(source, '_works'), File.join(source, '_docs')])
  %w[_layouts _includes _preview _data].each { |name| FileUtils.cp_r(File.join(root, name), source) }
  File.write(File.join(source, '_docs/review.md'), 'Test fixture only; no real editorial approval.')
  File.write(File.join(source, 'index.md'), "---\ntitle: Test home\n---\nFixture home.\n")
  base = { 'layout' => 'work', 'title' => 'Test edition', 'digitization_status' => 'scan_checked' }
  fixtures = {
    'unmarked' => base.merge('permalink' => '/works/unmarked/'),
    'draft' => base.merge('permalink' => '/works/draft/', 'published' => false),
    'ready' => base.merge('permalink' => '/works/ready/', 'published' => true,
                          'digitization_status' => 'verified', 'reviewed_by' => 'Test editor',
                          'reviewed_on' => '2026-09-09', 'reviewed_revision' => 'a' * 40,
                          'review_record' => '_docs/review.md')
  }
  fixtures.each do |name, data|
    File.write(File.join(source, "_works/#{name}.md"), data.to_yaml + "---\nFixture text.\n")
  end
  count, errors = WorksValidation.check(source)
  assert(count == 3 && errors.empty?, "Valid fixtures rejected: #{errors}")
  invalid = WorksValidation.metadata_errors(fixtures['draft'].merge('published' => true), source)
  assert(invalid.include?('published works must have verified status'), 'Unverified publication was not rejected')
  invalid = WorksValidation.metadata_errors(fixtures['ready'].reject { |k, _| k == 'reviewed_by' }, source)
  assert(invalid.include?('verified works require reviewed_by'), 'Missing editorial reviewer was not rejected')

  release = File.join(tmp, 'release.yml')
  File.write(release, {
    'include' => %w[_files _preview], 'collections' => { 'works' => { 'output' => true } },
    'works_preview' => false, 'unpublished' => false
  }.to_yaml)
  modes = {
    'normal' => [File.join(root, '_config.yml')],
    'preview' => [File.join(root, '_config.yml'), File.join(root, '_config.works-preview.yml')],
    'release' => [File.join(root, '_config.yml'), release]
  }
  modes.each do |mode, configs|
    destination = File.join(tmp, mode)
    site = Jekyll::Site.new(Jekyll.configuration(
      'config' => configs, 'source' => source, 'destination' => destination,
      'quiet' => true, 'disable_disk_cache' => true
    ))
    site.process
    if mode == 'normal'
      assert(!File.exist?(File.join(destination, 'works')), 'Archive leaked into normal output')
      assert(!File.exist?(File.join(destination, 'assets/css/works.css')), 'Archive stylesheet leaked into normal output')
      next
    end
    index = File.read(File.join(destination, 'works/index.html'))
    sitemap = File.read(File.join(destination, 'sitemap.xml'))
    fixtures.each_key do |name|
      expected = mode == 'preview' || name == 'ready'
      assert(File.exist?(File.join(destination, "works/#{name}/index.html")) == expected,
             "#{mode}: wrong publication state for #{name}")
      assert(index.include?("href=\"/leonroth/works/#{name}/\"") == expected,
             "#{mode}: wrong index eligibility for #{name}")
      assert(sitemap.include?("/works/#{name}/") == expected,
             "#{mode}: wrong sitemap eligibility for #{name}")
    end
  end
end
puts 'Publication checks passed: normal omission, explicit draft preview, approved-only release, index/sitemap, and metadata rejection.'
