/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      const selects = document.querySelectorAll('select')

      // Add missing title to select elements.
      for (const select of selects) {
        const title = select?.['data-field-name'] ?? select?.name
        select.setAttribute('title', title.replace(/_/g, ' '))
      }
    });
  })(django.jQuery);
}
