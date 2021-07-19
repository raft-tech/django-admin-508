/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {

      const checkboxes = document.querySelectorAll('input.action-select')
      // Add hidden label and aria attributes to each checkbox, so that each option
      // is able to be read by screen readers.
      for (const checkbox of checkboxes) {
        const label = document.createElement('label')
        label.setAttribute('id', `option-${checkbox.value}-label`)
        label.setAttribute('for', `option-${checkbox.value}`)
        label.innerHTML = `Option ${checkbox.value}`
        label.style.display = 'none'

        checkbox.setAttribute('id', `option-${checkbox.value}`)
        checkbox.setAttribute('aria-describedby', `option-${checkbox.value}-label`)

        checkbox.parentNode.appendChild(label)
      }
    });
  })(django.jQuery);
}
