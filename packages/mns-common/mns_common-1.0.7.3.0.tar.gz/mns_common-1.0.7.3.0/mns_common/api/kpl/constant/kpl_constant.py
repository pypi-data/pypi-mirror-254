import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)

# 开票啦 不选择的精选指数名称
NO_CHOOSE_KPL_INDEX_NAME = [
    '并购重组',
    '三季报增长',  # todo
    '实控人变更',
    '开板次新',
    '高送转',
    '举牌',
    '再融资',
    '股权转让',
    '专精特新',
    '分拆上市预期',
    '年报预增',
    '送转预期',
    '银行',
    '送转填权',
    '业绩增长',
    '中报增长',
    '科创板'
]

# 指数分类
FIRST_INDEX = "first_index"
SUB_INDEX = "sub_index"
