# RDCD GitHub Pages site

This folder is designed to be copied into the root of the `usc-epibio-rdcd-data-RShinyApp` repository as `docs/`.

## Before publishing

1. Open `docs/site-config.js`.
2. Add the public URLs for:
   - `navigatorUrl` — the Posit Connect Cloud Shiny app.
   - `sourceIndexUrl` — the same app with the Source Index tab open, if you have a stable tab-specific URL; otherwise use the Navigator URL.
   - `submissionFormUrl` — the Microsoft Form link.
   - `contactUrl` — optional; use `mailto:your-email@sc.edu` or leave it blank.
3. Commit the `docs/` folder in a pull request and merge it into `main`.

## Turn on GitHub Pages

In the repository, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, then select:

- Branch: `main`
- Folder: `/docs`

Save the settings. GitHub will display the live site address once deployment finishes.

The Shiny app remains hosted on Posit Connect Cloud; this static page only links visitors to it.
