/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      const tooltips = document.querySelectorAll('.help-tooltip')

      // Add role="tooltip" and tabindex="0", allowing tooltips to be read by screen readers.
      for (const tooltip of tooltips) {
        tooltip.setAttribute('role', 'tooltip')
        tooltip.setAttribute('tabindex', '0')
      }
    });
  })(django.jQuery);
}
