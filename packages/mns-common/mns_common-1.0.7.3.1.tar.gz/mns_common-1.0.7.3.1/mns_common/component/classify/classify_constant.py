import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)

# 按照上市时间对股票分类

# 股票类型
stock_type_param = {
    #  上市五个交易日的股票 名字以C开头
    "new_stock": "new",
    # 上市 5个交易日 -365 天的股票
    "sub_stock": "sub",
    # 365 到无穷天的股票
    "normal_stock": "normal",
    # 5-365天的股票
    'sub_stock_max_days': 365,
}


