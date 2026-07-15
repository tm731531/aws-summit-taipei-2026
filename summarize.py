#!/usr/bin/env python3
"""用 Cerebras GPT-OSS-120B 把逐字稿(.txt) map-reduce 成結構化大綱(.summary.md)。

用法:
    source ~/.config/llm/keys.env
    ./summarize.py 2026-07-15

會處理 <日期>/VOICE/transcripts/*.txt → 同目錄的 *.summary.md。
斷點續傳:已存在的 .summary.md 跳過。免費層有速率限制,故 request 間 sleep + 重試。
"""
import os, sys, glob, json, time, urllib.request, urllib.error

API = "https://api.cerebras.ai/v1/chat/completions"
MODEL = "gpt-oss-120b"
ROOT = os.path.dirname(os.path.abspath(__file__))

KEY = os.environ.get("CEREBRAS_API_KEY")
if not KEY:
    sys.exit("ERR: 先 source ~/.config/llm/keys.env")

if len(sys.argv) != 2:
    sys.exit("用法: ./summarize.py <日期資料夾>   例: ./summarize.py 2026-07-15")

DAY = sys.argv[1]
TDIR = os.path.join(ROOT, DAY, "VOICE", "transcripts")
if not os.path.isdir(TDIR):
    sys.exit("找不到 %s — 先跑 ./transcribe.py %s" % (TDIR, DAY))

CHUNK_CHARS = 9000   # 每塊約 9000 字,安全落在 context 內
SLEEP = 2            # request 間隔(秒),避開速率限制


def call(messages, max_tokens=2000, retries=5):
    body = json.dumps({"model": MODEL, "max_tokens": max_tokens,
                       "temperature": 0.2, "messages": messages}).encode()
    for attempt in range(retries):
        try:
            req = urllib.request.Request(API, data=body, headers={
                "Authorization": f"Bearer {KEY}",
                "Content-Type": "application/json",
                "User-Agent": "curl/8.5.0"})  # 避開 Cloudflare 對 urllib UA 的封鎖(error 1010)
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            return d["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            wait = 5 * (attempt + 1)
            print(f"    HTTP {e.code}, {wait}s 後重試 ({attempt+1}/{retries})", flush=True)
            time.sleep(wait)
        except Exception as e:
            print(f"    err {e}, 5s 後重試", flush=True)
            time.sleep(5)
    raise RuntimeError("Cerebras 重試耗盡")


def chunk_text(text, size):
    lines, chunks, cur, n = text.splitlines(), [], [], 0
    for ln in lines:
        cur.append(ln); n += len(ln)
        if n >= size:
            chunks.append("\n".join(cur)); cur, n = [], 0
    if cur:
        chunks.append("\n".join(cur))
    return chunks


MAP_SYS = ("你是 AWS Summit Taipei 2026 議程的技術助理。以下是一段議程錄音的逐字稿片段(含時間戳)，"
           "主題涵蓋企業 AI 落地：AI 開發流程(Kiro、spec-driven、prompt/context/harness)、"
           "平台架構(EKS、multi-tenant AI platform)、AI agent、治理與安全。"
           "請用繁體中文，忠實條列這段講了哪些重點，保留所有具體事實("
           "AWS 服務名稱、架構元件、數字、版本、指令、設定、講者舉的客戶案例與踩坑經驗)。"
           "特別注意:講者常中英夾雜，AWS 服務名/技術名詞一律保留英文原文不要翻譯。"
           "只做摘要不要杜撰，逐字稿有錯字請依上下文合理修正(例如 whisper 常把 EKS 聽成「一 K S」)。"
           "輸出純條列，不要開場白。")

REDUCE_SYS = ("你是 AWS Summit Taipei 2026 議程的技術助理。以下是同一場議程各片段的重點條列，"
              "請合併、去重、依講者的論述邏輯重新組織成一份結構化的繁體中文大綱(用 Markdown 標題與條列)，"
              "保留所有具體事實、AWS 服務名稱(英文原文)、架構決策與客戶案例。"
              "標出這場議程的主題與講者的核心主張。不要杜撰，不要加開場白。")

files = sorted(glob.glob(os.path.join(TDIR, "*.txt")))
if not files:
    sys.exit("%s 裡沒有逐字稿 — 先跑 ./transcribe.py %s" % (TDIR, DAY))

print(f"[{len(files)} 逐字稿待摘要]", flush=True)
for i, f in enumerate(files, 1):
    base = os.path.splitext(os.path.basename(f))[0]
    out = os.path.join(TDIR, base + ".summary.md")
    if os.path.exists(out):
        print(f"[{i}/{len(files)}] {base} 已摘要,跳過", flush=True)
        continue
    text = open(f, encoding="utf-8").read()
    chunks = chunk_text(text, CHUNK_CHARS)
    print(f"[{i}/{len(files)}] {base}: {len(text)}字 → {len(chunks)}塊", flush=True)
    partials = []
    for j, ch in enumerate(chunks, 1):
        print(f"    map {j}/{len(chunks)}", flush=True)
        partials.append(call([{"role": "system", "content": MAP_SYS},
                              {"role": "user", "content": ch}], max_tokens=1800))
        time.sleep(SLEEP)
    if len(partials) == 1:
        merged = partials[0]
    else:
        print(f"    reduce", flush=True)
        merged = call([{"role": "system", "content": REDUCE_SYS},
                       {"role": "user", "content": "\n\n---片段---\n".join(partials)}],
                      max_tokens=3000)
    tmp = out + ".partial"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(f"# 摘要：{base}\n\n> Cerebras gpt-oss-120b 自動摘要，待人工查核\n\n" + merged + "\n")
    os.replace(tmp, out)
    print(f"[{i}/{len(files)}] {base} 完成 → {os.path.basename(out)}", flush=True)
print("[全部摘要完成]", flush=True)
