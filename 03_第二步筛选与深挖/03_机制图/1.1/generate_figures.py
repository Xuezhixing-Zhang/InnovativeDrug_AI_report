from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


OUT_DIR = Path(__file__).resolve().parent
W, H = 1800, 1100


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


F_TITLE = font(50, True)
F_H = font(32, True)
F_M = font(24, True)
F_S = font(20)
F_XS = font(17)


def base_canvas(title: str, subtitle: str) -> Image.Image:
    img = Image.new("RGBA", (W, H), (248, 250, 249, 255))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(248 * (1 - t) + 235 * t)
        g = int(250 * (1 - t) + 246 * t)
        b = int(249 * (1 - t) + 244 * t)
        d.line([(0, y), (W, y)], fill=(r, g, b, 255))
    d.text((70, 42), title, fill=(31, 45, 58), font=F_TITLE)
    d.text((75, 108), subtitle, fill=(72, 88, 101), font=F_S)
    return img


def text_box(d: ImageDraw.ImageDraw, xy, text, fill=(255, 255, 255, 235), outline=(190, 205, 210), color=(32, 45, 56), f=F_S):
    x, y = xy
    pad_x, pad_y = 16, 8
    bbox = d.textbbox((0, 0), text, font=f)
    w, h = bbox[2] - bbox[0] + 2 * pad_x, bbox[3] - bbox[1] + 2 * pad_y
    d.rounded_rectangle((x, y, x + w, y + h), radius=8, fill=fill, outline=outline, width=1)
    d.text((x + pad_x, y + pad_y - 1), text, fill=color, font=f)


def arrow(d: ImageDraw.ImageDraw, p1, p2, color=(54, 112, 138), width=6):
    x1, y1 = p1
    x2, y2 = p2
    d.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    head = 20
    pts = [
        (x2, y2),
        (x2 - head * math.cos(ang - 0.45), y2 - head * math.sin(ang - 0.45)),
        (x2 - head * math.cos(ang + 0.45), y2 - head * math.sin(ang + 0.45)),
    ]
    d.polygon(pts, fill=color)


def curved_line(d: ImageDraw.ImageDraw, pts, fill, width=5):
    d.line(pts, fill=fill, width=width, joint="curve")


def draw_protein_blob(layer: Image.Image, center, scale=1.0, colors=((81, 158, 169), (118, 192, 178), (90, 131, 178))):
    d = ImageDraw.Draw(layer, "RGBA")
    cx, cy = center
    blobs = [
        (-140, -30, 220, 135, colors[0]),
        (-40, -100, 260, 130, colors[1]),
        (105, -40, 210, 130, colors[2]),
        (-105, 80, 270, 120, colors[1]),
        (90, 90, 250, 120, colors[0]),
        (-15, 20, 260, 190, (229, 211, 123)),
    ]
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow, "RGBA")
    for ox, oy, bw, bh, col in blobs:
        x0 = cx + ox * scale
        y0 = cy + oy * scale
        sd.ellipse((x0, y0, x0 + bw * scale, y0 + bh * scale), fill=(30, 50, 60, 35))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    layer.alpha_composite(shadow)
    for ox, oy, bw, bh, col in blobs:
        x0 = cx + ox * scale
        y0 = cy + oy * scale
        d.ellipse((x0, y0, x0 + bw * scale, y0 + bh * scale), fill=(*col, 218), outline=(255, 255, 255, 150), width=2)
    # Ribbon traces over the surface.
    for phase, col in [(0, (39, 107, 126, 220)), (1.7, (233, 138, 84, 230)), (3.0, (67, 91, 158, 210))]:
        pts = []
        for i in range(120):
            t = i / 119
            x = cx + scale * (-140 + 330 * t)
            y = cy + scale * (40 * math.sin(4.8 * math.pi * t + phase) + 60 * math.sin(1.2 * math.pi * t + phase / 2))
            pts.append((x, y))
        curved_line(d, pts, col, max(3, int(7 * scale)))


