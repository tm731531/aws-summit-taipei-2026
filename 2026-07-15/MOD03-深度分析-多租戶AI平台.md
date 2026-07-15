# MOD03 深度分析：BitoGroup 如何在 Amazon EKS 上蓋一座多租戶 AI Agent 平台

> **場次**：MOD03「每個團隊都有自己的 AI」｜2026-07-15 15:15–16:00｜📍 Room 201DEF｜Level 300
> **講者**：H.C.（AWS Solutions Architect，專精 Fintech / Container）＋ Michael（BitoGroup 維運經理）
> **來源**：現場錄音逐字稿（37 分鐘）＋ 現場投影片 50 張
> **可信度標記**：✅ 投影片可查證　🎤 僅講者口述（投影片無）　⚠️ 存疑，見文末待查核

---

## TL;DR

BitoGroup（幣托集團，受金管會監管的台灣虛擬貨幣交易所）不能用外部 AI SaaS —— 資料不能外流。他們也不想從零自建 —— AI 進步太快跟不上。最後選的路是：**站在開源專案 OpenClaw 上，用公司既有的 Amazon EKS 蓋一座多租戶 AI Agent 平台「BitoClaw」**，讓每個部門、每個團隊都有自己的 agent，但資料、工具、權限、成本全部由平台統一控管。

三個最值得偷的東西：

1. **「多租戶設計是讓團隊感覺不到邊界的存在」** —— 使用者只要用，安全性由平台扛。這是整場的設計哲學。
2. **不要把隔離等級一次拉到最高**。AWS SA 花了半場講 runtime 隔離的取捨，結論是 runc / gVisor / Kata 應該**混用**，按 trust level 選，全開最高級別是浪費資源的錯誤做法。
3. **KEDA 把閒置租戶縮容到零** —— 100 個租戶省 80% 成本。這是「每個團隊都有自己的 AI」在經濟上可行的關鍵。

---

## 一、為什麼企業不能直接拿 OpenClaw 來用

H.C. 開場先講現況：autonomous agent 爆紅，OpenClaw 的 GitHub star 曲線在幾個月內暴衝 ✅（143/146 有 `openclaw/openclaw` 的 star-history 圖），支援 Discord / Telegram / Slack 等一堆整合，社群貢獻大量 Skills。

然後他把場子拉回現實 —— **「Security Risks of Ungoverned OpenClaw」** ✅（147/149，引用 OWASP 2026 Top 10 Agentic 與 Oasis Security Research）：

| 風險 | 等級 | 現場投影片數字 |
|---|---|---|
| Prompt Injection | Critical | — |
| 惡意 Skill 供應鏈 | Critical | ClawHavoc 事件成長 **142%**；**1,184** 個惡意 plugin；**39** 個惡意 skill 散布 macOS 資訊竊取程式 |
| 原始碼漏洞 | High | 截至 2026-03 有 **82 個已知 CVE**（12 critical + 21 high）|
| 憑證外洩 | High | **80,000+** 個 instance 曝露，明文憑證 |
| 企業資料外洩 | High | **36.8%** 的社群 plugin 有安全問題 |

最刺眼的一個數字：**999,000+ 個 OpenClaw instance 曝露在公網** ✅（Oasis Security Research，參考站 `https://declawed.io/`）。H.C. 在台上說這份資料「我前兩天才更新到的」🎤。

> **這一段的價值**：它把「agent 好玩」和「agent 能進 production」之間那道牆講清楚了。個人玩 agent 不會遇到 isolation、成本追蹤、合規 —— 企業全都會遇到。

### 部署光譜：你在哪一格？

H.C. 給了一個由左到右的光譜 🎤：

```
本機自建            租雲端機器          容器編排           AgentCore
(Mac mini、           (小型 instance)     (EKS / ECS)      (託管)
 本地跑 agent)                            ← 今天講這格 →
─────────────────────────────────────────────────────────────→
          自由度高                                    隔離天生好
          管理難                                      轉換成本高
```

- **最右邊的 AgentCore**：by nature 每個 runtime 都是 micro-VM 隔離，顆粒度天生就好 🎤。但團隊要轉換沒那麼快 —— H.C. 拿早期 serverless vs container 的轉換成本做類比。
- **今天聚焦第三格（Kubernetes）**：因為大部分企業已經有 EKS / ECS cluster，開發習慣不用被破壞。

---

## 二、BitoGroup 的決策路徑（這段是精華）

