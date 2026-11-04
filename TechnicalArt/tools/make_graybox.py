# 读取 ch1_layout_v1.json，为每个场景生成灰盒布局图（PNG）与单场景布局数据（JSON，给 Unity / Codex 灰盒用）
import sys, json, os
from PIL import Image, ImageDraw, ImageFont
ROOT = sys.argv[1]
DATA = json.load(open(os.path.join(ROOT, "TechnicalArt/tools/ch1_layout_v1.json"), encoding="utf-8"))
NI = Image.open(os.path.join(ROOT, "TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png")).convert("RGBA")
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
f = ImageFont.truetype(FONT, 15, index=2); fsm = ImageFont.truetype(FONT, 12, index=2); fb = ImageFont.truetype(FONT, 20, index=2)
S = 30                     # 1u = 30px（布局图缩放）
YMIN, YMAX = -3.2, 8.4     # 竖向显示范围（u）
PAD = 40

def build(sc):
    L = sc["length"]; W = max(int(L*S) + PAD*2, 1000)
    stripH = int((YMAX-YMIN)*S)
    items = sc["interact"]
    legendH = 26 + 22*((len(items)+1)//2) + 60
    H = 60 + stripH + legendH
    img = Image.new("RGB", (W, H), (246, 242, 233)); d = ImageDraw.Draw(img)
    X = lambda u: PAD + int(u*S)
    Y = lambda u: 60 + int((YMAX-u)*S)
    d.rectangle([X(0), Y(YMAX), X(L), Y(YMIN)], fill=(214, 220, 228))
    # 单位网格
    for i in range(int(L)+1):
        col = (198, 205, 214) if i % 5 else (175, 184, 196)
        d.line([(X(i), Y(YMAX)), (X(i), Y(YMIN))], fill=col)
        if i % 5 == 0: d.text((X(i)+2, Y(YMIN)+2), f"{i}", fill=(90, 90, 90), font=fsm)
    for j in range(int(YMIN), int(YMAX)+1):
        d.line([(X(0), Y(j)), (X(L), Y(j))], fill=(205, 211, 220))
    # 天花板
    if sc.get("ceiling"):
        d.rectangle([X(0), Y(YMAX), X(L), Y(sc["ceiling"])], fill=(120, 110, 100))
        d.text((X(L)-90, Y(sc["ceiling"])-18), f"天花板 {sc['ceiling']}u", fill=(240, 235, 225), font=fsm)
    # 远景 / 中景注释条
    for k, (key, col, yy) in enumerate([("far", (150, 160, 185), 8.2), ("mid", (160, 145, 120), 7.6)]):
        for b in sc.get(key, []):
            d.rectangle([X(b["x"]), Y(yy), X(b["x"]+b["w"]), Y(yy-0.35)], fill=col)
            d.text((X(b["x"])+3, Y(yy)-1), ("远景 " if key=="far" else "中景 ")+b["label"], fill=(255, 255, 255), font=fsm)
    # 坑
    for p in sc.get("pits", []):
        d.rectangle([X(p["x"]), Y(p["floor"]), X(p["x"]+p["w"]), Y(YMIN)], fill=(92, 84, 78))
        d.text((X(p["x"])+2, Y(p["floor"])+3), p["label"], fill=(250, 240, 220), font=fsm)
    # 地面折线 → 多边形
    for seg in sc["ground"]:
        pts = [(X(a), Y(b)) for a, b in seg]
        poly = pts + [(pts[-1][0], Y(YMIN)), (pts[0][0], Y(YMIN))]
        d.polygon(poly, fill=(112, 128, 92)); d.line(pts, fill=(48, 60, 38), width=3)
    # 方块 / 墙 / 门
    for b in sc.get("blocks", []):
        kind = b.get("kind", "block")
        fill = {"thorn": (96, 44, 52), "door": (70, 120, 112), "stone": (150, 150, 160)}.get(kind, (150, 140, 120))
        d.rectangle([X(b["x"]), Y(b["base"]+b["h"]), X(b["x"]+b["w"]), Y(b["base"])], fill=fill, outline=(50, 45, 40), width=2)
        d.text((X(b["x"]), Y(b["base"]+b["h"])-17), b["label"], fill=(40, 35, 30), font=fsm)
    # 浮石（幻象）
    for p in sc.get("platforms", []):
        box = [X(p["x"]), Y(p["top"]), X(p["x"]+p["w"]), Y(p["top"]-0.35)]
        if p.get("illusion"):
            for t in range(0, box[2]-box[0], 6): d.line([(box[0]+t, box[1]), (box[0]+t+3, box[1])], fill=(40, 150, 140), width=3)
            d.rectangle(box, outline=(40, 150, 140))
        else: d.rectangle(box, fill=(130, 120, 100))
    if sc.get("platforms"): d.text((X(sc["platforms"][0]["x"]), Y(1.9)), "幻象浮石（冷光显形）", fill=(20, 110, 100), font=fsm)
    # 收集物
    for x, y in sc.get("lights", []):
        cx, cy = X(x), Y(y); d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=(110, 190, 90), outline=(40, 90, 30))
    for x, y in sc.get("ogham", []):
        cx, cy = X(x), Y(y); d.polygon([(cx, cy-8), (cx+6, cy), (cx, cy+8), (cx-6, cy)], fill=(225, 205, 140), outline=(90, 70, 30))
    for x in sc.get("torches", []):
        cx, cy = X(x), Y(2.6); d.polygon([(cx, cy-10), (cx+5, cy), (cx-5, cy)], fill=(60, 210, 190)); d.line([(cx, cy), (cx, cy+12)], fill=(80, 60, 40), width=3)
    # 互动点（编号）
    for i, it in enumerate(items, 1):
        cx, cy = X(it["x"]), Y(it["y"]+1.0)
        d.ellipse([cx-10, cy-10, cx+10, cy+10], fill=(176, 72, 52)); d.text((cx-4 if i < 10 else cx-8, cy-10), str(i), fill="white", font=f)
        d.line([(cx, cy+10), (cx, Y(it["y"]))], fill=(176, 72, 52), width=2)
    # 屏幕框（19.2×10.8u；地面时脚在屏底上方 2.7u）
    x = 0.0
    while x < L - 0.01:
        x2 = min(x+19.2, L)
        d.rectangle([X(x)+2, Y(8.1), X(x2)-2, Y(-2.7)], outline=(60, 80, 160), width=2)
        x += 19.2
    d.text((X(0)+4, Y(-2.7)-18), "屏幕框 19.2×10.8u", fill=(60, 80, 160), font=fsm)
    # 妮芙比例
    first = sc["ground"][0][0]
    th = int(2.1*S); tw = int(NI.width*th/NI.height); ni = NI.resize((tw, th), Image.LANCZOS)
    sx = items[0]["x"] if items[0]["type"] in ("start",) else 2.0
    img.paste(ni, (X(sx)-tw//2, Y(first[1])-th), ni)
    # 标题与图例
    d.text((PAD, 14), f"{sc['name']}  ·  长 {L}u（{int(L*100)} px @1080p）  ·  主色 {sc['palette']}  ·  灰盒 v1", fill=(40, 35, 30), font=fb)
    ly = 60 + stripH + 14
    d.text((PAD, ly), "互动点：", fill=(40, 35, 30), font=f)
    for i, it in enumerate(items, 1):
        col = (i-1) % 2; row = (i-1)//2
        d.text((PAD + 70 + col*min(560, (W-PAD*2)//2), ly + row*22), f"{i}. {it['label']}", fill=(60, 50, 40), font=f)
    ly2 = ly + 22*((len(items)+1)//2) + 10
    d.text((PAD, ly2), "● 三叶草光点   ◆ 欧甘石牌   ▲ 青绿妖火火把   虚线 = 幻象浮石   竖线每 1u，粗线每 5u   妮芙 = 2.1u", fill=(80, 70, 60), font=fsm)
    return img

for sc in DATA["scenes"]:
    out = os.path.join(ROOT, "TechArtAsset/Scenes", sc["id"]); os.makedirs(out, exist_ok=True)
    pth = os.path.join(out, f"{sc['id']}_graybox_v1.png")
    if os.path.exists(pth) and "--force" not in sys.argv: print("skip existing", pth); continue
    build(sc).save(pth)
    json.dump(sc, open(os.path.join(out, f"{sc['id']}_layout_v1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", pth)