def draw_ligand(d: ImageDraw.ImageDraw, cx, cy, s=1.0, color=(230, 91, 78)):
    r = 28 * s
    pts = []
    for i in range(6):
        a = math.pi / 6 + i * math.pi / 3
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.line(pts + [pts[0]], fill=color, width=max(3, int(4 * s)))
    d.line((cx + r, cy, cx + 2.1 * r, cy - 18 * s), fill=color, width=max(3, int(4 * s)))
    d.ellipse((cx + 2.0 * r - 8 * s, cy - 18 * s - 8 * s, cx + 2.0 * r + 8 * s, cy - 18 * s + 8 * s), fill=(247, 193, 67))
    d.line((cx - r, cy, cx - 1.7 * r, cy + 22 * s), fill=color, width=max(3, int(4 * s)))
    d.ellipse((cx - 1.7 * r - 8 * s, cy + 22 * s - 8 * s, cx - 1.7 * r + 8 * s, cy + 22 * s + 8 * s), fill=(74, 149, 214))


def draw_plate(d: ImageDraw.ImageDraw, x, y, cols=6, rows=4, s=18):
    d.rounded_rectangle((x - 14, y - 14, x + cols * s + 14, y + rows * s + 14), radius=14, fill=(236, 242, 246), outline=(149, 169, 183), width=2)
    for r in range(rows):
        for c in range(cols):
            fill = (91, 172, 134) if (r + c) % 3 else (232, 113, 88)
            d.ellipse((x + c * s, y + r * s, x + c * s + 10, y + r * s + 10), fill=fill)


def draw_neural_net(d: ImageDraw.ImageDraw, x, y):
    layers = [4, 6, 5, 3]
    xs = [x + i * 90 for i in range(len(layers))]
    nodes = []
    for li, n in enumerate(layers):
        ys = [y + (i - (n - 1) / 2) * 34 for i in range(n)]
        layer_nodes = [(xs[li], yy) for yy in ys]
        nodes.append(layer_nodes)
    for a, b in zip(nodes, nodes[1:]):
        for p in a:
            for q in b:
                d.line((p[0], p[1], q[0], q[1]), fill=(89, 119, 139, 70), width=1)
    for layer_nodes in nodes:
        for nx, ny in layer_nodes:
            d.ellipse((nx - 11, ny - 11, nx + 11, ny + 11), fill=(44, 108, 145), outline=(255, 255, 255), width=2)


def draw_del(d: ImageDraw.ImageDraw, x, y):
    colors = [(52, 142, 160), (231, 137, 67), (105, 177, 121), (124, 107, 184), (230, 91, 78)]
    for i in range(8):
        x0 = x + i * 34
        if i:
            d.line((x0 - 24, y, x0 - 5, y), fill=(100, 117, 124), width=3)
        d.ellipse((x0 - 14, y - 14, x0 + 14, y + 14), fill=colors[i % len(colors)], outline=(255, 255, 255), width=2)
    for i in range(9):
        h = 26 + (i % 3) * 12
        d.rounded_rectangle((x + i * 18, y + 44, x + i * 18 + 8, y + 44 + h), radius=3, fill=(52, 65, 75))