### 背景與痛點

BitoGroup 在台灣 10 幾年，從虛擬貨幣錢包 → 交易所（BitoPro）→ BitoPay → 企業穩定幣 🎤。Michael 2012 年加入，從 0 到 1 建立核心團隊。

**關鍵約束：受金管會監管** 🎤。Michael 原話：「資料是不能外流的」。

三個痛點 🎤：

1. **人均效能** —— 大量規範、大量維運、大量例行事務吃掉時間
2. **部門落差** —— 各部門都想用 AI，但有人怕、有人擅長、有人只是觀望，期待完全不一樣
3. **合規** —— 這是硬約束，不是偏好

### 三個選項，怎麼砍掉兩個

| 選項 | 為什麼不選 / 選 |
|---|---|
| **外部 SaaS 平台** | ❌ 資料要流到第三方 → **直接排除**，一秒都沒考慮 |
| **完全自建** | ❌ 自建很快（現在有 AI 輔助），但 **AI 進步速度太快，跟不上** |
| **站在開源多租戶框架上自建** | ✅ 最終選擇 —— 投影片上寫的就是「**OpenClaw 路線**」✅（120「導入策略 權衡分析」）|

Michael 特別澄清動機 🎤：

> 「我們做 BitoClaw 這個 AI 平台，不是因為要炫富，不是要追逐最新的 AI 工具。我們真的想解決的問題，就是 **AI 工具孤島**的問題。」

因為每個人各自接不同的 MCP、不同的服務 ——「但我身為資安主管，我可能也無法控管」。

### 決策的三個標準 🎤

1. **控制權** —— 控制資料與模型的落點，一切符合合規
2. **去中心化** —— 不想被單一 LLM 供應商綁架，想用哪個就哪個
3. **成本** —— **公司本來就有 Amazon EKS**，把既有資源極大化

投影片上的客戶金句 ✅（148）：

> **「選擇 Amazon EKS，不是追逐潮流，而是把團隊已經會的技能，變成平台的競爭力。」** —— Michael，BitoGroup 維運經理

> 💡 **這句話是整場最值得帶走的決策原則**。技術選型的理由不是「這個最潮」，而是「這個讓我們既有的沉沒技能變成資產」。

---

## 三、架構

### 全貌 ✅（100「平台架構總覽」）

| 層 | 技術選擇 |
|---|---|
| **前端** | Next.js + React + TypeScript + Tailwind CSS；CloudFront + S3 靜態部署 |
| **平台控制層** | Go + chi 路由框架；Amazon EKS；AWS CDK；**Rust Operator（kube-rs）** |
| **自動化與擴展** | ArgoCD + Helm GitOps；**KEDA HTTP Add-on**（閒置租戶縮容至零）|

> 注意 **Rust Operator（kube-rs）** 這個選擇 —— 自己寫 K8s operator 而不是用現成的，這是願意付工程成本換控制權的訊號。

### 雲端架構圖 ✅（116）

```
Route 53 → WAF → CloudFront → VPC (NAT Gateway, ALB)
                                 ├── AZ-A ┐
                                 └── AZ-B ┴─ EC2 Auto Scaling / Fargate
                                              ↓
                              Amazon EKS Cluster (Multi-Tenant)
                                              ↓
        S3 / Bedrock / Secrets Manager / ECR / EventBridge / SNS / EBS Snapshot

監控側：CloudWatch / CloudTrail / CloudWatch Logs / Alarms
```

### 租戶生命週期：5 步驟全自動 ✅（106「從登入到就緒，全程自動化」）

1. **Google SSO 登入** —— 驗證 ID Token 及 email 網域白名單
2. **Lambda 自動佈建** —— 建立 Secrets Manager + **Pod Identity**
3. **Rust Operator 啟動** —— 建立 Namespace + ArgoCD Application
4. **GitOps 同步部署** —— ArgoCD 自動同步 Helm chart
5. **租戶存取就緒** —— `https://claw.example.com/t/{tenant}/`、`https://{tenant}.hermes.example.com/`

> **零 API 金鑰架構** ✅（123）：透過 **Pod Identity** 直接存取 Bedrock，「從根本消除金鑰洩露風險」。這是整個架構最漂亮的一手 —— 不是「把金鑰保管好」，而是「讓金鑰不存在」。

### 使用者體驗 🎤

打開公司 **Slack** → tag 頻道 → tag BitoClaw → 直接跟 agent 對話。冷啟動不到 10 分鐘（因為租戶被縮到零，要喚醒）。

