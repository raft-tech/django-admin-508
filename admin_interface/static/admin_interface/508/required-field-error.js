

/** global: django */

if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
  (function ($) {
    'use strict';
    $(document).ready(function () {
      document.querySelector('.errornote').focus()
      let errorsProbably=document.querySelectorAll('.form-row ul.errorlist li')
      console.log({errorsProbably})
      for(let el of errorsProbably) {
        let formRow = el.parentNode.parentNode
        console.log({el})
        console.log({formRow})
        if(el.textContent === "This field is required.") {
          let label = formRow.querySelector('div label').innerHTML
          console.log({label})

          label = label.substring(0, label.length-1)
          el.innerHTML = `${label} is required.`
        }

      }

    });
  })(django.jQuery);
}
