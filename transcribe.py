#!/home/tom/whisper-venv/bin/python
"""逐段自動偵測語言的課程錄音轉錄。

用法:
    /home/tom/whisper-venv/bin/python transcribe.py 2026-07-15
    (faster-whisper 不在系統 python，一定要用這個 venv)

會把 <日期>/VOICE/ 底下所有錄音轉成 <日期>/VOICE/transcripts/<檔名>.txt。
每 5 分鐘一段獨立偵測語言（講師中英夾雜時避免整檔押錯語言）。
"""
import time, os, sys, glob, subprocess, tempfile
from faster_whisper import WhisperModel

SEG = 300  # 每段 5 分鐘, 逐段自動偵測語言
ROOT = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) != 2:
    sys.exit("用法: python3 transcribe.py <日期資料夾>   例: python3 transcribe.py 2026-07-15")

DAY = sys.argv[1]
SRC = os.path.join(ROOT, DAY, "VOICE")
OUT = os.path.join(SRC, "transcripts")

if not os.path.isdir(SRC):
    sys.exit("找不到 %s — 先把錄音放進去" % SRC)
os.makedirs(OUT, exist_ok=True)

files = sorted(sum([glob.glob(os.path.join(SRC, e)) for e in ("*.aac", "*.m4a", "*.mp3", "*.wav")], []))
if not files:
    sys.exit("%s 裡沒有錄音檔 (.aac/.m4a/.mp3/.wav)" % SRC)


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


print("[%d files] loading medium model..." % len(files), flush=True)
t0 = time.time()
model = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=8)
print("[model loaded in %.1fs]" % (time.time() - t0), flush=True)

for f in files:
    name = os.path.splitext(os.path.basename(f))[0]
    outpath = os.path.join(OUT, name + ".txt")
    dur = duration(f)
    print("\n=== %s (%.1fmin) segmented transcribe ===" % (name, dur / 60), flush=True)
    tf = time.time()
    last_lang = None
    with open(outpath, "w", encoding="utf-8") as w:
        w.write("# %s | segmented auto-language transcription\n" % name)
        offset = 0.0
        while offset < dur:
            seglen = min(SEG, dur - offset)
            tmp = tempfile.mktemp(suffix=".wav")
            subprocess.run(["ffmpeg", "-y", "-ss", str(offset), "-i", f, "-t", str(seglen),
                            "-ar", "16000", "-ac", "1", tmp], capture_output=True)
            if not os.path.exists(tmp):
                offset += SEG
                continue
            segs, info = model.transcribe(tmp, language=None, beam_size=5, vad_filter=True)
            if info.language != last_lang:
                w.write("\n### [%02d:%02d~] language: %s (p=%.2f) ###\n" % (
                    int(offset // 60), int(offset % 60), info.language, info.language_probability))
                w.flush()
                last_lang = info.language
            for s in segs:
                tt = s.start + offset
                w.write("[%02d:%02d] %s\n" % (int(tt // 60), int(tt % 60), s.text.strip()))
                w.flush()
            os.remove(tmp)
            print("  [%02d:%02d] lang=%s" % (int(offset // 60), int(offset % 60), info.language), flush=True)
            offset += SEG
    took = time.time() - tf
    print("[DONE %s: took %.1fmin, %.2fx rt] -> %s" % (name, took / 60, dur / took, outpath), flush=True)

print("\n[ALL DONE in %.1fmin]" % ((time.time() - t0) / 60), flush=True)
