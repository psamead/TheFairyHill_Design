"""Apply the 2026-11-14 approved ImagineEye scope change to the readable DOCX.

The current Word file has manual typography that should not be rebuilt from
older source scripts. This makes targeted, asserted edits in place.
"""

from pathlib import Path
from docx import Document


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "StoryDesign" / "妖精丘陵_Demo设计与开发实施说明.docx"
doc = Document(PATH)


def replace(paragraph, old, new):
    actual = paragraph.text
    assert old in actual, f"Expected text missing: {old!r}; got {actual!r}"
    for run in paragraph.runs:
        if old in run.text:
            run.text = run.text.replace(old, new)
            return
    raise AssertionError(f"Text spans multiple formatted runs: {old!r}")


P = doc.paragraphs
T = doc.tables

assert "2026-11-14 核心体验" not in P[6].text
P[6].add_run("  ·  2026-11-14 核心体验：获得想象之眼、切换现实与幻象视野，并在后续主线再次使用；第一、二章范围不变。")
replace(P[24], "用十字架显形漂浮石块；拾得欧甘石牌；拼字开门", "用十字架显形漂浮石块；通过欧甘文字线索获得想象之眼，切换现实与幻象视野寻找主线线索或道路；拾得欧甘石牌；拼字开门。获得镜头与关卡位置待灰盒验证")
replace(P[25], "铁十字架、存在值、欧甘谜题", "区分十字架脉冲与视野切换；掌握想象之眼、存在值和欧甘谜题")
replace(P[27], "与守门贵族对话；选择交出名字或拒绝", "再次切换视野，辨认一条不剧透守门者身份的线索；与守门贵族对话，选择交出名字或拒绝")
replace(P[28], "交易与代价", "再次用能力推动主线；人物互动、交易与代价")
replace(P[45], "能力系统可注册新能力（想象之眼等）", "能力系统可注册后续新能力；想象之眼的获得状态和视野状态在 S3→S4 间保持一致")
replace(P[54], "Should / Could", "Should / Must")
replace(P[55], "回忆、想象之眼", "回忆、想象之眼的获得 / 切换反馈")
replace(P[92], "是否理解铁十字架和欧甘门", "是否区分铁十字架脉冲与想象之眼视野切换、是否在后续主线再次切换、是否理解欧甘门")
replace(P[110], "以后可作为「想象之眼」的解锁道具", "可加强想象之眼的民俗呼应，但不能成为主线必需能力的可选解锁条件")

replace(T[0].cell(1, 1).paragraphs[0], "铁十字架（驱散 / 显形平台）；", "铁十字架（驱散 / 显形平台）；想象之眼（现实 / 幻象视野切换，获得后在主线再次使用）；")
replace(T[0].cell(3, 1).paragraphs[0], "想象之眼蜡笔滤镜", "想象之眼的蜡笔滤镜精修")
replace(T[1].cell(6, 0).paragraphs[0], "想象之眼（Could）", "想象之眼 ImagineEye（Must）")
replace(T[1].cell(6, 1).paragraphs[0], "切换蓝色蜡笔滤镜，显示 1 条隐藏路线；持续时每 3 秒存在值 -1", "主动切换现实 / 幻象视野；S3 获得并使用一次，后续主线再次使用以看见线索或道路；持续时每 3 秒存在值 -1 是待试玩初值。视野差异须可读，蜡笔滤镜精修可后置")
replace(T[1].cell(6, 2).paragraphs[0], "后处理 + 隐藏图层显隐", "AbilitySystem 状态切换 + 隐藏图层显隐；与 IronPulse 瞬时脉冲分开；获得、切换、回到现实均须有反馈")
replace(T[4].cell(3, 1).paragraphs[0], "铁十字架、欧甘门", "铁十字架、想象之眼、欧甘门")
replace(T[4].cell(3, 2).paragraphs[0], "试玩者在无讲解的情况下能完成一遍流程", "试玩者能获得并切换想象之眼，在后续主线再次使用，然后在无讲解的情况下完成交易与结尾")
replace(T[5].cell(1, 1).paragraphs[0], "普卡交易、想象之眼；", "普卡交易、想象之眼的深化玩法；")

doc.save(PATH)
print(PATH)
