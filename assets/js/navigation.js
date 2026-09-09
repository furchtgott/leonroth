/* The links remain available when JavaScript is disabled. */
const navigation = document.querySelector('.foundation-nav');
const menuToggle = document.querySelector('.menu-toggle');
if (navigation && menuToggle) {
  navigation.classList.add('enhanced');
  menuToggle.hidden = false;
  const submenuButtons = [...navigation.querySelectorAll('.submenu-toggle')];
  const closeSubmenus = () => submenuButtons.forEach(button => {
    button.setAttribute('aria-expanded', 'false');
    button.closest('.nav-item').classList.remove('is-open');
  });
  menuToggle.addEventListener('click', () => {
    const open = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
    if (!open) closeSubmenus();
  });
  submenuButtons.forEach(button => {
    button.hidden = false;
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      closeSubmenus();
      button.setAttribute('aria-expanded', String(open));
      button.closest('.nav-item').classList.toggle('is-open', open);
    });
  });
  document.addEventListener('click', event => {
    if (!navigation.contains(event.target)) closeSubmenus();
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    const openSubmenu = submenuButtons.find(button => button.getAttribute('aria-expanded') === 'true');
    if (openSubmenu) {
      closeSubmenus();
      openSubmenu.focus();
    } else if (menuToggle.getAttribute('aria-expanded') === 'true') {
      menuToggle.setAttribute('aria-expanded', 'false');
      navigation.classList.remove('is-open');
      menuToggle.focus();
    }
  });
}
