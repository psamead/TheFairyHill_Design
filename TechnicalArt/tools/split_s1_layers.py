# S1 自动粗拆五层（WIP）：颜色 + GrabCut 分层，遮挡处用 inpaint / 拉伸补，按 1.5 倍放大到游戏尺度并裁出各层所需宽度。
# 结果只用于试视差和定比例；最终边缘与补画在 PS 里修。
import sys, os, numpy as np, cv2
from PIL import Image
ROOT = sys.argv[1]
SRC = os.path.join(ROOT, "MJ_ref/S1_VILLAGE_KEY_03_pan.png")
OUT = os.path.join(ROOT, "TechArtAsset/Scenes/S1_Village/_work")
os.makedirs(OUT, exist_ok=True)
S = 1.0            # v2：不放大。1.5 倍时天空和村舍顶被镜头裁掉；原尺度下整幅构图正好放进镜头，村舍作为田野后方的中景
GROUND = 1000      # 原图中路面（妮芙脚底）所在行
LEVEL = 3840; SCREEN = 1920
P = {"L0_Sky": 0.05, "L1_Far": 0.2, "L2_Mid": 0.5, "L3_Walk": 1.0, "L4_Fore": 1.3}

img = cv2.imread(SRC)                       # BGR
H, W = img.shape[:2]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL).astype(int)   # H 0-255
hue = hsv[:, :, 0] * 360 / 256; sat = hsv[:, :, 1] / 255; val = hsv[:, :, 2] / 255
yy = np.arange(H)[:, None] * np.ones((1, W))

