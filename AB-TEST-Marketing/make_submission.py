"""학습용 노트북에서 📒 학습 노트 셀과 설치 셀을 걷어 내 제출용 노트북을 만든다.
사용법 (프로젝트 폴더에서):  python make_submission.py
"""
import glob, json

DST = "ab_test_marketing.ipynb"
candidates = [f for f in glob.glob("*learning*.ipynb")]
assert candidates, "이름에 'learning'이 들어간 학습용 노트북을 찾지 못했어요."
SRC = candidates[0]

nb = json.load(open(SRC, encoding="utf-8"))
keep, removed = [], 0
for cell in nb["cells"]:
    text = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
    head = text.lstrip()[:80]
    if "📒" in head or head.startswith(("%pip", "!pip")):
        removed += 1
        continue
    keep.append(cell)

nb["cells"] = keep
json.dump(nb, open(DST, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{SRC} → {DST}: 셀 {removed}개 제거, {len(keep)}개 유지")
