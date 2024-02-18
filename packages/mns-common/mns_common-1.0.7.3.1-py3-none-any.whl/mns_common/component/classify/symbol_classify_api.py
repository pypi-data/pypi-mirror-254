import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 16
project_path = file_path[0:end]
sys.path.append(project_path)
from mns_common.component.classify.classify_constant import stock_type_param
import mns_common.utils.data_frame_util as data_frame_util


# 深沪普通股票  选择 10cm涨幅的
def choose_sh_symbol(realtime_quotes_now):
    return realtime_quotes_now.loc[
        (realtime_quotes_now['classification'].isin(['S', 'H']))]


# 选择科创 创业板 20厘米的
def choose_kc_symbol(realtime_quotes_now):
    return realtime_quotes_now.loc[
        realtime_quotes_now['classification'].isin(['K', 'C'])]


# 选择北交所的 30厘米的
def choose_bjs_symbol(realtime_quotes_now):
    return realtime_quotes_now.loc[
        realtime_quotes_now['classification'].isin(['X'])]


# 新上市注册股票,不限制涨幅的
def choose_new_sub_c_symbol(realtime_quotes_now):
    return realtime_quotes_now.loc[realtime_quotes_now['name'].str.startswith('C')]


# 设置新股次新标记
def set_stock_type(real_time_quotes_now_init):
    if data_frame_util.is_empty(real_time_quotes_now_init):
        return None
    real_time_quotes_now = real_time_quotes_now_init.copy()
    real_time_quotes_now.loc[:, "stock_type"] = stock_type_param['normal_stock']
    # 上市五个交易日的股票
    real_time_quotes_now.loc[real_time_quotes_now['name'].str.startswith('C'), "stock_type"] = stock_type_param[
        'new_stock']

    real_time_quotes_now.loc[
        (real_time_quotes_now['stock_type'] != stock_type_param['new_stock'])
        & (real_time_quotes_now['diff_days'] <= stock_type_param['sub_stock_max_days']),
        "stock_type"] = stock_type_param['sub_stock']

    return real_time_quotes_now


# 新上市注册股票
def choose_new_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] == stock_type_param['new_stock']]

    return real_time_quotes_now


# 排除新股
def exclude_new_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] != stock_type_param['new_stock']]
    return real_time_quotes_now


# 选择次新
def choose_sub_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] == stock_type_param['sub_stock']]

    return real_time_quotes_now


# 排除次新
def exclude_sub_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] != stock_type_param['sub_stock']]
    return real_time_quotes_now


# 选择普通
def choose_normal_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] == stock_type_param['normal_stock']]

    return real_time_quotes_now


# 排除普通
def exclude_normal_stock(real_time_quotes_now):
    real_time_quotes_now = real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'] != stock_type_param['normal_stock']]
    return real_time_quotes_now


# 选择普通和次新
def choose_normal_and_sub_stock(real_time_quotes_now):
    return real_time_quotes_now.loc[
        real_time_quotes_now['stock_type'].isin([stock_type_param['normal_stock'],
                                                 stock_type_param['sub_stock']])]


# 选择科创 创业板 注册制以后主板 前五个交易日不设涨幅限制
def choose_kc_symbol_and_sub(realtime_quotes_now):
    real_time_quotes_now = realtime_quotes_now.loc[
        (realtime_quotes_now['classification'].isin(['K', 'C', 'X']))
        | (realtime_quotes_now['name'].str.startswith('C'))]
    return real_time_quotes_now
