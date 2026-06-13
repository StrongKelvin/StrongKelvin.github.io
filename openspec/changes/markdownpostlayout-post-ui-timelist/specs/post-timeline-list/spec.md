## ADDED Requirements

### Requirement: Component renders timeline post list
The system SHALL provide a `PostTimelineList.astro` component that renders posts in a vertical timeline layout with year grouping, collapsible year sections (accordion), and glow visual effects matching `preview-timeline.html` tl-needle-glow variant.

#### Scenario: Default timeline rendering
- **WHEN** the component receives an array of posts spanning multiple years
- **THEN** it SHALL render each year as a collapsible section with a year header (year label, post count badge, arrow indicator) and post items arranged vertically with timeline line and dot markers

#### Scenario: Groups posts by year
- **WHEN** posts span multiple years (e.g., 2025 and 2026)
- **THEN** the component SHALL render each year as a separate section with a year heading, posts within each year sorted by date descending, and years ordered newest first

#### Scenario: Respects limit prop
- **WHEN** the `limit` prop is set to `5`
- **THEN** the component SHALL render at most 5 posts across all years combined, newest first

#### Scenario: Excludes a specific post
- **WHEN** the `excludeSlug` prop is set to `"2025/2025-1"`
- **THEN** the component SHALL exclude the post with that ID from the rendered list before applying the limit

#### Scenario: Receives empty posts array
- **WHEN** the `posts` prop is an empty array
- **THEN** the component SHALL render nothing (no timeline container)

### Requirement: Collapsible year sections (accordion)
Year sections SHALL be collapsible via click interaction, with only one year open at a time.

#### Scenario: Click to toggle year
- **WHEN** user clicks a year header
- **THEN** if that year is closed, it SHALL open and all other years SHALL close; if that year is already open, it SHALL close

#### Scenario: First year open by default
- **WHEN** the component renders
- **THEN** the first (most recent) year group SHALL be open by default, all others closed

#### Scenario: Accordion disabled via prop
- **WHEN** the `accordion` prop is set to `false`
- **THEN** all year groups SHALL render expanded and non-collapsible

### Requirement: Component API surface
The component SHALL accept typed props for flexible integration.

#### Scenario: Accepts all defined props
- **WHEN** the component is invoked with `posts`, `excludeSlug`, `limit`, `groupByYear`, and `accordion`
- **THEN** it SHALL apply all props correctly without TypeScript errors

### Requirement: Timeline visual styling (tl-needle-glow)
The visual styling SHALL match the `preview-timeline.html` tl-needle-glow variant exactly, using the site's design tokens.

#### Scenario: Shows vertical timeline line
- **WHEN** the component renders
- **THEN** a vertical line (1.5px, `var(--color-border)`) SHALL appear on the left side spanning the full height of the timeline

#### Scenario: Solid dot with glow on active year
- **WHEN** a year group is open
- **THEN** its dot marker SHALL be 9x9px solid `var(--color-accent)`, scaled 1.4x, with layered box-shadow glow: 4px soft accent ring, 14px wider soft ring, and 32px diffuse outer glow

#### Scenario: Year header self-glow
- **WHEN** a year group is open
- **THEN** the year header SHALL display a rounded background with `oklch(78% 0.10 230 / 0.15)` and a 3-layer box-shadow glow effect

#### Scenario: Year header shows metadata
- **WHEN** the component renders
- **THEN** each year header SHALL display: large year label (1.6rem, bold), post count badge (monospace, rounded pill), and arrow indicator (▶) that rotates 90° when the section is open

#### Scenario: Post items show date, title, tags
- **WHEN** the component renders
- **THEN** each post item SHALL display: monospace date (MM-DD), clickable title link, and inline tag badges on the right side

#### Scenario: Hover effects on post items
- **WHEN** user hovers over a post item
- **THEN** the item background SHALL change to `var(--color-accent-soft)` and the title link SHALL change to `var(--color-accent)`

### Requirement: Collapse animation
Opening and closing year sections SHALL animate smoothly.

#### Scenario: Smooth open/close transition
- **WHEN** a year section is opened or closed
- **THEN** the post list SHALL animate with a `max-height` transition (0.4s cubic-bezier) and `opacity` transition (0.3s ease)

### Requirement: Dark mode support
The component SHALL respect the site's dark mode via `data-theme` attribute.

#### Scenario: Adapts to dark theme
- **WHEN** `data-theme="dark"` is set on `<html>`
- **THEN** all timeline colors SHALL adapt via CSS custom properties, with glow effects rendered against the dark background

### Requirement: Responsive layout
The component SHALL adapt to mobile viewports.

#### Scenario: Mobile single-column
- **WHEN** viewport width is 768px or less
- **THEN** the timeline padding-left SHALL reduce from `var(--space-xl)` to `var(--space-lg)`, year label font SHALL reduce to 1.3rem, and post items SHALL wrap tags below the title

### Requirement: Integration in MarkdownPostLayout
The `MarkdownPostLayout.astro` SHALL include a "近期文章" timeline section at the bottom of the article.

#### Scenario: Recent posts section at article bottom
- **WHEN** `MarkdownPostLayout.astro` renders
- **THEN** it SHALL include a timeline of the 5 most recent posts (excluding the current article), positioned after the `<div class="post-content">` section, with accordion disabled (all years expanded)

#### Scenario: Excludes current article
- **WHEN** rendering the recent posts timeline
- **THEN** the current article SHALL NOT appear in the timeline list

#### Scenario: Static expanded view
- **WHEN** rendering inside `MarkdownPostLayout`
- **THEN** the timeline SHALL show all available years fully expanded without collapsible behavior

### Requirement: Integration in /blog and /@blog pages
The `/blog` and `/@blog` pages SHALL use `PostTimelineList` with accordion behavior.

#### Scenario: /blog uses timeline
- **WHEN** `/blog.astro` renders
- **THEN** it SHALL render all posts in timeline format with accordion enabled and groupByYear=true

#### Scenario: /@blog uses timeline
- **WHEN** `@blog.astro` renders
- **THEN** it SHALL render all posts in timeline format with accordion enabled and groupByYear=true
