# 检查第一章布局是否符合 SCENE_SCALE_SPEC 的尺度规则（缺口、台阶、浮石间距、顶部净空）
import json, sys
R = {"walk_gap": 1.6, "run_gap": 3.0, "max_step": 2.0, "low_wall": 1.6, "headroom": 2.6}  # headroom：站在最高台阶上，头顶到天花板至少留出的高度（角色 2.1u + 0.5u）
D = json.load(open(sys.argv[1], encoding="utf-8"))
ok = True
def warn(m):
    global ok; ok = False; print("  !!", m)
for sc in D["scenes"]:
    print(sc["id"])
    for p in sc.get("pits", []):
        kind = "走跳" if p["w"] <= R["walk_gap"] else ("跑跳" if p["w"] <= R["run_gap"] else "过宽")
        print(f"  坑 x={p['x']} 宽 {p['w']}u → {kind}；坑底 {p['floor']}u（爬出高 {-p['floor']}u）")
        if kind == "过宽" and not sc.get("platforms"): warn("缺口超过跑跳上限且没有浮石")
        if -p["floor"] > R["max_step"]: warn("坑太深，爬不出来")
    for b in sc.get("blocks", []):
        if b.get("kind") in ("door", "thorn"): continue
        h = b["h"]; tag = "直接跳" if h <= R["low_wall"] else ("满跳" if h <= R["max_step"] else "需垫脚")
        print(f"  {b['label']}：{h}u → {tag}")
        if h > R["max_step"]:
            steps = [o for o in sc["blocks"] if o is not b and o["x"]+o["w"] <= b["x"] and b["x"]-(o["x"]+o["w"]) < 1.0]
            if not steps or h - max(s["h"] for s in steps) > R["max_step"]: warn(f"{b['label']} 太高")
    plats = sorted(sc.get("platforms", []), key=lambda q: q["x"])
    if plats:
        edges = []
        for p in sc["pits"]:
            pts = [(p["x"], 0.0)] + [((q["x"], q["top"]), (q["x"]+q["w"], q["top"])) for q in plats] + [(p["x"]+p["w"], 0.0)]
            seq = [pts[0]] + [e for pair in pts[1:-1] for e in pair] + [pts[-1]]
            for i in range(0, len(seq)-1, 2):
                g = seq[i+1][0]-seq[i][0]; dh = seq[i+1][1]-seq[i][1]
                print(f"  浮石段 {seq[i][0]:.1f}→{seq[i+1][0]:.1f}：水平 {g:.1f}u，高差 {dh:+.1f}u")
                if g > R["walk_gap"]: warn("浮石间距超过走跳上限")
    if sc.get("ceiling") and sc["ceiling"] + 1e-6 < R["max_step"] + R["headroom"]: warn("天花板过低（站上最高台阶后头顶净空不足 2.6u）")
print("全部通过" if ok else "有问题，见上")
