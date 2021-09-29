/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      // Get the page count with the classname
      const count = document.querySelector('span.action-counter')
      // Add the count to the page title so it is read on initial load
      console.log(count.textContent)
      document.title += " | " + count.textContent

    });
  })(django.jQuery);
}
