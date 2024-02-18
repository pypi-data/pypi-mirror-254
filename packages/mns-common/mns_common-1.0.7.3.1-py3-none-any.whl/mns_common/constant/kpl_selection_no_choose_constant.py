import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)
import pandas as pd


def get_exclude_kpl_selection():
    return pd.DataFrame([
        ['801250', '并购重组', '财务概念', 'first_index'],
        ['801573', '三季报增长', '财务概念', 'first_index'],
        ['801787', '实控人变更', '财务概念', 'first_index'],
        ['801104', '开板次新', '财务概念', 'first_index'],
        ['801284', '举牌', '财务概念', 'first_index'],
        ['801628', '资产管理', '财务概念', 'first_index'],
        ['801452', '再融资', '财务概念', 'first_index'],
        ['801008', '高送转', '财务概念', 'first_index'],
        ['801162', '超跌', '财务概念', 'first_index'],
        ['801273', '股权转让', '财务概念', 'first_index'],
        ['801522', '专精特新', '财务概念', 'first_index'],
        ['801450', '年报预增', '财务概念', 'first_index'],
        ['801382', '分拆上市预期', '财务概念', 'first_index'],
        ['801251', '送转预期', '财务概念', 'first_index'],
        ['801122', '壳资源', '财务概念', 'first_index'],
        ['801198', '送转填权', '财务概念', 'first_index'],
        ['801366', '业绩增长', '财务概念', 'first_index'],
        ['801572', '中报增长', '财务概念', 'first_index'],
        ['801574', '年报增长', '财务概念', 'first_index'],
        ['801574', '年报增长', '财务概念', 'first_index'],
        ['801631', '次新股', '财务概念', 'first_index'],

        ['801166', '上海国资改革', '宏观概念', 'first_index'],
        ['801033', '国企改革', '宏观概念', 'first_index'],
        ['801032', '深圳国资改革', '宏观概念', 'first_index'],
        ['801363', '黑龙江自贸区', '宏观概念', 'first_index'],
        ['801417', '天津自贸区', '宏观概念', 'first_index'],
        ['801209', '振兴东北', '宏观概念', 'first_index'],
        ['801376', '健康中国', '宏观概念', 'first_index'],
        ['801733', '中特估', '宏观概念', 'first_index'],
        ['801530', '中字头', '宏观概念', 'first_index'],

        ['801606', '成渝经济圈', '地域概念', 'first_index'],
        ['801182', '雄安新区', '地域概念', 'first_index'],
        ['801306', '深圳', '地域概念', 'first_index'],
        ['801132', '粤港澳', '地域概念', 'first_index'],
        ['801319', '福建', '地域概念', 'first_index'],
        ['801651', '湖南', '地域概念', 'first_index'],
        ['801115', '海南', '地域概念', 'first_index'],
        ['801407', '上海', '地域概念', 'first_index'],
        ['801310', '浙江', '地域概念', 'first_index'],
        ['801457', '武汉', '地域概念', 'first_index'],
        ['801211', '新疆', '地域概念', 'first_index'],
    ], columns=['symbol',
                'name',
                'exclude_reason',
                'index_class'
                ])


def get_exclude_kpl_selection_simple():
    return pd.DataFrame([
        ['801250', '并购重组', '财务概念', 'first_index'],
        ['801573', '三季报增长', '财务概念', 'first_index'],
        ['801787', '实控人变更', '财务概念', 'first_index'],
        ['801104', '开板次新', '财务概念', 'first_index'],
        ['801284', '举牌', '财务概念', 'first_index'],
        ['801628', '资产管理', '财务概念', 'first_index'],
        ['801452', '再融资', '财务概念', 'first_index'],
        ['801008', '高送转', '财务概念', 'first_index'],
        ['801162', '超跌', '财务概念', 'first_index'],
        ['801273', '股权转让', '财务概念', 'first_index'],
        ['801522', '专精特新', '财务概念', 'first_index'],
        ['801382', '分拆上市预期', '财务概念', 'first_index'],
        ['801251', '送转预期', '财务概念', 'first_index'],
        ['801122', '壳资源', '财务概念', 'first_index'],
        ['801198', '送转填权', '财务概念', 'first_index'],
        ['801631', '次新股', '财务概念', 'first_index'],

    ], columns=['symbol',
                'name',
                'exclude_reason',
                'index_class'
                ])


if __name__ == '__main__':
    df = get_exclude_kpl_selection()
    print(df)