def draw_new_ai():
    img = base_canvas(
        "Relay Dynamo：动态构象驱动的变构口袋发现",
        "全长结构 + 长时程 MD + ML/REL-DEL + 药化/生物物理闭环，用突变体特有构象窗口设计 RLY-2608 类变构抑制剂",
    )
    d = ImageDraw.Draw(img, "RGBA")

    # Left: experimental structural inputs.
    d.rounded_rectangle((80, 210, 390, 455), radius=26, fill=(255, 255, 255, 210), outline=(204, 216, 222), width=2)
    d.ellipse((128, 255, 220, 335), outline=(49, 95, 124), width=8)
    d.line((174, 335, 150, 405), fill=(49, 95, 124), width=8)
    d.line((174, 335, 232, 402), fill=(49, 95, 124), width=8)
    d.polygon([(254, 270), (330, 244), (322, 342), (258, 325)], fill=(112, 154, 184, 160), outline=(49, 95, 124))
    d.polygon([(285, 300), (333, 286), (330, 340), (292, 351)], fill=(238, 190, 80, 190), outline=(177, 137, 45))
    d.text((112, 218), "Cryo-EM / X-ray", fill=(31, 45, 58), font=F_M)
    d.text((116, 418), "全长 PI3Kα 构象", fill=(65, 79, 89), font=F_S)

    d.rounded_rectangle((80, 560, 390, 845), radius=26, fill=(255, 255, 255, 210), outline=(204, 216, 222), width=2)
    draw_del(d, 125, 650)
    d.text((120, 585), "REL-DEL 富集", fill=(31, 45, 58), font=F_M)
    d.text((120, 755), "突变体 > WT", fill=(230, 91, 78), font=F_M)
    d.text((120, 800), "非 ATP 竞争", fill=(65, 79, 89), font=F_S)

    arrow(d, (390, 335), (520, 385), (56, 122, 145), 7)
    arrow(d, (390, 705), (520, 630), (56, 122, 145), 7)

    # Center: dynamic protein and cryptic pocket.
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw_protein_blob(layer, (780, 540), 1.28)
    img.alpha_composite(layer)
    d = ImageDraw.Draw(img, "RGBA")
    # Dynamic trajectories.
    for k, col in enumerate([(43, 108, 176, 130), (230, 91, 78, 130), (72, 165, 127, 130), (237, 188, 66, 130)]):
        pts = []
        for i in range(170):
            t = i / 169
            x = 530 + 530 * t
            y = 510 + 130 * math.sin(2 * math.pi * t + k * 0.9) + 45 * math.sin(9 * math.pi * t + k)
            pts.append((x, y))
        curved_line(d, pts, col, 4)
    # Allosteric pocket highlight.
    pocket = [(838, 545), (895, 505), (957, 522), (980, 580), (938, 638), (870, 628), (828, 585)]
    d.polygon(pocket, fill=(255, 150, 66, 170), outline=(197, 76, 57), width=4)
    for r in range(4):
        d.ellipse((850 - r * 13, 512 - r * 10, 990 + r * 13, 650 + r * 10), outline=(235, 111, 80, 65), width=3)
    draw_ligand(d, 910, 575, 1.25, (219, 58, 63))
    text_box(d, (838, 682), "隐蔽变构口袋", color=(31, 45, 58), f=F_S)
    text_box(d, (645, 225), "MD 构象系综", fill=(255, 255, 255, 225), color=(31, 45, 58), f=F_M)
    d.text((646, 270), "3-5×10 μs；KD 5×100 μs", fill=(73, 89, 98), font=F_S)
    d.text((585, 830), "H1047R/E542K/E545K 使构象采样偏向可结合状态", fill=(72, 88, 101), font=F_S)

    # Top-right ML scorer and wet-lab loop.
    d.rounded_rectangle((1180, 208, 1665, 430), radius=28, fill=(255, 255, 255, 220), outline=(204, 216, 222), width=2)
    draw_neural_net(d, 1248, 325)
    d.text((1210, 235), "ML 打分/排序", fill=(31, 45, 58), font=F_M)
    d.rounded_rectangle((1200, 380, 1476, 414), radius=8, fill=(255, 255, 255, 215))
    d.text((1212, 383), "SAR / DEL / 结构", fill=(72, 88, 101), font=F_S)
    arrow(d, (1060, 530), (1232, 395), (56, 122, 145), 7)

    d.rounded_rectangle((1180, 545, 1665, 855), radius=28, fill=(255, 255, 255, 220), outline=(204, 216, 222), width=2)
    d.text((1210, 575), "药化/生物物理闭环", fill=(31, 45, 58), font=F_M)
    draw_ligand(d, 1285, 680, 1.25, (219, 58, 63))
    draw_plate(d, 1428, 635, 7, 5, 22)
    d.line((1238, 770, 1595, 770), fill=(148, 164, 174), width=2)
    graph = [(1240, 762), (1300, 735), (1370, 740), (1440, 690), (1510, 645), (1590, 620)]
    d.line(graph, fill=(72, 165, 127), width=5)
    d.text((1230, 805), "亲和力↑ 选择性↑ 胰岛素影响↓", fill=(72, 88, 101), font=F_S)
    arrow(d, (1400, 545), (1040, 655), (56, 122, 145), 6)
    arrow(d, (1400, 430), (1440, 545), (56, 122, 145), 6)

    # Output badge.
    d.rounded_rectangle((500, 930, 1300, 1020), radius=22, fill=(31, 45, 58, 235))
    d.text((535, 955), "输出：突变选择性变构抑制剂候选物（RLY-2608 / zovegalisib）", fill=(255, 255, 255), font=font(27, True))

    img.convert("RGB").save(OUT_DIR / "1.1_新AI机制.png", quality=95)


