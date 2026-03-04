# CLAUDE.md

This file provides guidance to Claude Code when working with the bamengine.org repository.

## Project Overview

This is the project website for [BAM Engine](https://github.com/kganitis/bam-engine), hosted at [bamengine.org](https://bamengine.org). Built with Hugo and the scientific-python-hugo-theme, deployed to GitHub Pages via GitHub Actions.

## Quick Reference

### Essential Commands

```bash
# Local development
hugo server                    # Dev server at http://localhost:1313

# Production build
hugo --minify                  # Build to public/

# Full build with JupyterLite + search
hugo --minify && \
  jupyter lite build --contents content/try/notebooks --output-dir public/try/repl && \
  npx pagefind --site public
```

### Directory Structure

| Directory | Purpose |
|-----------|---------|
| `content/` | Markdown pages — Hugo renders each `.md` to a page |
| `content/posts/` | Blog posts (must be `posts/`, not `blog/` — theme's `{{</* blog */>}}` shortcode queries this section) |
| `content/gallery/` | Gallery entries with simulation output images |
| `content/try/notebooks/` | Jupyter notebooks bundled into JupyterLite |
| `static/images/` | Logo SVGs, gallery PNGs, favicon |
| `layouts/shortcodes/` | Custom Hugo shortcodes (e.g., `jupyterlite.html`) |
| `layouts/_default/` | Layout overrides (e.g., `redirect.html`) |
| `assets/css/` | Custom CSS loaded by the theme |
| `themes/scientific-python-hugo-theme/` | Git submodule — do not edit directly |

## Detailed Documentation (`.claude/docs/`)

| File | Contents |
|------|----------|
| [THEME_REFERENCE.md](.claude/docs/THEME_REFERENCE.md) | Theme shortcodes, config options, dark mode, content conventions |

## Key Patterns

1. **Config-driven layout**: Hero, navbar, footer are all defined in `config.yaml` — no template editing needed
2. **Theme submodule**: The theme is a Git submodule. After cloning, run `git submodule update --init --recursive`
3. **Blog section**: Must use `content/posts/` (the `{{</* blog */>}}` shortcode hardcodes `"posts"`)
4. **Front matter**: Use YAML front matter. Blog posts need `authors` (list), not `author`
5. **JupyterLite**: Built in CI to `public/try/repl/`, embedded via iframe shortcode. Will 404 in local dev — that's expected
6. **Gallery images**: Generated from bam-engine simulation runs, committed to `static/images/`

## Critical Gotchas

- **Theme submodule**: `git clone` alone won't pull the theme. Always use `--recurse-submodules` or run `git submodule update --init --recursive`
- **Hugo extended**: The theme requires Hugo Extended (SCSS compilation). Standard Hugo will fail
- **Blog path**: Content in `content/blog/` will NOT appear in the `{{</* blog */>}}` shortcode — must be `content/posts/`
- **CNAME**: The `CNAME` file must exist in the repo root AND be written to `gh-pages` branch (the deploy workflow handles this)
- **Image paths**: In markdown, reference as `/images/filename.png` (relative to `static/`)

## Content Guidelines

- Pages use the theme's built-in components: `{{</* grid */>}}` for feature cards, `{{</* admonition */>}}` for callouts
- Keep pages focused — detailed API docs live on ReadTheDocs, not here
- Gallery entries: image + code snippet + link to full example on RTD

## Deployment

Push to `main` triggers GitHub Actions:
1. Hugo builds to `public/`
2. JupyterLite builds to `public/try/repl/`
3. Pagefind indexes `public/`
4. `peaceiris/actions-gh-pages` deploys to `gh-pages` branch
5. GitHub Pages serves from `gh-pages` with custom domain `bamengine.org`

## Related Repositories

| Repo | Purpose |
|------|---------|
| [kganitis/bam-engine](https://github.com/kganitis/bam-engine) | Main library (source, tests, docs, benchmarks) |
| [kganitis/bamengine.org](https://github.com/kganitis/bamengine.org) | This repo — project website |