### 多框架支援 ✅（134）

租戶可以選不同的 agent 框架：**Strands / OpenClaw / Hermes / Kiro**。onboarding 時 tenant-2 選 OpenClaw、tenant-3 選 Hermes。這呼應「去中心化、不被綁架」的決策標準。

### MCP / Skills 生態 ✅（108）

```
MCP Servers: GitLab, Grafana, Metabase, ClickUp, Slack, Jenkins
                          ↓
                      BitoClaw
                          ↑
Skills: bitopro-spot, bitopro-market-intel, clickup-ticket-creator,
        security-skill, monitor-skill
```

**治理重點** 🎤：各部門原本自建自己的 MCP，完全無法管。現在全部集中到平台核心，**統一使用、統一授權** —— 哪些部門可以用哪些 MCP，由平台決定。

BitoPro 的 Skill 是真的可以裝的 ✅（121）：
```
npx clawhub install bitopro-spot
npx clawhub install bitopro-market-intel
```

---

## 四、隔離：這場最硬的技術乾貨

### 4.1 租戶隔離的四個層級 ✅（132/133「Tenant Isolation & Security」）

光譜從 Dedicated 到 Shared：

| 層級 | 做法 | 成本 |
|---|---|---|
| **Cluster-level** | 每個團隊一個獨立 cluster | 物理隔離最強，**成本最高** 🎤 |
| **Namespace-level** | 共用 cluster，分 namespace | ← BitoGroup 選這個 |
| **Pod-level** | 共用 namespace，分 pod | |
| **App-level** | 共用 pod | 最省，隔離最弱 |

H.C. 的建議 🎤：**namespace + pod level** 就是甜蜜點，借用 Kubernetes 天生的功能就好。

### 4.2 BitoGroup 的 EKS 多租戶隔離設計 ✅（107，**四個機制**）

1. **Namespace** —— 租戶隔離
2. **NetworkPolicy** —— **預設 Deny All**，再適時開放
3. **RBAC** —— 最小權限原則
4. **ResourceQuota** —— 資源上限

> ⚠️ 逐字稿裡 Michael 說「4 層安全架構」，我原本以為是縱深防禦的四層。對照投影片後發現**「4」指的是這四個 EKS 隔離機制**，而真正的縱深防禦是 **10 層**（見下節）。這是 whisper + 口語省略造成的誤解，已修正。

### 4.3 Agent 在 Pod 裡跑的三種模式 ✅（135「Challenge with running agents in a pod」）

| 模式 | 說明 | 適用 |
|---|---|---|
| **① Agentic Loop** | loop 在標準 pod 裡呼叫工具 / API | 受信任的工具 |
| **② Remote Sandbox** | 編排 loop 在標準 pod，把**程式碼執行**派到隔離 sandbox | 需要執行特殊工具時 |
| **③ Full Background Agent** | loop + 產碼 + 執行全部在一個隔離 sandbox 裡 | 最高風險工作負載 |

### 4.4 Runtime 比較表（⭐ 本場最有價值的一張投影片）

✅（112「Runtime Comparison」）—— **這張表逐字稿完全沒唸出數字，只有投影片有**：

| 屬性 | runc | gVisor | Kata Containers |
|---|---|---|---|
| **隔離機制** | Namespaces + cgroups | User-space kernel | Micro-VM (KVM) |
| **安全邊界** | Soft（**共用 kernel**）| Strong（app kernel）| **Strongest**（自有 kernel）|
| **冷啟動** | **<1ms** | ~10ms | **~100–200ms** |
| **記憶體額外開銷** | ~0MB | ~20MB | **~128MB** |
| **Syscall 相容性** | **100%** | ~70–80% | 100% |
| **效能影響** | 無 | 低～中 | 中 |
| **OCI 相容** | Yes | Yes (runsc) | Yes (kata-runtime) |
| **最適合** | 受信任的工作負載 | 安全/效能平衡 | **高度不受信任的程式碼** |

個別細節卡 ✅（138/139/140）：
- **runc**（138）：<1ms 冷啟動 / ~0MB 額外開銷 / 100% syscall 相容 / 共用 kernel
- **gVisor**（139）：~10ms 冷啟動 / ~20MB 記憶體開銷 / 70%+ syscall 覆蓋 / Go 語言實作
- **Kata Containers**（140）：~150ms 開機 / ~128MB 記憶體開銷 / 100% syscall 相容 / KVM hypervisor

