## 1. Upgrade BlogPost Component

- [x] 1.1 Extend BlogPost props to accept `date`, `description`, `tags` (optional)
- [x] 1.2 Rewrite BlogPost template to render `.post-card` markup with title link, formatted date, description, and tag pills
- [x] 1.3 Add card styles with CSS variables (`--color-surface`, `--color-border`, `--radius-md`, hover effects)

## 2. Restyle [tag].astro Page Layout

- [x] 2.1 Add `Profile` component import and render at top of page
- [x] 2.2 Wrap content in `<div class="main">` with two-column grid CSS
- [x] 2.3 Add `.section-title` showing tag name and post count
- [x] 2.4 Add `Sidebar` component import and render in right column
- [x] 2.5 Pass `allPosts` and `allTags` to Sidebar (import `getCollection` for full dataset)

## 3. Clean Up

- [x] 3.1 Remove unused commented-out code from `[tag].astro`
- [x] 3.2 Remove `console.log` debug statements
- [x] 3.3 Verify page renders correctly with `npm run dev`
- [x] 3.4 Verify dark mode and responsive layout work
