'use strict';
{
  const toggleNavSidebar = document.getElementById('toggle-nav-sidebar');
  const navSidebar = document.getElementById('nav-sidebar');
  const openSidebarButton = document.getElementById('open-nav-sidebar-button')
  if (toggleNavSidebar !== null) {

    const navLinks = document.querySelectorAll('#nav-sidebar a');

    function disableNavLinkTabbing() {
      navSidebar.classList.add('close')
      openSidebarButton.classList.remove('hidden')

      for (const navLink of navLinks) {
        navLink.tabIndex = -1;
      }
    }
    function enableNavLinkTabbing() {

      navSidebar.classList.remove('close')
      openSidebarButton.classList.add('hidden')

      for (const navLink of navLinks) {
        navLink.tabIndex = 0;
      }
    }

    const main = document.getElementById('main');
    let navSidebarIsOpen = localStorage.getItem('django.admin.navSidebarIsOpen');
    if (navSidebarIsOpen === null) {
      navSidebarIsOpen = 'true';

      enableNavLinkTabbing();
    }
    if (navSidebarIsOpen === 'false') {
      disableNavLinkTabbing();
    }

    if (navSidebarIsOpen === 'true') {
      enableNavLinkTabbing();
    }

    toggleNavSidebar.addEventListener('click', () => {
      navSidebarIsOpen = 'false';
      disableNavLinkTabbing();
      localStorage.setItem('django.admin.navSidebarIsOpen', navSidebarIsOpen);
    });
    
    openSidebarButton.addEventListener('click', () => {
      navSidebarIsOpen = 'true';
      enableNavLinkTabbing();
      localStorage.setItem('django.admin.navSidebarIsOpen', navSidebarIsOpen);
    });
  }

  function initSidebarQuickFilter() {
    const options = [];
    if (!navSidebar) {
      return;
    }
    navSidebar.querySelectorAll('th[scope=row] a').forEach((container) => {
      options.push({title: container.innerHTML, node: container});
    });

    function checkValue(event)
    {
      let filterValue = event.target.value;
      if (filterValue) filterValue = filterValue.toLowerCase();
      if (event.key === 'Escape') {
        filterValue = '';
        event.target.value = ''; // clear input
      }
      let matches = false;
      for (const o of options)
      {
        let displayValue = '';
        if (filterValue) {
          if (o.title.toLowerCase().indexOf(filterValue) === -1) displayValue = 'none';
          else matches = true;
        }
        // show/hide parent <TR>
        o.node.parentNode.parentNode.style.display = displayValue;
      }

      if (!filterValue || matches) event.target.classList.remove('no-results');
      else event.target.classList.add('no-results');

      sessionStorage.setItem('django.admin.navSidebarFilterValue', filterValue);
    }

    const nav = document.getElementById('nav-filter');
    nav.addEventListener('change', checkValue, false);
    nav.addEventListener('input', checkValue, false);
    nav.addEventListener('keyup', checkValue, false);

    const storedValue = sessionStorage.getItem('django.admin.navSidebarFilterValue');
    if (storedValue) {
      nav.value = storedValue;
      checkValue({target: nav, key: ''});
    }
  }
  window.initSidebarQuickFilter = initSidebarQuickFilter;
  initSidebarQuickFilter();
}
