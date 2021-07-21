/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      const checkboxes = document.querySelectorAll('input[type="checkbox"]')
      for (const checkbox of checkboxes) {
        if (checkbox.classList.contains('action-select')) {
          // Add aria-label to each table row checkbox, so that each option is able to be read by screen readers.
          checkbox.setAttribute('aria-label', `Row ${checkbox.value}`)
        } else if (checkbox.id === 'action-toggle') {
          // Similarly, add a label to the "toggle all" checkbox in the first row of the table.
          checkbox.setAttribute('aria-label', 'Toggle all')
        } else {
          checkbox.setAttribute('aria-label', checkbox.parentNode.className.split('-').pop())
        }
      }

    });
  })(django.jQuery);
}
