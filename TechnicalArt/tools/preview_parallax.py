# 视差预览：在几个镜头位置合成五层，叠上妮芙（2.1u）与灰盒物件轮廓，检查比例与分层
import sys, os, json
from PIL import Image, ImageDraw, ImageFont
ROOT, SCENE = sys.argv[1], sys.argv[2]
D = os.path.join(ROOT, "TechArtAsset/Scenes", SCENE, "_work")
GROUND = int(sys.argv[3]); OUTN = sys.argv[4]
P = {"L0_Sky": 0.05, "L1_Far": 0.2, "L2_Mid": 0.5, "L3_Walk": 1.0, "L4_Fore": 1.3}
L = {k: Image.open(os.path.join(D, f"{SCENE}_{k}_wip.png")).convert("RGBA") for k in P}
lay = json.load(open(os.path.join(ROOT, "TechArtAsset/Scenes", SCENE, f"{SCENE}_layout_v1.json"), encoding="utf-8"))
NI = Image.open(os.path.join(ROOT, "TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png")).convert("RGBA")
ni = NI.resize((int(NI.width * 210 / NI.height), 210), Image.LANCZOS)
f = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 22, index=2)
TOP = GROUND + 270 - 1080
L_px = int(lay["length"] * 100)
cams = [0, (L_px - 1920) // 2, L_px - 1920]
frames = []
for c in cams:
    fr = Image.new("RGBA", (1920, 1080), (0, 0, 0, 255))
    for k, p in P.items():
        fr.alpha_composite(L[k], (-int(c * p), -TOP)) if False else fr.alpha_composite(L[k].crop((int(c * p), TOP, int(c * p) + 1920, TOP + 1080)))
        if k == "L3_Walk":
            d = ImageDraw.Draw(fr)
            for b in lay.get("blocks", []):
                x0 = b["x"] * 100 - c; x1 = (b["x"] + b["w"]) * 100 - c
                yb = 810 - b["base"] * 100; yt = 810 - (b["base"] + b["h"]) * 100
                d.rectangle([x0, yt, x1, yb], outline=(255, 60, 40, 255), width=3)
            for it in lay["interact"]:
                x = it["x"] * 100 - c
                if -50 < x < 1970: d.ellipse([x - 9, 801 - it["y"] * 100, x + 9, 819 - it["y"] * 100], fill=(255, 60, 40, 255))
            nx = 600 if c else 350
            fr.alpha_composite(ni, (nx - ni.width // 2, 810 - ni.height))
    d = ImageDraw.Draw(fr); d.line([(0, 810), (1920, 810)], fill=(255, 255, 255, 120), width=1)
    d.text((16, 12), f"{SCENE}  镜头 x = {c/100:.1f}u", fill=(255, 255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
    frames.append(fr)
sheet = Image.new("RGB", (1920, 1080 * 3 + 20), (20, 20, 20))
for i, fr in enumerate(frames): sheet.paste(fr.convert("RGB"), (0, i * 1090))
sheet.save(os.path.join(D, OUTN), quality=88)
# 动态预览（GIF，缩小）
g = []
for c in range(0, L_px - 1920 + 1, 60):
    fr = Image.new("RGBA", (1920, 1080), (0, 0, 0, 255))
    for k, p in P.items(): fr.alpha_composite(L[k].crop((int(c * p), TOP, int(c * p) + 1920, TOP + 1080)))
    fr.alpha_composite(ni, (900 - ni.width // 2, 810 - ni.height))
    g.append(fr.convert("RGB").resize((640, 360), Image.LANCZOS))
g[0].save(os.path.join(D, OUTN.replace(".jpg", ".gif")), save_all=True, append_images=g[1:] + g[::-1], duration=50, loop=0)
print("ok", len(g))
