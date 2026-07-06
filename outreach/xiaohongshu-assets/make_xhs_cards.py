from __future__ import annotations

import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "cards"
SCREENSHOTS = ROOT / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)
for old_card in OUT.glob("*.png"):
    old_card.unlink()

W, H = 1080, 1350


def font_candidates(bold: bool = False) -> list[Path]:
    if sys.platform.startswith("win"):
        font_dir = Path(os.environ.get("WINDIR", "Windows")) / "Fonts"
        return [font_dir / ("msyhbd.ttc" if bold else "msyh.ttc"), font_dir / "simhei.ttf"]
    if sys.platform == "darwin":
        return [Path("/System/Library/Fonts/PingFang.ttc")]
    return [
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
    ]


def pick_font(bold: bool = False) -> Path:
    for candidate in font_candidates(bold):
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No CJK font found. Install Microsoft YaHei, PingFang, Noto Sans CJK, or WenQuanYi.")


FONT_REG = pick_font(False)
FONT_BOLD = pick_font(True)

INK = "#0f172a"
MUTED = "#475569"
BLUE = "#2563eb"
GREEN = "#059669"
CYAN = "#0891b2"
RED = "#dc2626"
BG = "#f8fafc"
CARD = "#ffffff"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap_pixels(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for raw in text.split("\n"):
        current = ""
        for char in raw:
            candidate = current + char
            if current and text_width(draw, candidate, fnt) > max_width:
                lines.append(current.rstrip())
                current = char.lstrip()
            else:
                current = candidate
        lines.append(current.rstrip())
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 14,
) -> int:
    x, y = xy
    for line in wrap_pixels(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def round_rect(draw: ImageDraw.ImageDraw, box, radius=30, fill=CARD, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base(title: str, idx: str, accent: str = BLUE) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 26), fill=accent)
    draw.ellipse((-160, -130, 360, 390), fill="#dbeafe")
    draw.ellipse((790, 910, 1270, 1390), fill="#ccfbf1")
    draw.text((70, 64), "OpenSciFlow", font=font(34, True), fill=accent)
    draw.text((70, 112), idx, font=font(24), fill=MUTED)
    draw_wrapped(draw, title, (70, 185), font(58, True), INK, 880, 18)
    return img, draw


def save(img: Image.Image, name: str):
    img.save(OUT / name, quality=94, optimize=True)


def paste_screenshot(
    img: Image.Image,
    draw: ImageDraw.ImageDraw,
    screenshot_name: str,
    box: tuple[int, int, int, int],
    source_crop: tuple[int, int, int, int] | None = None,
):
    src = Image.open(SCREENSHOTS / screenshot_name).convert("RGB")
    if source_crop is not None:
        src = src.crop(source_crop)
    x1, y1, x2, y2 = box
    frame_w, frame_h = x2 - x1, y2 - y1

    scaled_w = frame_w - 36
    scaled_h = int(src.height * scaled_w / src.width)
    resized = src.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
    cropped = resized.crop((0, 0, scaled_w, min(scaled_h, frame_h - 36)))

    round_rect(draw, box, 28, "#ffffff", "#cbd5e1", 2)
    img.paste(cropped, (x1 + 18, y1 + 18))


def card_01():
    img, draw = base("我在发起一个\nAI for Science\n本地 Agent 开放协议", "01 / 封面", BLUE)
    draw_wrapped(
        draw,
        "不是再做万能 AI Scientist，而是先做一层可检查、可执行、可复现的协议。",
        (80, 540),
        font(35),
        MUTED,
        880,
    )
    round_rect(draw, (80, 840, 1000, 1095), 34, "#eff6ff", "#bfdbfe")
    draw.text((120, 885), "manifest-first + local-first", font=font(38, True), fill=BLUE)
    draw.text((120, 950), "reproducibility-first", font=font(38, True), fill=GREEN)
    draw.text((120, 1015), "opensciflow.yaml / workflow template / run record", font=font(27), fill=INK)
    draw.text((80, 1215), "GitHub 搜：OpenSciFlow", font=font(36, True), fill=GREEN)
    save(img, "01-cover.png")


def card_02():
    img, draw = base("AI for Science 工具很多\n但真正跑起来很痛苦", "02 / 痛点", GREEN)
    items = [
        "环境装不上",
        "模型权重和版本说不清",
        "GPU / HPC 要求不透明",
        "license / citation 容易漏",
        "跑完之后难以复现",
    ]
    y = 480
    for i, item in enumerate(items, 1):
        round_rect(draw, (90, y, 990, y + 105), 26, CARD, "#d1fae5")
        draw.text((130, y + 28), f"{i}. {item}", font=font(34, True), fill=INK)
        y += 130
    save(img, "02-pain-points.png")


