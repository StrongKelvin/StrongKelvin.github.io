## Why

`src/pages/tags/[tag].astro` 目前使用最簡陋的 `<ul>` 列表和無樣式的 `<BlogPost>` 元件（僅產出裸 `<li><a>`），與網站整體採用卡片式設計、雙欄 grid 佈局、Profile hero 等風格完全不一致。這個差異讓標籤篩選頁面看起來像未完成的作品。

## What Changes

- `src/pages/tags/[tag].astro`：改為與其他內容頁面一致的佈局結構（Profile hero + `.main` 雙欄 grid + Sidebar），文章列表改為卡片樣式
- `src/components/BlogPost.astro`：從裸 `<li><a>` 升級為 `.post-card` 風格卡片元件，包含日期、描述、標籤等後設資訊
- 無 Breaking Changes

## Capabilities

### New Capabilities
- `tag-page-layout`: 標籤篩選頁面的完整佈局，包含 Profile hero、雙欄 grid、Sidebar、統計資訊

### Modified Capabilities

<!-- No existing specs are modified -->

## Impact

- `src/pages/tags/[tag].astro`：大幅改寫 template 部分
- `src/components/BlogPost.astro`：需擴充 props 以接收 date、description、tags 等欄位