**H.C. 的比喻**（口語，很好記）🎤：
- **runc** = 公司裡最資深、能力最強的老員工。什麼都懂，速度非常快。唯一要注意的是 —— 哪天他剛好中毒了，就有點麻煩。
- **gVisor** = 銀行的防彈玻璃。隔了一層讓你不直接接觸，但它不是絕對打不破，「其實還是會有機會」。

### 4.5 選 runtime 的四個面向 ✅（110「Choosing the Right Runtime」）

| 面向 | 選擇 |
|---|---|
| **Trust Level** | Untrusted → Kata 或 gVisor；Trusted → **runc** |
| **Performance Needs** | 延遲敏感 → runc 或 gVisor；高吞吐 I/O → **runc** |
| **Resource Density** | 高 pod 密度 → runc 或 gVisor；要強隔離 → Kata |
| **Compliance** | 法規要求 → **Kata**；一般 → gVisor |

> 🔑 **H.C. 在結尾特別強調的重點** 🎤：
> 「不要覺得我一次全部都拿最高級別的全部合拍上去，這樣就是沒有問題 —— 其實這個方法是**很有問題的**。原因在於你其實會花很多資源。」
>
> 正確做法是 **mix**：Sandbox Controller 允許同一個 cluster 裡混用不同 runtime，「你並不需要去選擇一個然後放棄另外幾個」。

### 4.6 Sandbox 怎麼實作 ✅

**Building Sandcastles**（112/113）：
> Sandbox Manager 掌管生命週期並與 Kubernetes API 溝通。Sandbox Router 用 `X-Sandbox-ID` header 把執行請求代理到正確的 pod。兩者都在同一個 ALB 後面。每個 pod template 上的 **RuntimeClass** 決定這個 session 跑在 gVisor 還是 Kata+Firecracker。

**Agent Sandbox Controller**（137）—— 用 K8s CRD 管理生命週期：
- `SandboxTemplate`
- `SandboxClaim`
- `Sandbox`
- `SandboxWarmPool` ← **預先開好的閒置 sandbox，降低冷啟動延遲**

**RuntimeClass 用法**（136）：
```yaml
spec:
  runtimeClassName: gvisor
```
換 isolation 只要改 runtime class，**上層 workload 不用動** 🎤。

### 4.7 一個重要的時間點 ✅（142）

> Until **February 16, 2026**, Kata Containers with Firecracker required **bare-metal EC2 instances**, since Firecracker depends on KVM. **EC2 nested virtualization on C8i, M8i, and R8i instances** removed that constraint. Both runtimes can now run on standard virtual EC2 instances and integrate into an existing EKS cluster without changes.

**白話**：2026 年 2 月 16 日之前，要跑 Kata + Firecracker 必須用 bare metal 機器（貴、綁定）。現在 C8i / M8i / R8i 支援 nested virtualization，**普通 EC2 就能跑，而且能直接併進現有 EKS cluster 不用改架構**。

> 這是「Kata 從理論選項變成實務選項」的分水嶺。如果你上次評估 Kata 是 2025 年，結論該重算了。

---

## 五、資安與合規

### 10 層縱深防禦 ✅（123「安全架構：10 層縱深防禦」）

1. 邊緣防護
2. 身分驗證
3. 網路隔離
4. 帳號授權
5. 租戶隔離
6. 密鑰管理
7. LLM 存取
8. **成本控制** ← 注意：成本被當成安全層之一
9. 資料保護
10. 稽核記錄

補充說明 ✅：
- **零 API 金鑰架構**：透過 Pod Identity 直接存取 Bedrock，從根本消除金鑰洩露風險
- **每日 Lambda 掃描**確保成本控制，搭配 **EBS 快照提供 7 天資料保留**

> 💡 **把「成本控制」放進安全架構的 10 層裡，是這場一個很反直覺但很對的設計**。失控的 agent 燒錢跟資料外洩一樣是事故。

### ISO 27001 對照 ✅（125「ISO 27001 資安合規 — THE BITOGROUP SOLUTION」）

| 條款 | 實作 |
|---|---|
| **A.9 存取控制** | 使用者身份驗證，RBAC 最小權限 |
| **A.10 加密** | 傳輸層與靜態資料加密，金鑰集中管理 |
| **A.12 操作安全** | 完整稽核日誌，異常行為告警 |
| **A.14 系統安全** | Container Image 掃描，依賴套件 SCA |
| **A.16 事件管理** | **AI 誤用事件分類與事後 RCA 流程** |
| **A.18 合規性** | 個資保護設計，資料保留政策 |

