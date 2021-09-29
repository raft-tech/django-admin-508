/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      const filters = document.querySelectorAll('#changelist-filter .list-filter-dropdown select')
      let options = ''
      // Override the default onchange handler of each filter
      for (const filter of filters) {
        // This needs to be a function expression so `this` references the filter elements themselves
        filter.onchange = function() {
          const value = this.options[this.selectedIndex].value
          options = options.concat(value)
        };
      }

      const applyFiltersButton = document.querySelector('#submit-filters');
      if (applyFiltersButton) {
        applyFiltersButton.onclick = function () {
          window.location = options
        };
      }
    });
  })(django.jQuery);
}
