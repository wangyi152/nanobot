# -*- coding: utf-8 -*-
"""
整式乘法测试卷 PDF 生成器
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# 注册中文字体
try:
    pdfmetrics.registerFont(TTFont('SimSun', 'C:/Windows/Fonts/simsun.ttc'))
    pdfmetrics.registerFont(TTFont('SimHei', 'C:/Windows/Fonts/simhei.ttf'))
except:
    print("未找到中文字体，请确保系统有宋体/黑体字体")

def create_test_paper():
    # 创建 PDF 文档
    doc = SimpleDocTemplate(
        "整式乘法专项测试卷.pdf",
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    elements = []
    styles = getSampleStyleSheet()
    
    # 自定义样式
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontName='SimHei',
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=20
    )
    
    info_style = ParagraphStyle(
        'Info',
        parent=styles['Normal'],
        fontName='SimSun',
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=15
    )
    
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading2'],
        fontName='SimHei',
        fontSize=14,
        spaceAfter=10,
        spaceBefore=15
    )
    
    question_style = ParagraphStyle(
        'Question',
        parent=styles['Normal'],
        fontName='SimSun',
        fontSize=11,
        leading=18,
        spaceAfter=8
    )
    
    # 标题
    elements.append(Paragraph("整式乘法专项测试卷", title_style))
    elements.append(Paragraph("考试时间：90 分钟    满分：120 分", info_style))
    elements.append(Paragraph("班级：__________  姓名：__________  学号：__________  得分：__________", info_style))
    elements.append(Spacer(1, 0.5*cm))
    
    # 第一部分：选择题
    elements.append(Paragraph("一、选择题（每题 3 分，共 15 分）", heading_style))
    
    questions_1_5 = [
        "1. 下列计算正确的是（    ）<br/>A. 3x² · 4x³ = 12x⁶    B. (-2a³) · 5a⁴ = -10a⁷    C. 6m²n · 3mn² = 18m²n²    D. (-4x²y) · (-3xy³) = -12x³y⁴",
        "2. 计算 (2x-3)(3x+2) 的结果是（    ）<br/>A. 6x²-5x-6    B. 6x²+5x-6    C. 6x²-5x+6    D. 6x²-13x-6",
        "3. 若 (x+a)(x+b) = x²+5x+6，则 a+b 的值为（    ）<br/>A. 5    B. 6    C. -5    D. -6",
        "4. 计算 (2a+3b)² - (2a-3b)² 的结果是（    ）<br/>A. 8a²    B. 18b²    C. 24ab    D. 0",
        "5. 若 x²+kx+9 是完全平方式，则 k 的值为（    ）<br/>A. 6    B. -6    C. ±6    D. ±3"
    ]
    
    for q in questions_1_5:
        elements.append(Paragraph(q, question_style))
    
    elements.append(Spacer(1, 0.5*cm))
    
    # 第二部分：填空题
    elements.append(Paragraph("二、填空题（每题 4 分，共 20 分）", heading_style))
    
    questions_6_10 = [
        "6. 计算：(-3x²y³) · 4xy² = ______________",
        "7. 计算：(5a²-3b²)(5a²+3b²) = ______________",
        "8. 若 2ᵐ = 3，2ⁿ = 5，则 2²ᵐ⁺ⁿ = ______________",
        "9. 已知 a+b=5，ab=3，则 a²+b² = ______________",
        "10. 计算：(x+1)(x-1)(x²+1)(x⁴+1) = ______________"
    ]
    
    for q in questions_6_10:
        elements.append(Paragraph(q, question_style))
    
    elements.append(Spacer(1, 0.5*cm))
    
    # 第三部分：计算题
    elements.append(Paragraph("三、计算题（每题 6 分，共 48 分）", heading_style))
    
    questions_11_18 = [
        "11. (-2a²b)³ · (-¼ab²)",
        "12. 3x²y(2x²-3xy+4y²) - 2xy²(3x-4y)",
        "13. (2m-3n)(3m+2n) - (m+n)(2m-n)",
        "14. (x+2y-z)(x-2y+z)",
        "15. (2a-b)² + (a+2b)² - 5(a²+b²)",
        "16. [(x+2)(x-2)]² - (x²+4)²",
        "17. (x²+x+1)(x²-x+1) - (x⁴+x²+1)",
        "18. (2x+1)²(2x-1)² - (4x²-1)²"
    ]
    
    for q in questions_11_18:
        elements.append(Paragraph(q, question_style))
        elements.append(Spacer(1, 0.3*cm))
    
    # 分页
    elements.append(Spacer(1, 2*cm))
    doc.build(elements)
    
    # 第二页
    elements = []
    
    elements.append(Paragraph("三、计算题（续）", heading_style))
    
    # 第四部分：化简求值题
    elements.append(Paragraph("四、化简求值题（每题 7 分，共 21 分）", heading_style))
    
    questions_19_21 = [
        "19. 先化简，再求值：(2a+3b)² - (2a-3b)² + 12ab，其中 a=2，b=-1",
        "20. 先化简，再求值：[(x+y)² - (x-y)²] ÷ 4xy，其中 x=3，y=2",
        "21. 已知 x²-3x+1=0，求代数式 x² + 1/x² 的值"
    ]
    
    for q in questions_19_21:
        elements.append(Paragraph(q, question_style))
        elements.append(Spacer(1, 1*cm))
    
    # 第五部分：综合应用题
    elements.append(Paragraph("五、综合应用题（第 22 题 8 分，第 23 题 8 分，共 16 分）", heading_style))
    
    elements.append(Paragraph("22. 一块长方形土地的长为 (3a+2b) 米，宽为 (2a-b) 米，现计划在其中修建一个边长为 (a+b) 米的正方形花坛，其余部分种植草坪。", question_style))
    elements.append(Paragraph("(1) 求草坪的面积（用含 a、b 的代数式表示）；", question_style))
    elements.append(Paragraph("(2) 当 a=5，b=3 时，求草坪的实际面积。", question_style))
    elements.append(Spacer(1, 1.5*cm))
    
    elements.append(Paragraph("23. 观察下列等式：", question_style))
    elements.append(Paragraph("(x-1)(x+1) = x²-1", question_style))
    elements.append(Paragraph("(x-1)(x²+x+1) = x³-1", question_style))
    elements.append(Paragraph("(x-1)(x³+x²+x+1) = x⁴-1", question_style))
    elements.append(Paragraph("(1) 根据规律填空：(x-1)(xⁿ+xⁿ⁻¹+…+x+1) = ______________", question_style))
    elements.append(Paragraph("(2) 利用上述规律计算：2⁹⁹+2⁹⁸+…+2²+2+1", question_style))
    elements.append(Paragraph("(3) 若 x³+x²+x+1=0，求 x²⁰²⁶ 的值", question_style))
    
    elements.append(Spacer(1, 2*cm))
    elements.append(Paragraph("祝同学们考试顺利！🍀", ParagraphStyle('GoodLuck', parent=styles['Normal'], fontName='SimHei', fontSize=12, alignment=TA_CENTER)))
    
    doc.build(elements)
    print("PDF 生成成功！")

if __name__ == "__main__":
    create_test_paper()