> **A.16 那條特別值得看** —— 他們已經把「AI 誤用」當成一種正式的資安事件類型，有分類機制和 RCA 流程。多數公司連這個概念都還沒有。

### 可觀測性：Langfuse × LiteLLM × Grafana ✅（124）

```
所有模型呼叫 → LiteLLM Proxy → (async callback) → Langfuse（完整 Trace）
                                                 → Grafana（即時監控）
```

Michael 的說法 🎤：「哪一支呼叫、哪一個團隊呼叫的任何 AI agent 的事情，都是可以被追溯的。」

> **LiteLLM Proxy 是這裡的樞紐** —— 所有模型呼叫都得穿過它，這同時解決了三件事：供應商中立（不被單一 LLM 綁架）、成本歸屬（知道誰花了多少 token）、稽核（完整 trace）。一個元件吃三個需求，這是架構上很划算的一手。

### 合規壓力來自外部 🎤

Michael 提到「上禮拜美國總統發出了一個行政命令：所有企業使用的 AI agent 都必須要通過資安跟法律確認才可以使用」。

> ⚠️ 這條我沒查證，投影片也沒有。**見文末待查核**。

---

## 六、成本控管

### 四個成本策略 ✅（130「成本優化」）

| 策略 | 效果 |
|---|---|
| **KEDA 縮容至零** | **100 租戶省 80%** 成本；3 租戶省 69% |
| **Graviton ARM64（t4g）** | 省 **20%** EC2 成本 |
| **Karpenter Spot 實例** | （投影片列出，無數字）|
| **模型成本** | Bedrock 按 token 計費 |

### KEDA scale-to-zero 是關鍵 🎤

Michael 的描述：
> 「我們把這些閒置的租戶 —— 譬如說你現在沒有在用了，你沒有在用 AI agent 了 —— 我們會把它的機器歸零。在你要使用的時候，只要去 touch 它一下，它就會自動開機，就可以直接使用了。」

代價是**冷啟動要等不到 10 分鐘** 🎤。

> 🔑 **注意這個數字的意義：100 個租戶省 80%，3 個租戶只省 69%。**
> scale-to-zero 的效益**隨租戶數放大** —— 因為租戶越多，同時活躍的比例越低。這解釋了為什麼「每個團隊都有自己的 AI」在經濟上反而比「三個共用的 AI」更划算。這是整場最反直覺的一個發現。

### 成本也是安全問題 ✅

10 層縱深防禦的第 8 層就是「成本控制」，配合**每日 Lambda 掃描**。

---

## 七、成果 ✅（104「平台亮點」/ 127「成功指標 KPI 儀表板」）

| 指標 | 數字 |
|---|---|
| **首次部署時間** | **20 分鐘**（從零到上線）|
| **用戶規模** | 100+ 用戶 |
| **Uptime SLA 目標** | 99.99% |
| **Trace 覆蓋率** | **100%** |
| **稽核** | 所有 AI agent 使用過程可稽核 |

Michael 的收尾金句 🎤：

> **「AI 平台的價值不只在模型的程度，而是在安全底座能否撐起真正的日常工作。」**

以及設計哲學 🎤：

> **「多租戶設計，是讓團隊感覺不到邊界的存在。他們只要使用，不需要擔心安全性 —— 安全性由這個平台去完全把它做到。」**

---

## 八、可以直接拿的東西

### AWS 官方 Sample ✅（129）

```
https://github.com/aws-samples/sample-openclaw-multi-tenant-platform
```

這是 H.C. 跟 Michael 合作做的、BitoGroup 架構的**去識別化版本**。

> ⚠️ **H.C. 在台上講了兩次的警告** 🎤：
> 「這是 **Sample，不是套上去就可以用**。」
> 「我很推薦像 Michael 這種精神 —— 你只是**參考**這個 sample 去構建出適合你的環境，而不是完全拿這個 sample 去 apply 上去。」
>
> 他建議可以只挑其中一部分參考：Helm chart 的設計、Pod Identity 的設計、或前面 routing 的設計 —— 「並不是全部都要拿起來去使用」。

### 一個平台服務全公司 ✅（118「一個平台，全公司不同的 AI 需求」）

