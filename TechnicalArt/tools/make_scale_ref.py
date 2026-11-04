# 生成第一章比例参照图：妮芙 v3 侧面 + 跳跃弧线 + 关卡尺度规则（1920x1080，1 单位 = 100 px）
import sys, math
from PIL import Image, ImageDraw, ImageFont
ROOT = sys.argv[1]
OUT = sys.argv[2]
CJK = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
try: f = ImageFont.truetype(CJK, 22); fs = ImageFont.truetype(CJK, 17); fb = ImageFont.truetype(CJK, 30)
except: f = fs = fb = ImageFont.load_default()

U = 100; W, H = 1920, 1080; GROUND = 810  # 地面线：屏幕底部往上 2.7 单位（25%）
# ---- 参数（与 SCENE_SCALE_SPEC.md 一致）----
NH = 2.1; WALK = 3.2; RUN = 5.6; APEX = 2.4; T_UP = 0.40; FALL_MULT = 1.5
g = 2*APEX/T_UP**2; v0 = g*T_UP; gd = g*FALL_MULT; t_dn = math.sqrt(2*APEX/gd)

def X(u): return int(u*U)
def Y(u): return int(GROUND - u*U)

img = Image.new("RGB", (W, H), (236, 230, 216)); d = ImageDraw.Draw(img)
for i in range(0, 20):
    d.line([(X(i), 0), (X(i), H)], fill=(222, 214, 198))
for j in range(-3, 9):
    d.line([(0, Y(j)), (W, Y(j))], fill=(222, 214, 198))
d.rectangle([0, GROUND, W, H], fill=(120, 132, 96))
d.line([(0, GROUND), (W, GROUND)], fill=(60, 70, 50), width=3)
for j in range(0, 8): d.text((4, Y(j)-22), f"{j}u", fill=(120, 110, 95), font=fs)

# ---- 妮芙侧面（turnaround 第 2 个人物；最小接缝分开第 1 个人物 + 连通域 + 只清除纯底色的封闭空洞）----
import numpy as np
from scipy import ndimage
from PIL import ImageFilter
src = Image.open(ROOT + "/MJ_ref/Niamh_v3_turnaround.png").convert("RGB")
c = np.array(src).astype(int); BG = np.array([239, 228, 215])
ink = np.abs(c - BG).sum(2) >= 40; Hh = ink.shape[0]
x0, x1 = 420, 600; M = ink[:, x0:x1].astype(float) + 0.001; back = np.zeros(M.shape, int)
for y in range(1, Hh):
    prev = M[y-1]; st = np.vstack([np.r_[np.inf, prev[:-1]], prev, np.r_[prev[1:], np.inf]])
    back[y] = st.argmin(0) - 1; M[y] += st.min(0)
