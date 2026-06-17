## ADDED Requirements

### Requirement: Tag page follows main layout grid

The tag page `<div class="main">` SHALL use the same two-column grid layout as other content pages: `grid-template-columns: 1fr 280px` with `gap: var(--space-xl)` and collapse to single column at `max-width: 768px`.

#### Scenario: Tag page renders in two-column layout on desktop
- **WHEN** the viewport width is greater than 768px
- **THEN** the page content SHALL be displayed in a two-column grid with content on the left and sidebar on the right

#### Scenario: Tag page collapses to single column on mobile
- **WHEN** the viewport width is 768px or less
- **THEN** the page SHALL display content and sidebar in a single column stacked vertically

### Requirement: Tag page includes Profile hero

The tag page SHALL render the `<Profile>` component at the top of the page content area, identical to how `index.astro` and `blog.astro` include it.

#### Scenario: Profile hero appears at top of content
- **WHEN** the tag page loads
- **THEN** the Profile hero SHALL be displayed above the main content grid with avatar, name, subtitle, bio, and tech tags

### Requirement: Tag page includes Sidebar

The tag page SHALL render the `<Sidebar>` component in the right column of the grid, receiving `allPosts` and `allTags` as props.

#### Scenario: Sidebar appears in right column on desktop
- **WHEN** the tag page renders on a desktop viewport
- **THEN** the Sidebar SHALL be visible in the right column of the `.main` grid

#### Scenario: Sidebar appears below content on mobile
- **WHEN** the tag page renders on a mobile viewport (768px or less)
- **THEN** the Sidebar SHALL appear below the main content in a single column

### Requirement: Tag page shows filtered posts as cards

Posts filtered by the selected tag SHALL be displayed using the `.post-card` card pattern with `--color-surface` background, `--radius-md` border-radius, `--color-border` border, and hover effect.

#### Scenario: Filtered posts display as styled cards
- **WHEN** the tag page renders with filtered posts
- **THEN** each post SHALL appear as a card with title, publication date, description, and tag pills

#### Scenario: Post card has hover effect
- **WHEN** the user hovers over a post card
- **THEN** the card border SHALL change to `--color-accent-muted` and display a subtle box-shadow

### Requirement: Tag page displays section title with post count

The page SHALL display a section title in `.section-title` style (small uppercase, `--color-text-secondary`, border-bottom) showing the tag name and post count.

#### Scenario: Section title shows tag name and count
- **WHEN** the tag page renders with tag "astro" and 5 posts
- **THEN** the section title SHALL display text like "標籤：astro（共 5 篇文章）"

### Requirement: BlogPost component renders as full card

The `<BlogPost>` component SHALL accept `title`, `url`, `date`, `description`, and `tags` props and render a full `.post-card` element with all post metadata.

#### Scenario: BlogPost renders card with all metadata
- **WHEN** BlogPost receives title, url, date, description, and tags props
- **THEN** it SHALL render a card containing title as a link, formatted date, description text, and tag pills

#### Scenario: BlogPost renders minimal card when optional props are missing
- **WHEN** BlogPost receives only title and url props (no date, description, tags)
- **THEN** it SHALL render a card containing only the title as a link, with graceful fallback
