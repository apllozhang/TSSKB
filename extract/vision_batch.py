# -*- coding: utf-8 -*-
"""GLM-4.6V 批量图片识别：extract/<slug>/pXXX_hash.png -> extract/<slug>_figures.json"""
import os, json, base64, time, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

KEY = "d55308fc85e14fc885748e323d587daa.sng9dusFvj3Apwyz"
URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
PROMPT = (
    "这是网络技术培训教材中的一张插图。用中文回答，格式："
    "[类型:架构图|拓扑图|流程图|数据表格|产品照片|配置截图|对比图|其他] "
    "50字以内描述核心信息（设备名/连接关系/数据要点）。没有实质信息就写[类型:装饰图] 无。"
)
SLUG = sys.argv[1]
MAXWORK = int(sys.argv[2]) if len(sys.argv) > 2 else 6

manifest = json.load(open(f"extract/{SLUG}_manifest.json", encoding="utf-8"))
outdir = f"extract/{SLUG}"
outfile = f"extract/{SLUG}_figures.json"
results = {}
if os.path.exists(outfile):
    results = json.load(open(outfile, encoding="utf-8"))

def call(item):
    fname = item["file"]
    if fname in results:
        return fname, results[fname], True
    for attempt in range(3):
        try:
            b64 = base64.b64encode(open(os.path.join(outdir, fname), "rb").read()).decode()
            r = requests.post(URL, headers={"Authorization": f"Bearer {KEY}"}, timeout=120, json={
                "model": "glm-4v-flash",
                "messages": [{"role": "user", "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                    {"type": "text", "text": PROMPT}]}],
                "temperature": 0.1, "max_tokens": 200,
            })
            r.raise_for_status()
            txt = r.json()["choices"][0]["message"]["content"].strip()
            return fname, txt, True
        except Exception as e:
            if attempt == 2:
                return fname, f"[识别失败: {type(e).__name__}]", False
            time.sleep(3 * (attempt + 1))

done = fail = 0
with ThreadPoolExecutor(MAXWORK) as ex:
    futs = [ex.submit(call, it) for it in manifest]
    for fu in as_completed(futs):
        fname, txt, ok = fu.result()
        results[fname] = txt
        done += 1
        fail += (not ok)
        if done % 25 == 0:
            json.dump(results, open(outfile, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"{SLUG}: {done}/{len(manifest)} done, fail={fail}", flush=True)
json.dump(results, open(outfile, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{SLUG} FINISHED: {len(results)}/{len(manifest)}, fail={fail}")
