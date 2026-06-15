## Why

Sidebar 中的「分類」目前使用硬編碼的假資料（6 個固定分類與 slug），與實際文章標籤脫節，導致分類計數與真實內容不符，降低站點可信度。

## What Changes

- 移除 Sidebar.astro 中硬編碼的 `categories` 陣列
- 改從 `allPosts` 中的 tags 動態統計產生分類清單與計數
- 保持「分類」區塊的 URL 結構（`/tags/{slug}`）與現有標籤頁面相容

## Capabilities

### New Capabilities

無新增能力。

### Modified Capabilities

無規格層級需求變更。

## Impact

- `src/components/Sidebar.astro`：移除假資料、改為動態推導