def draw_cryo_microscope(d, x, y):
    d.ellipse((x + 30, y + 10, x + 130, y + 92), outline=(55, 82, 107), width=8)
    d.rectangle((x + 78, y + 88, x + 96, y + 190), fill=(55, 82, 107))
    d.polygon([(x + 10, y + 190), (x + 165, y + 190), (x + 140, y + 230), (x + 35, y + 230)], fill=(116, 143, 163))
    d.line((x + 90, y + 230, x + 65, y + 292), fill=(55, 82, 107), width=8)
    d.line((x + 90, y + 230, x + 125, y + 292), fill=(55, 82, 107), width=8)


def draw_xray(d, x, y):
    d.polygon([(x + 155, y + 85), (x + 235, y + 50), (x + 255, y + 145), (x + 180, y + 178)], fill=(237, 190, 80, 185), outline=(169, 125, 46))
    for i in range(5):
        yy = y + 64 + i * 24
        d.line((x, yy, x + 150, yy + 15), fill=(62, 138, 172), width=4)
    for i in range(7):
        ang = -1.2 + i * 0.4
        d.line((x + 255, y + 112, x + 255 + 125 * math.cos(ang), y + 112 + 125 * math.sin(ang)), fill=(200, 96, 77, 135), width=3)


def draw_energy_surface(d, x, y):
    # Contour-like FEP/energy landscape.
    for i, col in enumerate([(220, 90, 75), (237, 151, 74), (236, 198, 82), (105, 176, 128), (54, 141, 159)]):
        pad = i * 24
        d.ellipse((x + pad, y + pad * 0.65, x + 330 - pad, y + 185 - pad * 0.55), outline=(*col, 210), width=5)
    path = [(x + 28, y + 142), (x + 90, y + 103), (x + 150, y + 122), (x + 205, y + 75), (x + 280, y + 85)]
    d.line(path, fill=(31, 45, 58), width=5)
    for px, py in path:
        d.ellipse((px - 8, py - 8, px + 8, py + 8), fill=(31, 45, 58))


