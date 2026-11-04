# 抠出 MJ 道具图（米色底）：与画布边缘连通的底色 = 背景；去掉底部散草 / 影子；裁到物体边界
import sys, numpy as np, cv2
from scipy import ndimage
from PIL import Image
def cut(src, dst, bottom_trim=0):
    im = np.array(Image.open(src).convert("RGB")).astype(int); H, W, _ = im.shape
    edge = np.concatenate([im[:8].reshape(-1,3), im[:, :8].reshape(-1,3), im[:, -8:].reshape(-1,3)])
    bg = np.median(edge, 0)
    # 底色有渐变：用局部模糊图作背景估计
    blur = cv2.GaussianBlur(im.astype(np.float32), (0, 0), 60)
    diff = np.abs(im - blur).sum(2); sat = (im.max(2) - im.min(2))
    near = (diff < 40) & (np.abs(im - bg).sum(2) < 140)
    lab, n = ndimage.label(near)
    border = set(np.unique(np.r_[lab[0], lab[:, 0], lab[:, -1]])) - {0}
    fg = ~np.isin(lab, list(border))
    # v2：米色 / 浅黄底（亮、低饱和）一律当背景，去掉物体周围的光晕
    hsv = cv2.cvtColor(im.astype(np.uint8), cv2.COLOR_RGB2HSV).astype(int)
    beige = (hsv[:, :, 2] > 175) & (hsv[:, :, 1] < 110)
    fg &= ~beige
    fg = ndimage.binary_opening(fg, iterations=2)
    lab, n = ndimage.label(fg); sz = ndimage.sum(fg, lab, range(1, n+1)); fg = lab == (sz.argmax() + 1)
    fg = ndimage.binary_fill_holes(fg)
    fg &= ~beige   # v3：被物体围住的米色底（如栅门下方的空隙）也去掉
    fg = ndimage.binary_opening(fg, iterations=1)
    # 去底部散草：每行前景宽度 < 最大宽度 50% 且位于下 25% → 去掉
    rows = fg.sum(1); ys = np.where(rows > 0)[0]; mx = rows.max()
    for y in range(ys[-1], int(ys[0] + (ys[-1]-ys[0])*0.75), -1):
        if rows[y] < mx * 0.5: fg[y] = False
        else: break
    if bottom_trim: fg[ys[-1]-bottom_trim+1:] = False
    a = cv2.GaussianBlur(fg.astype(np.float32), (3, 3), 0)
    ys, xs = np.where(fg)
    out = np.dstack([im.astype(np.uint8), (a*255).astype(np.uint8)])[ys.min():ys.max()+1, xs.min():xs.max()+1]
    Image.fromarray(out, "RGBA").save(dst); print(dst, out.shape)
cut(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 0)
