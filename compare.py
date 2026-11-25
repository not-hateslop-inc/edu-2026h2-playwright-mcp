import json
from pathlib import Path

ref = Path("results/answer.json") if Path("results/answer.json").exists() else Path("results/a_bs4.json")
print("기준:", ref)
answer = {r["title"]: r for r in json.loads(ref.read_text(encoding="utf-8"))}
for name in ["a_bs4", "b_playwright", "c_mcp"]:
    p = Path(f"results/{name}.json")
    if not p.exists():
        print(f"{name:<14} 결과 없음"); continue
    rows = json.loads(p.read_text(encoding="utf-8"))
    ok = sum(1 for r in rows if r.get("title") in answer and int(r.get("stock", -1)) == answer[r["title"]]["stock"])
    print(f"{name:<14} {ok}/{len(answer)} 정확, 행 수 {len(rows)}")