| SRE | 資安 | 其他部門 |
|---|---|---|
| 事件應變、日誌分析 | 稽核追蹤、告警彙整 | 產品、研發、行銷 |
| K8S 維運、CI/CD | 合規報表 | 數據、法務、業務 |
| 系統監控、成本優化 | 資安監控、安全掃描 | 客服、人資 |
| 可觀測性 | 情資整合分析 | …等各單位需求 |

---

## 九、我的觀察（不是講者說的）

1. **這場的真正主題不是 AI，是治理**。整整 37 分鐘，講模型能力的時間接近零。所有內容都在回答一個問題：「怎麼讓一個管不住的東西變得管得住」。這跟角度 ③（自有資料的治理與安全）完全對上。

2. **「站在開源上自建」是被約束逼出來的最優解，不是理想解**。BitoGroup 沒得選 SaaS（合規），沒本錢純自建（跟不上），所以走中間路線。如果你的合規壓力沒那麼大，這個結論不一定適用你 —— 但**決策的三個標準（控制權 / 去中心化 / 成本）值得照抄**。

3. **Pod Identity 消除金鑰，是這套架構裡最能單獨抽出來用的東西**。不需要多租戶、不需要 OpenClaw，任何在 EKS 上跑的東西都能用這招把「金鑰保管」問題變成「金鑰不存在」問題。

4. **LiteLLM Proxy 一個元件吃三個需求**（供應商中立 / 成本歸屬 / 稽核），投資報酬率極高。這也是最容易在小規模先做起來的一步。

5. **runtime 混用的觀念可以遷移到非 AI 場景**。「按 trust level 選隔離強度、不要無腦全開最高」對任何多租戶容器平台都成立。

6. **缺口：他們沒講失敗**。整場是成功故事，沒有講踩過什麼坑、什麼方案試了不 work、20 分鐘部署是第幾版才做到的。這是議程的通病，不是這場的問題，但吸收時要打折。

---

## ❓ 待查核

| 項目 | 狀態 |
|---|---|
| **「第二次使用只要 3 分鐘」** | ⚠️ 逐字稿有，但**掃過 MOD03 全部 50 張投影片都找不到這個數字**。可能是聽錯（如「數秒內」或「20 分鐘」）。**引用前請再確認**。 |
| **「上禮拜美國總統發行政命令，企業用 AI agent 須通過資安與法律確認」** | ⚠️ 僅講者口述，投影片無，我也未查證。要用請先查原始行政命令。 |
| **Hermes Agent 的 GitHub org 名稱** | ⚠️ star-history 圖上 repo 路徑是 `.../hermes-agent`，但 org 前綴在每張照片都被切掉或糊掉。**不要猜**。 |
| **「Nitro System / Nitro 自家 sandbox 技術」** | 🎤 逐字稿裡 H.C. 說 AWS 正基於 Nitro System 研發自家 sandbox 技術，「等功能完善一點再跟大家講」。但**沒有任何一張投影片印出「Nitro」**。屬未公開資訊，引用需謹慎。 |
| **Oasis Security 三個大數字**（999,821 / 12,573,351 / 52,048）| ⚠️ 投影片上有圖但**軸標與單位不可辨識**。只有「999,000+ Exposed OpenClaw Instances」這個說明文字是明確的。 |
| **後端 "Colam"** | ⚠️ 逐字稿聽成 Colam，投影片寫的是 **Go + chi 路由框架**。已用投影片為準。 |

---

## 🔗 來源

- **錄音**：`VOICE/05_MOD03_multitenant-eks.m4a`（39 分鐘，15:15–15:54）
- **逐字稿**：`VOICE/transcripts/05_MOD03_multitenant-eks.txt`（1,051 行）
- **投影片**：`slides/05_MOD03_multitenant-eks/`（50 張，編號 100–149）
- **AWS Sample**：https://github.com/aws-samples/sample-openclaw-multi-tenant-platform
- **OpenClaw 曝露風險參考站**：https://declawed.io/
- **OWASP 2026 Top 10 Agentic**（投影片引用）

> **這份文件的產生方式**：本地 faster-whisper 轉錄 → 逐字稿與 50 張投影片逐一交叉比對 → 凡投影片能查證的以投影片為準（whisper 把 BitoClaw 聽成 4 種不同拼法、gVisor 聽成 G-Ryzen、Kata 聽成 colorcontainer）→ 只有口述的標 🎤 → 對不上的進待查核，不猜。
