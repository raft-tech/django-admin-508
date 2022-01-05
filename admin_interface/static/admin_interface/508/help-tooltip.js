/** global: django */

if (typeof django !== "undefined" && typeof django.jQuery !== "undefined") {
  (function ($) {
    "use strict";
    $(document).ready(function () {
      const tooltips = document.querySelectorAll(".help-tooltip");

      // Add role="tooltip" and tabindex="0", allowing tooltips to be read by screen readers.
      for (const tooltip of tooltips) {
        tooltip.setAttribute("role", "tooltip");
        tooltip.setAttribute("tabindex", "0");

        if (tooltip.classList.contains("help-icon")) {
          const titleText = tooltip.title;
          const h2 = tooltip.parentElement;
          h2.removeChild(tooltip);

          h2.innerHTML = `<strong>${h2.innerHTML}</strong><br><br><div>${titleText}</div>`;

          h2.parentElement.style.whiteSpace = "normal";
        }
      }
    });
  })(django.jQuery);
}