def card_03():
    img, draw = base("先不做万能 Agent\n先做 Agent 能读懂的协议层", "03 / 核心想法", BLUE)
    boxes = [
        ("opensciflow.yaml", "工具/模型怎么运行\n输入、输出、环境、权重、引用"),
        ("workflow template", "科研任务怎么分步骤\n哪些插件可用，产物是什么"),
        ("run record", "这次到底跑了什么\n命令、版本、日志、文件 hash"),
    ]
    y = 485
    for title, body in boxes:
        round_rect(draw, (80, y, 1000, y + 180), 30, CARD, "#bfdbfe")
        draw.text((125, y + 32), title, font=font(36, True), fill=BLUE)
        draw_wrapped(draw, body, (125, y + 88), font(29), MUTED, 800, 8)
        y += 220
    save(img, "03-protocol-layer.png")


def card_04():
    img, draw = base("已经公开在 GitHub\n不是停留在 PPT", "04 / GitHub", CYAN)
    paste_screenshot(img, draw, "github-org.png", (72, 380, 1008, 1120), (0, 0, 900, 1420))
    draw_wrapped(
        draw,
        "公开仓库、manifest 草案、workflow 模板、community 文档已经上线。",
        (90, 1170),
        font(30, True),
        INK,
        880,
    )
    save(img, "04-github-org.png")


def card_05():
    img, draw = base("本地 Agent 的安全原则\n不是随便执行 shell", "05 / Local agent", BLUE)
    paste_screenshot(img, draw, "agent-contract.png", (72, 380, 1008, 1110))
    round_rect(draw, (90, 1160, 990, 1260), 24, "#eff6ff", "#bfdbfe")
    draw_wrapped(
        draw,
        "只执行 manifest 里审阅过的命令模板，并记录 run record。",
        (125, 1186),
        font(30, True),
        BLUE,
        800,
    )
    save(img, "05-local-agent-contract.png")


def card_06():
    img, draw = base("现在已经开源了什么", "06 / 进展", GREEN)
    stats = [
        ("79+", "related projects mapped"),
        ("7", "plugin manifest drafts"),
        ("5", "workflow templates"),
        ("R0-R6", "readiness levels"),
        ("1", "run-record schema"),
        ("BioPilot", "reference prototype"),
    ]
    y = 395
    for num, label in stats:
        round_rect(draw, (80, y, 1000, y + 105), 24, CARD, "#bbf7d0")
        draw.text((120, y + 23), num, font=font(36, True), fill=GREEN)
        draw.text((360, y + 29), label, font=font(29, True), fill=INK)
        y += 125
    save(img, "06-current-progress.png")


def card_07():
    img, draw = base("我们不声称", "07 / 边界", CYAN)
    no_items = [
        "自动发现科学真理",
        "自动完成药物研发",
        "替代现有科研工具",
        "验证模型科学正确性",
        "和 listed projects 已经合作",
    ]
    y = 390
    for item in no_items:
        draw.text((95, y), "x", font=font(42, True), fill=RED)
        draw.text((155, y + 4), item, font=font(34, True), fill=INK)
        y += 90
    round_rect(draw, (80, 895, 1000, 1085), 34, "#ecfdf5", "#bbf7d0")
    draw.text((125, 940), "我们先做：", font=font(34, True), fill=GREEN)
    draw_wrapped(draw, "可检查、可执行、可复现的本地 Agent 协议层", (125, 998), font(36, True), INK, 780)
    save(img, "07-boundaries.png")


def card_08():
    img, draw = base("最需要的不是点赞\n而是纠错", "08 / 参与", GREEN)
    items = [
        "协议字段够不够？",
        "哪些模型/工具应该优先支持？",
        "HPC / Slurm 还缺哪些字段？",
        "本地 Agent 权限应该怎么限制？",
        "哪些结果最容易被误解？",
    ]
    y = 420
    for item in items:
        round_rect(draw, (90, y, 990, y + 86), 24, CARD, "#bbf7d0")
        draw.text((130, y + 23), item, font=font(29, True), fill=INK)
        y += 108
    round_rect(draw, (90, 1030, 990, 1190), 32, "#eff6ff", "#bfdbfe")
    draw.text((130, 1078), "GitHub 搜：OpenSciFlow", font=font(42, True), fill=BLUE)
    draw.text((130, 1140), "先求被纠错，再求被使用。", font=font(30, True), fill=GREEN)
    save(img, "08-call-to-action.png")


def main():
    for fn in [card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08]:
        fn()
    print(f"Generated cards in {OUT}")


if __name__ == "__main__":
    main()
