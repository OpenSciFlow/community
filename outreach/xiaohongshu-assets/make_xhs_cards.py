from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "cards"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1350

FONT_DIR = Path("C:/Windows/Fonts")
FONT_REG = FONT_DIR / "msyh.ttc"
FONT_BOLD = FONT_DIR / "msyhbd.ttc"

INK = "#0f172a"
MUTED = "#475569"
BLUE = "#2563eb"
GREEN = "#059669"
CYAN = "#0891b2"
BG = "#f8fafc"
CARD = "#ffffff"
LINE = "#dbeafe"
SOFT = "#ecfeff"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    width_chars: int,
    line_gap: int = 14,
) -> int:
    x, y = xy
    for raw in text.split("\n"):
        lines = wrap(raw, width=width_chars) if raw else [""]
        for line in lines:
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
    draw_wrapped(draw, title, (70, 185), font(58, True), INK, 13, 18)
    return img, draw


def save(img: Image.Image, name: str):
    img.save(OUT / name, quality=94, optimize=True)


def card_01():
    img, draw = base("我想做一套\nAI for Science\n本地 Agent 标准", "01 / 封面", BLUE)
    draw_wrapped(
        draw,
        "不是再做一个万能 AI Scientist，\n而是让科研工具能被安全调用、记录、复现。",
        (80, 520),
        font(36),
        MUTED,
        19,
    )
    round_rect(draw, (80, 860, 1000, 1110), 34, "#eff6ff", "#bfdbfe")
    draw.text((120, 905), "核心：标准化文件 + 本地优先执行", font=font(38, True), fill=BLUE)
    draw.text((120, 970), "opensciflow.yaml / workflow template / run record", font=font(28), fill=INK)
    draw.text((80, 1215), "GitHub 搜：OpenSciFlow", font=font(36, True), fill=GREEN)
    save(img, "01-cover.png")


def card_02():
    img, draw = base("AI for Science 工具很多\n但真正跑起来很痛苦", "02 / 痛点", GREEN)
    items = ["环境装不上", "模型权重不知道从哪来", "GPU / HPC 要求不清楚", "license / citation 容易漏", "结果报告不可复现"]
    y = 480
    for i, item in enumerate(items, 1):
        round_rect(draw, (90, y, 990, y + 105), 26, CARD, "#d1fae5")
        draw.text((130, y + 28), f"{i}. {item}", font=font(34, True), fill=INK)
        y += 130
    save(img, "02-pain-points.png")


def card_03():
    img, draw = base("不先做万能 Agent\n先做 Agent 能读懂的标准文件", "03 / 核心想法", BLUE)
    boxes = [
        ("opensciflow.yaml", "工具/模型怎么运行\n输入、输出、环境、权重、引用"),
        ("workflow template", "科研任务怎么分步骤\n哪些插件可用，产物是什么"),
        ("run record", "这次到底跑了什么\n命令、版本、日志、文件 hash"),
    ]
    y = 485
    for title, body in boxes:
        round_rect(draw, (80, y, 1000, y + 180), 30, CARD, "#bfdbfe")
        draw.text((125, y + 32), title, font=font(36, True), fill=BLUE)
        draw_wrapped(draw, body, (125, y + 88), font(29), MUTED, 28, 8)
        y += 220
    save(img, "03-standard-files.png")


def card_04():
    img, draw = base("本地 Agent 应该这样跑", "04 / 工作流", CYAN)
    steps = ["用户一句话", "匹配 workflow", "读取 manifest", "检查环境/权重/许可证", "只执行已审阅命令", "生成日志、结果和报告"]
    y = 405
    for i, step in enumerate(steps, 1):
        draw.ellipse((92, y + 8, 152, y + 68), fill=CYAN)
        draw.text((111, y + 19), str(i), font=font(26, True), fill="white")
        draw.text((185, y + 13), step, font=font(34, True), fill=INK)
        if i < len(steps):
            draw.line((122, y + 76, 122, y + 130), fill="#67e8f9", width=5)
        y += 135
    save(img, "04-local-agent-flow.png")


def card_05():
    img, draw = base("现在已经开源了什么", "05 / 进展", BLUE)
    stats = [
        ("79+", "AI for Science 项目地图"),
        ("7", "plugin manifest 草案"),
        ("5", "workflow template"),
        ("R0-R6", "readiness levels"),
        ("1", "local agent contract"),
    ]
    y = 420
    for num, label in stats:
        round_rect(draw, (80, y, 1000, y + 125), 28, CARD, "#dbeafe")
        draw.text((125, y + 28), num, font=font(44, True), fill=BLUE)
        draw.text((330, y + 37), label, font=font(32, True), fill=INK)
        y += 150
    save(img, "05-current-progress.png")


def card_06():
    img, draw = base("我们不声称", "06 / 边界", GREEN)
    no_items = ["自动发现科学真理", "自动做药物研发", "替代现有工具", "验证模型科学正确性"]
    y = 385
    for item in no_items:
        draw.text((95, y), "×", font=font(42, True), fill="#dc2626")
        draw.text((155, y + 4), item, font=font(34, True), fill=INK)
        y += 88
    round_rect(draw, (80, 845, 1000, 1070), 34, "#ecfdf5", "#bbf7d0")
    draw.text((125, 895), "我们先做：", font=font(34, True), fill=GREEN)
    draw_wrapped(draw, "可执行、可检查、可复现的协议层", (125, 955), font(38, True), INK, 18)
    save(img, "06-boundaries.png")


def card_07():
    img, draw = base("如果你做这些方向\n欢迎来改协议", "07 / 招募", BLUE)
    items = ["计算生物", "分子模拟", "蛋白设计", "材料模型", "科学工作流", "HPC / Slurm", "开源工具维护"]
    x, y = 90, 455
    for item in items:
        round_rect(draw, (x, y, x + 410, y + 95), 24, CARD, "#bfdbfe")
        draw.text((x + 38, y + 27), item, font=font(30, True), fill=INK)
        x += 465
        if x > 600:
            x = 90
            y += 130
    draw_wrapped(draw, "最需要的不是点赞，\n而是帮我们指出字段哪里不对。", (100, 1050), font(34, True), GREEN, 20)
    save(img, "07-contributors.png")


def card_08():
    img, draw = base("GitHub 搜：OpenSciFlow", "08 / 入口", GREEN)
    round_rect(draw, (90, 405, 990, 725), 34, CARD, "#bbf7d0")
    draw.text((130, 455), "最想要的反馈", font=font(40, True), fill=GREEN)
    draw_wrapped(
        draw,
        "1. 协议字段够不够？\n2. 哪些模型/工具应该先支持？\n3. 本地 Agent 应该怎么限制权限？",
        (130, 535),
        font(34),
        INK,
        24,
    )
    round_rect(draw, (90, 850, 990, 1035), 34, "#eff6ff", "#bfdbfe")
    draw.text((130, 900), "OpenSciFlow", font=font(52, True), fill=BLUE)
    draw.text((130, 975), "早期开源倡议 / correction-first", font=font(30), fill=MUTED)
    save(img, "08-call-to-action.png")


def main():
    for fn in [card_01, card_02, card_03, card_04, card_05, card_06, card_07, card_08]:
        fn()
    print(f"Generated cards in {OUT}")


if __name__ == "__main__":
    main()
