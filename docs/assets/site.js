(function () {
  const config = window.RDCD_SITE_CONFIG || {};

  document.querySelectorAll("[data-config-link]").forEach((link) => {
    const key = link.dataset.configLink;
    const url = config[key];

    if (!url) {
      link.classList.add("is-unset");
      link.setAttribute("aria-disabled", "true");
      link.setAttribute("title", "This link will be added before publication.");
      link.addEventListener("click", (event) => event.preventDefault());
      return;
    }

    link.href = url;
    if (link.dataset.configText && config[link.dataset.configText]) {
      link.textContent = config[link.dataset.configText];
    }
  });
})();
