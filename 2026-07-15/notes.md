# 2026-07-15（三）AWS Summit Taipei 2026 — Day 1

> 狀態：📝 待整理 — 錄音轉錄後回填
> 場地：TICC 台北國際會議中心

議程來源：[我的推薦文](https://blog.tomting.com/2026/07/10/aws-summit-taipei-2026-enterprise-ai-sessions/) — 三個切入角度：**(1) 讓團隊用起來 (2) 基建擴展與地端支援 (3) 自有資料的治理與安全**

---

## 重點摘要

<!-- 一天結束後回填：3-5 條最值得記住的 -->

---

## 10:00–11:00 Keynote  ｜ 📍 3F 大會堂

**角度**：開場總覽

<!-- 現場記 -->

---

## 11:30–12:15 MOD01: AI-Driven Development Lifecycle  ｜ 📍 Room 201DEF

**角度**：讓團隊用起來

<!-- 現場記 -->

---

## 13:30–14:15 KIRO02: AI Engineering with Prompt/Context/Harness  ｜ 📍 Room 201ABC

**角度**：團隊工程實踐

<!-- 現場記 -->

---

## 14:30–15:00 KIRO05: From Vibe Coding to Spec-Driven Approach  ｜ 📍 Room 201ABC

**角度**：標準化 AI 開發

<!-- 現場記 -->

---

## 15:15–16:00 MOD03: Multi-Tenant AI Platform on EKS（BitoGroup 案例）  ｜ 📍 Room 201DEF

**角度**：② 平台架構 ＋ ③ 治理與安全

> ⭐ **這場另有獨立深度分析**：[MOD03-深度分析-多租戶AI平台.md](MOD03-深度分析-多租戶AI平台.md)
> 涵蓋架構、四層租戶隔離、runtime 比較表（runc/gVisor/Kata 含精確數字）、10 層縱深防禦、ISO 27001 對照、成本控管四策略、以及可直接取用的 AWS sample。

**三句話版本**：BitoGroup（金管會監管的交易所，資料不能外流）不能用 AI SaaS、又追不上純自建的速度，最後站在開源 **OpenClaw** 上、用公司既有的 **Amazon EKS** 蓋了多租戶 AI Agent 平台 **BitoClaw**。設計哲學是「多租戶設計是讓團隊感覺不到邊界的存在」。**KEDA 把閒置租戶縮容到零，100 租戶省 80% 成本** —— 這是「每個團隊都有自己的 AI」在經濟上可行的關鍵。

**最值得帶走的**：
- 「選擇 Amazon EKS，不是追逐潮流，而是把團隊已經會的技能，變成平台的競爭力。」
- 隔離**不要一次拉到最高** —— 按 trust level 混用 runc / gVisor / Kata
- **Pod Identity 零金鑰架構** —— 把「金鑰保管」變成「金鑰不存在」
- **LiteLLM Proxy 一個元件吃三個需求**：供應商中立 + 成本歸屬 + 稽核

---

## 🚫 未參加：MOD04（16:15–17:00 ｜ 📍 Room 201DEF）

**AI 時代的 Kubernetes 平台：用 EKS Auto Mode 消除維運負擔**

臨時有事沒去，無錄音。

> 角度 ②（規模化維運）這塊由 MOD03 部分覆蓋 —— MOD03 的多租戶 AI 平台本身就跑在 EKS 上。缺的是 EKS Auto Mode 這個具體的維運免除機制。會後可看 AWS 有無放簡報/錄影。

---

## 指令 / 設定速查

```bash
# 議程上出現的 aws cli 指令、console 操作路徑
```

---

## ❓ 待查核

<!-- 錄音聽不清、講者講法與官方文件有出入的，事後查 AWS docs -->

---

## 🔗 參考來源

<!-- 查核用的 AWS 官方文件連結 -->
