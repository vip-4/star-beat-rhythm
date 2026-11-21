# 星節奏 Star Beat — 原創靜態 HTML5 節奏遊戲

一款完全原創的四軌節奏遊戲。**所有圖形由 Canvas 2D 繪製，所有音樂與音效由 Web Audio API 即時合成**，沒有外部圖片、音檔、字型或第三方套件，可直接部署到任何靜態托管平台。

> 本作品為獨立原創遊戲，未使用 Friday Night Funkin' 或任何既有節奏遊戲的美術、音樂、程式碼或商標。FNF 的素材授權禁止公開發布，故本專案從零製作原創內容。

---

## 專案結構

```
rhythm-static/
├── index.html               # 語意化首頁 + SEO/GEO meta + JSON-LD
├── css/style.css            # RWD、淺色主題、無障礙樣式
├── js/game.js               # 狀態機、譜面、Canvas 渲染、Web Audio、粒子池
├── og-image.png             # 社群分享圖（1200×630）
├── .nojekyll                # 停用 GitHub Pages 的 Jekyll
├── _headers                 # Cloudflare Pages 安全標頭與快取規則
├── robots.txt
├── sitemap.xml
├── llms.txt                 # 生成式引擎友善摘要
└── tools/
    ├── make_og.py           # 重新產生 og-image.png
    ├── smoke-test.js        # 不需瀏覽器的狀態機煙測
    ├── github_pages_deploy.py
    ├── cloudflare_pages_deploy.py
    └── gitee_atomgit_sync.py
```

---

## SEO / GEO 實作

- 語意化 `<header>/<nav>/<main>/<section>/<article>/<aside>/<footer>`
- 完整 `title`、`description`、`keywords`、canonical、Open Graph、Twitter Card
- JSON-LD：`WebSite`、`Organization`、`WebPage`、`GameApplication`、`FAQPage`（5 組問答）
- FAQ 文字與 JSON-LD 內容一致，提高精選摘要與 AI 引用機會
- `llms.txt` 提供核心事實、操作方式、判定規則與引用建議
- 所有重要內容均為真實 HTML 文字，不藏在 Canvas 中

---

## 操作方式

- 鍵盤：`D`、`F`、`J`、`K`，或方向鍵 `←`、`↓`、`↑`、`→`
- 手機：畫面下方四個觸控軌道按鈕
- `Space`：開始／暫停切換（焦點不在按鈕上時）
- 判定：70ms 內 Perfect（300 分）；140ms 內 Good（100 分）；超過 180ms 為 Miss

---

## 部署

正式網址（GitHub Pages）：https://vip-4.github.io/star-beat-rhythm/

原始碼備份：
- GitHub：https://github.com/vip-4/star-beat-rhythm
- Gitee：https://gitee.com/vip882/star-beat-rhythm
- AtomGit：https://atomgit.com/zzw1208/star-beat-rhythm

部署腳本（憑證僅由環境變數傳入，切勿寫入檔案）：

```bash
# GitHub Pages
GH_TOKEN=<token> GH_REPO=star-beat-rhythm python tools/github_pages_deploy.py

# Cloudflare Pages
CF_ACCOUNT_ID=<account> CF_PROJECT_NAME=star-beat-rhythm CF_API_TOKEN=<token> \
  python tools/cloudflare_pages_deploy.py

# Gitee / AtomGit 原始碼同步
GITEE_TOKEN=<token> ATOMGIT_TOKEN=<token> python tools/gitee_atomgit_sync.py
```

本機驗證：

```bash
node tools/smoke-test.js
python -m http.server 8080 -d .
```

---

## 授權與聲明

本專案原始碼與原創素材可自由使用；不含任何第三方遊戲素材。若日後加入外部素材，請另行確認授權條款。本網站僅供娛樂與技術展示，免費遊玩，無內購、無註冊、無現金交易。
