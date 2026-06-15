## Why

隨著部落格文章與標籤數量增加，Sidebar 中的「分類」卡片列出所有 tag，在 tags 超過 10 筆時卡片過長，影響側邊欄整體視覺平衡與操作體驗。需要限制可視高度並提供排序切換功能。

## What Changes

- 限制「分類」卡片高度，使其最多顯示 title + 10 筆分類資料，超出部分出現垂直捲軸
- 在「分類」title 右側新增排序切換按鈕，可切換「依名稱排序」與「依熱門度（文章數）排序」
- 預設排序維持現狀：先依文章數量降冪，同名時依名稱字母升冪

## Capabilities

### New Capabilities
- `category-sort-toggle`: 分類卡片的排序切換功能，支援名稱與熱門度兩種排序模式

### Modified Capabilities
- `sidebar-categories`: 限制分類卡片最大可視高度並加入垂直捲軸；title 右側新增排序切換 UI

## Impact

- `src/components/Sidebar.astro`：修改分類區塊的 CSS 與邏輯
- 新增少量 client-side JS（或 Preact component）處理排序切換的互動狀態