# --- 天空：暖黄色（色相 31–70）且与顶边连通 ---
sky = ((hue > 31) & (hue < 70) & (sat > 0.2) & (val > 0.55) & (yy < 700)).astype(np.uint8)
sky = cv2.morphologyEx(sky, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab = cv2.connectedComponents(sky)
top_ids = set(np.unique(lab[0])) - {0}
sky = np.isin(lab, list(top_ids)).astype(np.uint8)
sky = cv2.morphologyEx(sky, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

# --- 田野顶边：每列从 640 往下找第一段田野色 ---
field = (hue > 34) & (hue < 62) & (sat > 0.55) & (val > 0.45)
ftop = np.full(W, 700)
for x in range(W):
    col = field[640:900, x]
    run = np.convolve(col, np.ones(6), "valid") >= 6
    idx = np.argmax(run) if run.any() else 60
    ftop[x] = 640 + idx
ftop = cv2.medianBlur(ftop.astype(np.uint8 if ftop.max() < 256 else np.uint16).reshape(1, -1).astype(np.float32), 5).ravel().astype(int) if False else ftop
ftop = np.array(np.convolve(np.pad(ftop, 15, mode="edge"), np.ones(31) / 31, "valid"), int)

# --- 村舍 + 树 + 石墙（GrabCut）---
rect_mask = np.zeros((H, W), np.uint8)
gc = np.full((H, W), cv2.GC_BGD, np.uint8)
x0, y0, x1, y1 = 0, 180, 1220, 980
gc[y0:y1, x0:x1] = cv2.GC_PR_BGD
cv2.rectangle(gc, (0, 260), (470, 640), cv2.GC_PR_FGD, -1)         # 村舍
cv2.rectangle(gc, (240, 200), (690, 600), cv2.GC_PR_FGD, -1)        # 树
cv2.rectangle(gc, (0, 600), (1150, 760), cv2.GC_PR_FGD, -1)         # 石墙
gc[sky == 1] = cv2.GC_BGD
bgd = np.zeros((1, 65), np.float64); fgd = np.zeros((1, 65), np.float64)
small = cv2.resize(img, (W // 2, H // 2)); gcs = cv2.resize(gc, (W // 2, H // 2), interpolation=cv2.INTER_NEAREST)
cv2.grabCut(small, gcs, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
house = np.isin(cv2.resize(gcs, (W, H), interpolation=cv2.INTER_NEAREST), [cv2.GC_FGD, cv2.GC_PR_FGD]).astype(np.uint8)
house = cv2.morphologyEx(house, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(house)
keep = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] > 4000]
house = np.isin(lab, keep).astype(np.uint8)

# --- v4：村舍背后的远景用 MJ 编辑器擦除重画的版本（_pan_empty）补，替换原来的模糊 inpaint ---
EMPTY = SRC.replace("_pan.png", "_pan_empty.png")
B = img.copy()
if os.path.exists(EMPTY):
    E = cv2.imread(EMPTY)
    if E.shape != img.shape: E = cv2.resize(E, (W, H), interpolation=cv2.INTER_LANCZOS4)
    M = cv2.dilate(house, np.ones((41, 41), np.uint8)).astype(np.float32)
    M[:420, :900] = 1                                   # 左上山脊上的小尖顶也一起换掉（只保留中间那座古墓）
    M[(yy >= ftop[None, :] + 12)] = 0                     # 田野部分仍用原图
    M = cv2.GaussianBlur(M, (51, 51), 0)[..., None]
    B = (img * (1 - M) + E * M).astype(np.uint8)
    hsvB = cv2.cvtColor(B, cv2.COLOR_BGR2HSV_FULL).astype(int)
    hueB = hsvB[:, :, 0] * 360 / 256; satB = hsvB[:, :, 1] / 255; valB = hsvB[:, :, 2] / 255
    sky = ((hueB > 31) & (hueB < 70) & (satB > 0.2) & (valB > 0.55) & (yy < 700)).astype(np.uint8)
    sky = cv2.morphologyEx(sky, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    n_, lab_ = cv2.connectedComponents(sky)
    sky = np.isin(lab_, list(set(np.unique(lab_[0])) - {0})).astype(np.uint8)
    sky = cv2.morphologyEx(sky, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

# --- v7：天空改为「逐列找山脊」：从上往下找第一段连续的山体色（偏粉橙、色相<30），山脊上方 8 px 起算远景，
#     这样山脊墨线整条留在远景层，天空层里不会残留第二条山脊线 ---
_hsv = cv2.cvtColor(B, cv2.COLOR_BGR2HSV_FULL).astype(int)
_h = _hsv[:, :, 0] * 360 / 256; _s = _hsv[:, :, 1] / 255; _v = _hsv[:, :, 2] / 255
hillc = (((_h < 30) | (_h > 150)) & (_s > 0.3) & (_v > 0.35)) | ((_h > 80) & (_h < 300) & (_v > 0.25))   # v9：左上角低饱和的灰绿 / 蓝绿山坡也算山
ridge = np.full(W, -1)
for x in range(W):
    col = hillc[:700, x]
    run = np.convolve(col, np.ones(10), "valid") >= 10
    if run.any(): ridge[x] = int(np.argmax(run))
# v9：找不到山体色的列（画面最左边是低饱和的灰绿山坡）用相邻有效列补，避免左上角整片被当成天空
valid = np.where(ridge >= 0)[0]
ridge = np.interp(np.arange(W), valid, ridge[valid]).astype(int)
print("ridge left 0..80:", ridge[:80:10])
ridge = np.array(np.convolve(np.pad(ridge, 4, mode="edge"), np.ones(9) / 9, "valid"), int)
sky = (yy < (ridge[None, :] - 8)).astype(np.uint8)

# --- 分层遮罩 ---
below_ftop = yy >= (ftop[None, :] + 12)   # v3：避开树线下那条墨线，墨线留在远景层
PATH_TOP = 955; FORE_TOP = 1015
xx = np.ones((H, 1)) * np.arange(W)[None, :]
mid = ((below_ftop & (yy < PATH_TOP)) | (house == 1) | ((yy >= 700) & (xx < 1300) & (yy < PATH_TOP))).astype(np.uint8)   # v5：石墙下方到田野之间不留空，否则露出远景的拉伸色
walk = (yy >= PATH_TOP).astype(np.uint8)
fore = ((yy >= FORE_TOP) & (val < 0.32)) | (yy >= 1065)
fore = cv2.morphologyEx(fore.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
far = ((sky == 0) & (yy < PATH_TOP)).astype(np.uint8)   # v4：远景在村舍背后也是完整的山坡

def feather(m, r=2):
    return cv2.GaussianBlur(m.astype(np.float32), (2 * r + 1, 2 * r + 1), 0)

def fill(base, hole, method="inpaint"):
    """把 hole 区域补满（被前一层挡住、视差时会露出来的部分）"""
    out = base.copy()
    if method == "inpaint":
        k = 4
        sm = cv2.resize(base, (W // k, H // k), interpolation=cv2.INTER_AREA)
        hm = cv2.resize(hole.astype(np.uint8), (W // k, H // k), interpolation=cv2.INTER_NEAREST)
        hm = cv2.dilate(hm, np.ones((3, 3), np.uint8))
        f = cv2.inpaint(sm, hm, 9, cv2.INPAINT_TELEA)
        f = cv2.GaussianBlur(cv2.resize(f, (W, H), interpolation=cv2.INTER_CUBIC), (9, 9), 0)
        m = cv2.dilate(hole.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
        out[m] = f[m]
    else:  # 向下拉伸：每列用洞上方最后一个有效像素往下填
        for x in range(W):
            colh = hole[:, x]
            if not colh.any(): continue
            ys = np.where(colh)[0]
            src = max(ys.min() - 2, 0)
            out[ys, x] = base[src, x]
        out = np.where(hole[..., None], cv2.GaussianBlur(out, (1, 15), 0), out)
    return out

layers = {}
# L0：天空补满（盖在远景后面）
specks = cv2.dilate(((_v < 0.6) & (yy < ridge[None, :] - 8)).astype(np.uint8), np.ones((9, 9), np.uint8))   # v8：山脊上方零星的墨点 / 短线（原画山肩的虚线）一并从天空层擦掉
l0 = fill(B, (yy >= (ridge[None, :] - 16)) | (specks == 1), "inpaint"); layers["L0_Sky"] = (l0, np.ones((H, W), np.float32))
# L1：远景，向下补到画底，被中景挡住的地方拉伸
l1 = B.copy()   # v6：树线以下直接用原图田野（不再铺中位色），中景与远景之间露出的窄缝就是真实的田野纹理
a1 = feather(np.maximum(far, (yy >= ftop[None, :] - 2) & (yy < PATH_TOP + 40)))
layers["L1_Far"] = (l1, a1 * (sky == 0) + a1 * (yy > 700) * (sky == 1))
# L2：中景，被路面挡住的地方向下拉伸
l2 = fill(img, yy >= PATH_TOP, "stretch")
a2 = feather(np.maximum(mid, (yy >= PATH_TOP) & (yy < PATH_TOP + 60) & below_ftop)); layers["L2_Mid"] = (l2, a2)
# L3：可行走层（路面），被前景草挡住的地方拉伸
l3 = img.copy()   # v5：不再向下拉伸；前景草的空隙里露出的是原图的草，不是拉伸条纹
a3 = feather(walk, 1); layers["L3_Walk"] = (l3, a3)
# L4：前景草
layers["L4_Fore"] = (img, feather(fore, 1))

PAD = int(round((GROUND + 270 / S) - H))   # 底部补齐，使路面距画底 270 px（放大后）
ws = {}
for name, (bgr, al) in layers.items():
    p = P[name]
    need = int((SCREEN + (LEVEL - SCREEN) * p) * 1.05 / S) + 1     # 原图中需要的宽度
    if need > W:   # v2：前景层不够宽时水平镜像接上（草地可以无缝镜像）
        bgr = np.hstack([bgr, bgr[:, ::-1]]); al = np.hstack([al, al[:, ::-1]])
    rgb = cv2.cvtColor(bgr[:, :need], cv2.COLOR_BGR2RGB)
    alpha = (np.clip(al[:, :need], 0, 1) * 255).astype(np.uint8)
    if PAD > 0:
        base = np.median(rgb[-40:].reshape(-1, 3), 0).astype(np.uint8)
        rgb = np.vstack([rgb, np.tile(base, (PAD, rgb.shape[1], 1))])
        alpha = np.vstack([alpha, np.repeat(alpha[-1:], PAD, 0)])
    rgba = np.dstack([rgb, alpha])
    im = Image.fromarray(rgba, "RGBA")
    im = im.resize((int(im.width * S), int(im.height * S)), Image.LANCZOS)
    im.save(os.path.join(OUT, f"S1_Village_{name}_wip.png"), optimize=False)
    ws[name] = im.size
print("PAD", PAD, ws)
np.save(os.path.join(OUT, "_ftop.npy"), ftop)
