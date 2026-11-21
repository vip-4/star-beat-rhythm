# -*- coding: utf-8 -*-
"""產生 1200x630 的 Open Graph 分享圖（僅需 Pillow，無外部素材）。"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
OUTPUT = Path(__file__).resolve().parents[1] / "og-image.png"

FONT_CANDIDATES = [
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/NotoSansTC-Bold.otf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main():
    image = Image.new("RGB", (WIDTH, HEIGHT), "#16112f")
    draw = ImageDraw.Draw(image)

    # 斜向漸層背景
    for y in range(HEIGHT):
        for x in range(0, WIDTH, 4):
            t = (x / WIDTH + y / HEIGHT) / 2
            r = int(0x2b * (1 - t) + 0x16 * t)
            g = int(0x23 * (1 - t) + 0x11 * t)
            b = int(0x50 * (1 - t) + 0x2f * t)
            draw.rectangle([x, y, x + 4, y + 1], fill=(r, g, b))

    gold = "#f5c451"
    colors = ["#e05c65", "#e6a23c", "#4a90d9", "#7b68ae"]

    # 四条轨道与音符
    for i, color in enumerate(colors):
        x = 150 + i * 110
        draw.rounded_rectangle([x - 30, 150, x + 30, 470], radius=14,
                               fill=(35, 28, 65), outline=color, width=3)
        draw.rounded_rectangle([x - 26, 250 + i * 45, x + 26, 274 + i * 45],
                               radius=9, fill=color)
        draw.rounded_rectangle([x - 30, 438, x + 30, 446], radius=3, fill=gold)

    font_title = load_font(76)
    font_sub = load_font(28)
    font_body = load_font(32)
    font_small = load_font(22)

    draw.text((620, 190), "星節奏", font=font_title, fill="#ffffff")
    draw.text((624, 285), "S T A R   B E A T", font=font_sub, fill=gold)
    draw.text((624, 350), "原創 HTML5 四軌節奏遊戲", font=font_body, fill="#dfe6f2")
    draw.text((624, 402), "無外部素材 · Web Audio 合成 · 靜態托管", font=font_small, fill="#a9a3c4")

    draw.rounded_rectangle([620, 470, 1120, 542], radius=18, fill="#2b2350", outline=gold, width=2)
    draw.text((870, 506), "免註冊 · 免下載 · 立即遊玩", font=font_small, fill=gold, anchor="mm")

    image.save(OUTPUT, optimize=True)
    print(f"已產生：{OUTPUT}")


if __name__ == "__main__":
    main()
