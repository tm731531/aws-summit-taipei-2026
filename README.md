# AWS Summit Taipei 2026 — 議程筆記

> AWS Summit Taipei 2026 的個人參會筆記。每天一個**日期資料夾**，內含當天整理好的 Markdown 筆記。GitHub 會自動渲染成網頁，直接點檔案就能讀。

## 活動資訊
- **活動**：AWS Summit Taipei 2026（公開議程 50 場）
- **場地**：TICC 台北國際會議中心
- **期程**：兩天（2026-07-15 ~ 2026-07-16）
- **選場依據**：[我的推薦文 — 企業 AI 落地三角度](https://blog.tomting.com/2026/07/10/aws-summit-taipei-2026-enterprise-ai-sessions/)
- **筆記方式**：現場錄音（本地 faster-whisper 轉錄，不上雲）＋ 補拍條列多的投影片 → 事後整理成 Markdown，並經 AWS 官方文件查核修正。

## 🎯 選場的三個角度

推薦文用這三條篩掉 50 場裡的雜訊：

1. **讓團隊用起來** — 開發流程、工程實踐
2. **基建擴展與地端支援** — 平台架構、K8s、遷移
3. **自有資料的治理與安全** — governance、合規

## 📅 議程與筆記

### Day 1 — 2026-07-15（三）｜[筆記](2026-07-15/notes.md)

| 時間 | 場次 | 角度 |
|------|------|------|
| 10:00–11:00 | Keynote | 開場總覽 |
| 11:30–12:15 | MOD01: AI-Driven Development Lifecycle | ① 讓團隊用起來 |
| 13:30–14:15 | KIRO02: AI Engineering with Prompt/Context/Harness | ① 團隊工程實踐 |
| 14:30–15:00 | KIRO05: From Vibe Coding to Spec-Driven Approach | ① 標準化 AI 開發 |
| 15:15–16:00 | MOD03: Multi-Tenant AI Platform on EKS（BitoGroup 案例）| ② 平台架構 |
| 16:15–17:00 | MOD04: Kubernetes Platform with EKS Auto Mode | ② 維運擴展 |

### Day 2 — 2026-07-16（四）｜[筆記](2026-07-16/notes.md)

| 時間 | 場次 | 角度 |
|------|------|------|
| 10:00–11:00 | Keynote | 閉幕總結 |
| 11:30–12:15 | AIML05: Enterprise AI Agents（HOYA BIT 案例）| ② 平台落地實作 |
| 下午 | **用 Kiro 做 AI HR 小幫手**（改去）| ① Kiro 實作落地 |
| ~~13:30–14:15~~ | ~~SEC01: Multi-Tenant AI Agent Governance SaaS~~ | ~~③ 治理框架~~ |
| ~~14:25–15:05~~ | ~~FINTECH02: On-Premises to Agentic AI with Multi-Agent~~ | ~~② 地端遷移~~ |

> 💡 這一跳其實讓 **角度 ①（讓團隊用起來）收成一條完整線**：Day 1 的 KIRO02（工程實踐）+ KIRO05（spec-driven 方法論）是理論，Day 2 這場是拿 Kiro 真的做出 HR 小幫手 —— 方法論 → 實作，整理筆記時可以互相對照驗證。
>
> ⚠️ 代價是**角度 ③（治理與安全）整條沒有現場覆蓋** —— SEC01 是那條線唯一的場次，沒有替補。會後看 AWS 有無放簡報/錄影再補。

## 🔧 錄音 → 筆記流程

```bash
# 1. 錄音丟進當天的 VOICE/
cp ~/錄音/*.aac 2026-07-15/VOICE/

# 2. 本地轉錄（medium model, CPU int8, 逐 5 分鐘自動偵測語言）
./transcribe.py 2026-07-15
# → 產出 2026-07-15/VOICE/transcripts/*.txt
# 實測 1.24x realtime：5 小時錄音約需 4 小時，晚上丟著跑

# 3. Cerebras 結構化摘要（map-reduce，免費雲端，快）
source ~/.config/llm/keys.env
./summarize.py 2026-07-15
# → 產出 2026-07-15/VOICE/transcripts/*.summary.md

# 4. 摘要 + 投影片 → 人工彙整校正進 2026-07-15/notes.md
```

**依賴**
- `transcribe.py` → **`/home/tom/whisper-venv`**（faster-whisper 1.2.1，系統 python 沒有，shebang 已指這個 venv）＋ `ffmpeg` / `ffprobe`
- `summarize.py` → `CEREBRAS_API_KEY`（在 `~/.config/llm/keys.env`，記得先 `source`）

**兩支腳本都可重入**：`transcribe.py` 重跑會覆寫；`summarize.py` 已有 `.summary.md` 的會跳過（斷點續傳，免費層被限速中斷也不怕）。

> ⚠️ **摘要是待查核的草稿，不是筆記**。Cerebras 只壓縮不查證，whisper 的同音字錯誤會被它一路帶進摘要。事實（AWS 服務名、數字、架構決策）一律回頭對逐字稿或 AWS 官方文件。

## 📂 每個日期資料夾的結構

| 路徑 | 放什麼 | 上傳? |
|------|--------|-------|
| `notes.md` | 整理好的筆記（**這個 repo 的主體**） | ✅ |
| `VOICE/` | 上課錄音 + `transcripts/` 逐字稿 | 🚫 |
| `slides/` | 投影片翻拍照片 | 🚫 |
| `clips/` | 操作示範影片切段；只有 `.md` 重點筆記會上傳 | 🚫（`.md` 除外）|

## ℹ️ 這個 repo 收錄範圍
- ✅ **收錄**：整理好的 Markdown 筆記、對照表、指令速查。
- 🚫 **不收錄**（`.gitignore` 排除）：投影片照片、上課錄音、逐字稿、講義 PDF —— 體積大且含現場聲音/版權內容，只留在本機。

## 🔗 實用資源
- [AWS 官方文件](https://docs.aws.amazon.com/)（查核事實用）
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS Summit Taipei](https://aws.amazon.com/tw/events/summits/taipei/)（會後簡報/錄影通常放這）
