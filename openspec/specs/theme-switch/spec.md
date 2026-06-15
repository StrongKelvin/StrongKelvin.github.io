## 新增需求

### 需求：Header 顯示主題切換按鈕
Header 的導覽列最右側 SHALL 顯示一個可點擊的主題切換按鈕。該按鈕 SHALL 使用 ThemeIcon.astro 中的 SVG 太陽／月亮圖示來表示當前主題。

#### 情境：切換按鈕出現在 Header 中
- **WHEN** 頁面載入完成
- **THEN** Header 最右側（搜尋按鈕旁）SHALL 顯示主題切換按鈕

### 需求：使用者可在淺色與深色主題之間切換
點擊主題切換按鈕 SHALL 切換頁面的淺色／深色配色方案。當前選擇 SHALL 透過 `localStorage` 以 `theme` 作為鍵值進行持久化。

#### 情境：點擊切換主題
- **WHEN** 使用者點擊主題切換按鈕
- **THEN** `document.documentElement` 上的 `dark` class SHALL 被切換
- **AND** 太陽／月亮圖示 SHALL 更新以反映當前主題

#### 情境：主題在頁面重新載入後保持不變
- **WHEN** 使用者選擇深色主題並重新載入頁面
- **THEN** 頁面 SHALL 以深色主題渲染且無閃爍
- **AND** `dark` class SHALL 在首次繪製前被套用

### 需求：全域定義深色主題 CSS 變數
全域 CSS（`src/styles/global.css`）SHALL 在 `html.dark` 選擇器下定義一組完整的深色主題 CSS 變數覆寫。變數 SHALL 包含 `--color-bg`、`--color-surface`、`--color-border`、`--color-text`、`--color-text-secondary`、`--color-accent`、`--color-accent-soft`、`--color-accent-muted` 以及 `--color-tag-bg`。

#### 情境：深色模式呈現正確顏色
- **WHEN** `html` 元素帶有 `dark` class
- **THEN** 頁面 SHALL 對所有顏色屬性使用深色主題 CSS 變數
- **AND** 背景顏色 SHALL 為深色（oklch 亮度約 17-22%）
- **AND** 文字顏色 SHALL 為淺色（oklch 亮度約 88%）

### 需求：Header 背景隨主題自動適應
Header SHALL 使用 `var(--color-surface)` 作為背景色，搭配 `backdrop-filter: blur(12px)`，使其自動適應淺色與深色主題。

#### 情境：淺色模式下 Header 比瀏覽器網址列深
- **WHEN** 頁面處於淺色主題
- **THEN** Header 背景 SHALL 為 `var(--color-surface)` 搭配 0.82 不透明度與模糊效果
- **AND** 其視覺外觀 SHALL 與瀏覽器網址列背景有明顯區別

#### 情境：深色模式下 Header 呈現暗色
- **WHEN** 頁面處於深色主題
- **THEN** Header 背景 SHALL 使用深色 `--color-surface` 值
- **AND** 底部邊框 SHALL 使用深色 `--color-border` 值