def draw_baseline():
    img = base_canvas(
        "当前成熟基线：实验结构 + 物理对接/FEP + 湿实验验证",
        "行业标准依赖高质量结构与物理能量模型，可靠但常受限于静态快照、结构可得性和隐蔽口袋采样",
    )
    d = ImageDraw.Draw(img, "RGBA")

    # Experimental structure panel.
    d.rounded_rectangle((70, 205, 515, 500), radius=28, fill=(255, 255, 255, 220), outline=(204, 216, 222), width=2)
    draw_cryo_microscope(d, 110, 260)
    draw_xray(d, 285, 282)
    d.text((105, 225), "结构生物学", fill=(31, 45, 58), font=F_M)
    d.text((290, 455), "冷冻电镜 / X-ray", fill=(72, 88, 101), font=F_S)

    arrow(d, (515, 355), (642, 422), (56, 122, 145), 7)

    # Static protein structure.
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw_protein_blob(layer, (850, 450), 1.08, ((91, 146, 179), (134, 185, 170), (149, 129, 181)))
    img.alpha_composite(layer)
    d = ImageDraw.Draw(img, "RGBA")
    d.ellipse((815, 418, 950, 530), fill=(118, 90, 167, 110), outline=(83, 62, 129), width=4)
    draw_ligand(d, 884, 475, 1.0, (214, 73, 67))
    text_box(d, (720, 230), "静态结合位点", f=F_M)
    d.text((725, 285), "单构象/少数共晶结构", fill=(72, 88, 101), font=F_S)

    # Docking and FEP.
    arrow(d, (1025, 475), (1190, 438), (56, 122, 145), 7)
    d.rounded_rectangle((1170, 250, 1690, 555), radius=28, fill=(255, 255, 255, 220), outline=(204, 216, 222), width=2)
    d.text((1210, 278), "对接 / MD / FEP+", fill=(31, 45, 58), font=F_M)
    draw_energy_surface(d, 1255, 340)
    draw_ligand(d, 1555, 388, 0.72, (214, 73, 67))
    d.text((1210, 500), "ΔG 排序；同系物优化", fill=(72, 88, 101), font=F_S)

    # Wet lab validation.
    d.rounded_rectangle((1180, 650, 1690, 940), radius=28, fill=(255, 255, 255, 220), outline=(204, 216, 222), width=2)
    d.text((1215, 680), "合成与实验验证", fill=(31, 45, 58), font=F_M)
    for i in range(5):
        x = 1230 + i * 58
        d.rectangle((x, 745, x + 28, 865), fill=(207, 220, 227), outline=(100, 118, 129))
        d.polygon([(x, 865), (x + 28, 865), (x + 20, 910), (x + 8, 910)], fill=(235, 129, 91, 190), outline=(100, 118, 129))
    draw_plate(d, 1540, 762, 5, 5, 22)
    d.text((1215, 900), "DMTA 周期：设计-合成-测试-分析", fill=(72, 88, 101), font=F_S)
    arrow(d, (1435, 555), (1435, 650), (56, 122, 145), 7)

    # Bottleneck visual.
    d.rounded_rectangle((80, 620, 535, 935), radius=28, fill=(255, 246, 239, 235), outline=(230, 160, 130), width=2)
    d.text((118, 650), "主要瓶颈", fill=(176, 74, 58), font=F_M)
    # Hourglass.
    d.polygon([(145, 715), (245, 715), (205, 792), (245, 875), (145, 875), (185, 792)], outline=(96, 112, 120), fill=(245, 249, 250), width=4)
    for i in range(18):
        x = 171 + (i % 6) * 9
        y = 740 + (i // 6) * 12
        d.ellipse((x, y, x + 5, y + 5), fill=(221, 151, 64))
    d.polygon([(174, 855), (216, 855), (205, 820), (186, 820)], fill=(221, 151, 64, 180))
    d.text((290, 725), "结构获得慢", fill=(64, 76, 84), font=F_S)
    d.text((290, 777), "难采样隐蔽口袋", fill=(64, 76, 84), font=F_S)
    d.text((290, 829), "突变/WT 选择性难", fill=(64, 76, 84), font=F_S)

    # Visual contrast at center bottom.
    d.rounded_rectangle((620, 735, 1070, 910), radius=24, fill=(235, 242, 245, 220), outline=(190, 205, 210), width=2)
    d.text((655, 760), "可靠性来自物理与实测", fill=(31, 45, 58), font=F_M)
    d.text((655, 815), "但对动态构象/变构网络", fill=(72, 88, 101), font=F_S)
    d.text((655, 855), "通常需要大量迭代补足", fill=(72, 88, 101), font=F_S)

    img.convert("RGB").save(OUT_DIR / "1.1_传统方法.png", quality=95)


if __name__ == "__main__":
    draw_new_ai()
    draw_baseline()
    print("generated: 1.1_new_ai_mechanism.png")
    print("generated: 1.1_baseline_method.png")
