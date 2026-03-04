# Scientific Python Hugo Theme Reference

Quick reference for the [scientific-python-hugo-theme](https://github.com/scientific-python/scientific-python-hugo-theme) as used in bamengine.org.

## Shortcodes

### Grid (feature cards)

```markdown
{{</* grid columns="1 2 2 3" */>}}

[[item]]
type = 'card'
title = 'Card Title'
body = '''
Card content in TOML multi-line string.
'''

{{</* /grid */>}}
```

`columns="1 2 2 3"` = responsive breakpoints: mobile, tablet, desktop, wide.

### Blog highlights

```markdown
{{</* blog */>}}
```

Renders latest posts from `content/posts/` section. No parameters.

### Admonition

```markdown
{{</* admonition note */>}}
Content here.
{{</* /admonition */>}}
```

Types: `note`, `warning`, `tip`.

## Config Options

All layout is driven by `config.yaml`. Key sections:

- `params.hero`: Landing page hero (title, subtitle, image, button)
- `params.navbar`: Top navigation links and dropdowns
- `params.footer`: Footer columns, social links, logo
- `params.navbarlogo`: Logo in navbar (image path relative to `static/images/`)
- `params.colorScheme`: `"auto"` | `"light"` | `"dark"`
- `params.search`: `true` enables Pagefind search
- `params.fonts`: Google Fonts to load

## Dark Mode

The theme adds `theme-switch-dark` / `theme-switch-light` classes to `<body>`. Override styles in `assets/css/custom.css`:

```css
body.theme-switch-dark .hero-title img {
  content: url("/images/logo-dark.svg");
}
```

## Blog Post Front Matter

```yaml
---
title: "Post Title"
date: 2026-03-04
authors:          # MUST be "authors" (list), NOT "author"
  - Author Name
---
```

Use `<!--more-->` to set the summary cutoff for listings.

## External Links in Navbar

```yaml
- title: Docs
  url: https://bam-engine.readthedocs.io
  is_external: true
```
