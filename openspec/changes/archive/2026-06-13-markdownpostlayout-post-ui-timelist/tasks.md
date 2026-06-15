## 1. Create PostTimelineList Component

- [x] 1.1 Create `src/components/PostTimelineList.astro` with props interface (`posts`, `excludeSlug?`, `limit?`, `groupByYear?`, `accordion?`)
- [x] 1.2 Implement year grouping logic: sort posts by date descending, group by year
- [x] 1.3 Implement filtering logic: apply `excludeSlug` and `limit` props
- [x] 1.4 Render timeline HTML structure: `.timeline` container, `.year-group` sections with year header (`.year-label` + `.year-count` + `.year-arrow`), `.post-list` with `.post-item` entries (date, title link, tags)
- [x] 1.5 Add tl-needle-glow CSS: vertical line (1.5px), solid dot (9x9px with 3-layer glow on open), year header self-glow (background + box-shadow), collapsible animation (max-height/opacity transition)
- [x] 1.6 Implement accordion client JS: click year header to toggle `.is-open`, close all others, first year open by default
- [x] 1.7 Add dark mode support via `data-theme` CSS variables
- [x] 1.8 Add responsive styles for mobile (<=768px): reduced padding, smaller year font, wrapped tags
- [x] 1.9 Verify component renders correctly with empty array, single year, multi-year, and with/without accordion

## 2. Integrate Timeline into MarkdownPostLayout

- [x] 2.1 Import `PostTimelineList` in `MarkdownPostLayout.astro`
- [x] 2.2 Build filtered recent posts list: sort all posts, exclude current article by `post.id`, limit to 5
- [x] 2.3 Add timeline section after `<div class="post-content">` with heading "近期文章" and `accordion={false}`
- [x] 2.4 Verify the current article is excluded and only 5 recent posts appear in expanded view

## 3. Integrate Timeline into Blog and Archive Pages

- [x] 3.1 Replace inline card list in `src/pages/blog.astro` with `PostTimelineList` (all posts, accordion enabled)
- [x] 3.2 Replace inline card list in `src/pages/@blog.astro` with `PostTimelineList` (all posts, accordion enabled)
- [x] 3.3 Verify `/blog` and `/@blog` pages render correctly with tl-needle-glow styling
- [x] 3.4 Run `npm run build` to confirm no build errors
