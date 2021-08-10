/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      console.log("LOADED")
      const filters = document.querySelectorAll('#changelist-filter .list-filter-dropdown select')
      let options = ''
      // Override the default onchange handler of each filter
      for (const filter of filters) {
        // This needs to be a function expression so `this` references the filter elements themselves
        filter.onchange = function() {
          const value = this.options[this.selectedIndex].value
          options = options.concat(value)
          console.log(options)
        };
      }

      const applyFiltersButton = document.querySelector('#submit-filters');
      applyFiltersButton.onclick = function () {
        console.log("SUBMIT", options)
        window.location = options
      };

    });
  })(django.jQuery);
}
