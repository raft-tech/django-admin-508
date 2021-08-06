/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      const errors = document.querySelectorAll('.errornote')

      // Add ARIA role to error elements so they are read by screen readers.
      for (const error of errors) {
        error.setAttribute('role', 'alert')
      }

      const errorItems = document.querySelectorAll('.errorList')

      for (const error of errorItems) {
        error.setAttribute('role', 'alert')
      }
    });
  })(django.jQuery);
}