seam = np.zeros(Hh, int); seam[-1] = M[-1].argmin()
for y in range(Hh-1, 0, -1): seam[y-1] = seam[y] + back[y, seam[y]]
seam += x0
keepm = np.zeros_like(ink)
for y in range(Hh): keepm[y, seam[y]:815] = True
# v2：只把「与画布边缘连通、且几乎等于底色」的像素当背景（阈值 14）。
# v1 把与底色接近的封闭区域也清掉了，结果手和小腿的肤色被抠掉。
near = np.abs(ndimage.uniform_filter(c.astype(float), size=(3, 3, 1)) - BG).sum(2) < 14
cand = near & keepm
for y in range(Hh): cand[y, :seam[y]] = True; cand[y, 815:] = True
lab, n = ndimage.label(cand)
border = set(np.unique(np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]])) - {0}
bgmask = np.isin(lab, list(border))
filled = ~bgmask & keepm
filled[:, 815:] = False
filled = ndimage.binary_opening(filled, iterations=1)
lab, n = ndimage.label(filled); sz = ndimage.sum(filled, lab, range(1, n+1)); filled = lab == (sz.argmax()+1)
ys, xs = np.where(filled)
alpha = Image.fromarray((filled*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
rgba = src.convert("RGBA"); rgba.putalpha(alpha)
crop = rgba.crop((xs.min(), ys.min(), xs.max()+1, ys.max()+1))
crop.save(OUT.replace(".png", "_niamh_fullres.png"))
th = int(NH*U); tw = int(crop.width*th/crop.height)
ni = crop.resize((tw, th), Image.LANCZOS)
ni.save(OUT.replace(".png", "_niamh210.png"))
def put(xu): img.paste(ni, (X(xu)-tw//2, GROUND-th), ni)

put(1.6)
d.line([(X(0.6), Y(NH)), (X(2.6), Y(NH))], fill=(160, 60, 40), width=2)
d.text((X(0.2), Y(NH)-34), "妮芙 2.1u = 210px（屏高约 1/5）", fill=(140, 50, 30), font=fs)

# ---- 跳跃弧线：走跳 / 跑跳 ----
def arc(x0, vx, col, label, row=0):
    pts = []; t = 0.0
    while True:
        if t <= T_UP: y = v0*t - 0.5*g*t*t
        else: tt = t-T_UP; y = APEX - 0.5*gd*tt*tt
        if y < 0 and t > T_UP: break
        pts.append((X(x0+vx*t), Y(y))); t += 0.01
    for a, b in zip(pts[::2], pts[1::2]): d.line([a, b], fill=col, width=4)
    xend = x0 + vx*(T_UP+t_dn)
    d.text((X(x0)+10, Y(-0.45-0.4*row)), f"{label}：水平 {vx*(T_UP+t_dn):.1f}u，最高 {APEX}u", fill=col, font=fs)
    return xend
arc(3.0, WALK, (40, 90, 160), "走跳")
arc(3.0, RUN, (170, 90, 20), "跑跳", 1)
d.line([(X(2.8), Y(APEX)), (X(7.4), Y(APEX))], fill=(90, 90, 90), width=1)
d.text((X(7.5), Y(APEX)-14), f"最高 {APEX}u（长按）；轻点约 0.9u", fill=(70, 70, 70), font=fs)

# ---- 关卡尺度示例 ----
# 石墙 1.2u
d.rectangle([X(8.0), Y(1.2), X(9.0), GROUND], fill=(150, 145, 130), outline=(80, 75, 65), width=2)
d.text((X(7.75), Y(1.2)-30), "低墙 ≤1.6u（例 1.2）", fill=(60, 55, 45), font=fs)
# 台阶 2.0u
d.rectangle([X(10.0), Y(2.0), X(11.6), GROUND], fill=(130, 125, 110), outline=(80, 75, 65), width=2)
d.text((X(9.9), Y(2.0)-30), "最高台阶 2.0u", fill=(60, 55, 45), font=fs)
# 缺口 1.6 / 3.0
def gap(x0, w, lab):
    d.rectangle([X(x0), GROUND, X(x0+w), H], fill=(40, 36, 44))
    d.text((X(x0)+4, GROUND+12), lab, fill=(240, 230, 210), font=fs)
gap(12.4, 1.6, "走跳缺口 ≤1.6u")
gap(15.0, 3.0, "跑跳缺口 ≤3.0u")
# 门洞 3.2u
d.rectangle([X(18.2), Y(3.2), X(19.4), GROUND], outline=(40, 110, 100), width=3)
d.text((X(17.25), Y(3.2)-30), "门 / 通道 ≥3.2u", fill=(30, 90, 80), font=fs)
put(18.8)

d.text((24, 18), "The Fairy Hills · 第一章比例参照 v1（1920×1080，PPU 100，1u = 100px，镜头高 10.8u）", fill=(50, 40, 30), font=f)
d.text((24, 52), f"走 {WALK} u/s · 跑 {RUN} u/s · 上升 {T_UP}s · 下落重力 ×{FALL_MULT} · 滞空 {T_UP+t_dn:.2f}s · 地面线距屏底 2.7u", fill=(80, 70, 60), font=fs)
img.save(OUT)
print("g", round(g,2), "v0", round(v0,2), "gd", round(gd,2), "air", round(T_UP+t_dn,3), "walkdist", round(WALK*(T_UP+t_dn),2), "rundist", round(RUN*(T_UP+t_dn),2))
