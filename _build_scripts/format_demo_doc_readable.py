"""Make the current human-facing Demo Word document readable in portrait A4.

This works on the existing DOCX, preserving its later editorial updates. The
older doc_impl.js data is not a safe source for rebuilding the current file.
"""

from pathlib import Path
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Twips


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "StoryDesign" / "妖精丘陵_Demo设计与开发实施说明.docx"
GREEN = "2F5D3A"


def set_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell):
    tc_pr = cell._tc.get_or_add_tcPr()
    margins = tc_pr.find(qn("w:tcMar"))
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tc_pr.append(margins)
    for edge, size in (("top", 90), ("bottom", 90), ("left", 110), ("right", 110)):
        tag = margins.find(qn(f"w:{edge}"))
        if tag is None:
            tag = OxmlElement(f"w:{edge}")
            margins.append(tag)
        tag.set(qn("w:w"), str(size))
        tag.set(qn("w:type"), "dxa")


def set_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.find(qn("w:tblBorders"))
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = borders.find(qn(f"w:{edge}"))
        if tag is None:
            tag = OxmlElement(f"w:{edge}")
            borders.append(tag)
        tag.set(qn("w:val"), "single")
        tag.set(qn("w:sz"), "4")
        tag.set(qn("w:color"), "D7E1D8")


def set_table_widths(table, widths):
    table.autofit = False
    twips = [round(w * 1440) for w in widths]
    tbl_w = table._tbl.tblPr.find(qn("w:tblW"))
    tbl_w.set(qn("w:type"), "dxa")
    tbl_w.set(qn("w:w"), str(sum(twips)))
    for col, width in zip(table.columns, twips):
        col.width = Twips(width)
    for row in table.rows:
        for cell, width in zip(row.cells, twips):
            cell.width = Twips(width)


def format_table(table, widths):
    assert len(table.columns) == len(widths)
    set_table_widths(table, widths)
    set_borders(table)
    for row_index, row in enumerate(table.rows):
        tr_pr = row._tr.get_or_add_trPr()
        if tr_pr.find(qn("w:cantSplit")) is None:
            tr_pr.append(OxmlElement("w:cantSplit"))
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            if row_index == 0:
                set_shading(cell, GREEN)
            elif row_index % 2 == 0:
                set_shading(cell, "F3F7F2")
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(2)
                paragraph.paragraph_format.line_spacing = 1.16
                for run in paragraph.runs:
                    run.font.name = "Microsoft YaHei"
                    run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
                    run.font.size = Pt(9.5)
                    if row_index == 0:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)


def insert_paragraph_before(document, table, text, style=None, label=None):
    p = document.add_paragraph(style=style)
    table._element.addprevious(p._p)
    if label:
        r = p.add_run(label)
        r.bold = True
        r.font.color.rgb = RGBColor(47, 93, 58)
    r = p.add_run(text)
    r.font.name = "Microsoft YaHei"
    r._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    r.font.size = Pt(10.5)
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(4)
    return p


def convert_records(document, table, headers, title, fields):
    assert [c.text.strip() for c in table.rows[0].cells] == headers, "Unexpected table; inspect before changing"
    for row in table.rows[1:]:
        values = [c.text.strip() for c in row.cells]
        heading = title(values)
        p = insert_paragraph_before(document, table, heading, style="Readable Entry")
        p.paragraph_format.keep_with_next = True
        for field_index, (label, index) in enumerate(fields):
            if values[index]:
                detail = insert_paragraph_before(document, table, values[index], label=label)
                detail.paragraph_format.keep_with_next = field_index < len(fields) - 1
    table._element.getparent().remove(table._element)


def main():
    document = Document(DOCX)
    tables = list(document.tables)
    assert len(tables) in (6, 9), "Unexpected table count; inspect the document before running"
    if "Readable Entry" not in [style.name for style in document.styles]:
        style = document.styles.add_style("Readable Entry", WD_STYLE_TYPE.PARAGRAPH)
    else:
        style = document.styles["Readable Entry"]
    style.font.name = "Microsoft YaHei"
    style.font.size = Pt(12)
    style.font.bold = True
    style.font.color.rgb = RGBColor(47, 93, 58)
    style.paragraph_format.space_before = Pt(12)
    style.paragraph_format.space_after = Pt(4)

    if len(tables) == 9:
        convert_records(
            document, tables[1],
            ["段落", "场景", "玩家做什么", "教学 / 体验目标", "时长"],
            lambda v: f"{v[0]}  {v[1]}   ·   {v[4]}",
            [("玩家操作  ", 2), ("体验目标  ", 3)],
        )
        convert_records(
            document, tables[3],
            ["角色", "动画", "帧数（建议）", "依据参考图", "级别"],
            lambda v: f"{v[0]}   ·   {v[4]}",
            [("动作  ", 1), ("数量参考  ", 2), ("参考图  ", 3)],
        )
        convert_records(
            document, tables[4],
            ["场景", "图块 / 物件", "视差层", "概念参考", "级别"],
            lambda v: f"{v[0]}   ·   {v[4]}",
            [("图块与物件  ", 1), ("视差层  ", 2), ("概念参考  ", 3)],
        )

    for paragraph in document.paragraphs:
        if paragraph.style is not None and (
            paragraph.style.name == "Readable Entry"
            or paragraph.style.name.startswith("Heading")
        ):
            paragraph.paragraph_format.keep_with_next = True
        elif paragraph.text.startswith(("玩家操作  ", "动作  ", "数量参考  ", "图块与物件  ", "视差层  ")):
            paragraph.paragraph_format.keep_with_next = True

    assert len(document.tables) == 6
    for table, widths in zip(document.tables, (
        [1.12, 5.15],
        [1.50, 3.05, 1.72],
        [1.18, 4.38, 0.71],
        [1.18, 4.38, 0.71],
        [1.18, 2.93, 2.16],
        [1.60, 2.67, 2.00],
    )):
        format_table(table, widths)

    # The short extension table is a single idea. Keep it with its section
    # heading instead of leaving only its final rows on a mostly empty page.
    for row in document.tables[-1].rows[:-1]:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.keep_with_next = True

    document.save(DOCX)
    print(DOCX)


if __name__ == "__main__":
    main()
