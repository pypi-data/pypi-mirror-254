import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)
import re
from loguru import logger
import mns_common.utils.data_frame_util as data_frame_util
# question
# 必填，查询问句
#
# sort_key
# 非必填，指定用于排序的字段，值为返回结果的列名
#
# sort_order
# 非必填，排序规则，至为asc（升序）或desc（降序）
#
# page
# 非必填，查询的页号，默认为1
#
# perpage
# 非必填，每页数据条数，默认值100，由于问财做了数据限制，最大值为100，指定大于100的数值无效。
#
# loop
# 非必填，是否循环分页，返回多页合并数据。默认值为False，可以设置为True或具体数值。
#
# 当设置为True时，程序会一直循环到最后一页，返回全部数据。
#
# 当设置具体数值n时，循环请求n页，返回n页合并数据。


import mns_common.api.em.east_money_stock_api as east_money_stock_api
from mns_common.db.MongodbUtil import MongodbUtil
import pandas as pd
import mns_common.component.common_service_fun_api as common_service_fun_api
import mns_common.api.ths.ths_stock_api as ths_stock_api

mongodb_util = MongodbUtil('27017')


def get_zt_reason():
    zt_df = ths_stock_api.wei_cai_api('涨停', 'stock')
    zt_df.columns = ["code",
                     "name",
                     "now_price",
                     "chg",
                     "zt_tag",

                     "first_closure_time",
                     "last_closure_time",
                     "zt_detail",
                     "connected_boards_numbers",
                     "zt_reason",

                     "closure_volume",
                     "closure_funds",
                     "closure_funds_per_amount",
                     "closure_funds_per_flow_mv",
                     "frying_plates_numbers",

                     "flow_mv",
                     "statistics_detail",
                     "zt_type",
                     "market_code",
                     "symbol",
                     ]
    zt_df['statistics'] = zt_df['statistics_detail'].apply(convert_statistics)
    del zt_df['code']
    del zt_df['flow_mv']
    zt_df['zt_flag'] = True
    return zt_df


# 定义一个函数，用于将统计数据转换成相应的格式
def convert_statistics(stat):
    try:
        match = re.match(r'(\d+)天(\d+)板', stat)
        if match:
            n, m = map(int, match.groups())
            return f'{n}/{m}'
        elif stat == '首板涨停':
            return '1/1'
        else:
            return stat
    except BaseException as e:
        logger.error("转换出现异常:{},{}", e, stat)
        return '1/1'


def get_real_time_zt_info():
    zt_df = get_zt_reason()
    if data_frame_util.is_empty(zt_df):
        return None
    real_time_df = east_money_stock_api.get_real_time_quotes_all_stocks()

    zt_df = merge_high_chg(real_time_df, zt_df)

    symbol_list = list(zt_df['symbol'])
    zt_ream_time_data = real_time_df.loc[real_time_df['symbol'].isin(symbol_list)]
    zt_ream_time_data = zt_ream_time_data[[
        'symbol',
        'amount',
        'quantity_ratio',
        'high',
        'low',
        'high',
        'low',
        'open',
        'list_date',
        'exchange',
        'wei_bi',
        'flow_mv',
        'total_mv',
        'buy_1_num'
    ]]

    query_company = {'symbol': {"$in": symbol_list}}
    query_field = {'_id': 1,
                   "industry": 1,
                   "first_sw_industry": 1,
                   "first_industry_code": 1,
                   "second_sw_industry": 1,
                   "second_industry_code": 1,
                   "third_sw_industry": 1,
                   "third_industry_code": 1,
                   "ths_concept_name": 1,
                   "ths_concept_code": 1,
                   "ths_concept_sync_day": 1,
                   "em_industry": 1,
                   "company_type": 1,
                   "mv_circulation_ratio": 1,
                   "ths_concept_list_info": 1,
                   "kpl_plate_name": 1,
                   "kpl_plate_list_info": 1,
                   "diff_days": 1

                   }
    company_df = mongodb_util.find_query_data_choose_field('company_info', query_company, query_field)

    company_df = company_df.set_index(['_id'], drop=True)
    zt_df = zt_df.set_index(['symbol'], drop=True)
    zt_ream_time_data = zt_ream_time_data.set_index(['symbol'], drop=False)

    zt_df = pd.merge(zt_df, company_df, how='outer',
                     left_index=True, right_index=True)
    zt_df = pd.merge(zt_df, zt_ream_time_data, how='outer',
                     left_index=True, right_index=True)

    zt_df = common_service_fun_api.classify_symbol(zt_df)
    zt_df = common_service_fun_api.total_mv_classification(zt_df)

    zt_df = common_service_fun_api.symbol_amount_simple(zt_df)
    zt_df = common_service_fun_api.exclude_new_stock(zt_df)
    return zt_df


def merge_high_chg(real_time_df, zt_df):
    real_time_df_high_chg = real_time_df.loc[real_time_df['chg'] >= 9.5]
    if data_frame_util.is_empty(real_time_df_high_chg) and data_frame_util.is_empty(zt_df):
        return None

    if data_frame_util.is_not_empty(zt_df) and data_frame_util.is_empty(real_time_df_high_chg):
        return zt_df

    if data_frame_util.is_empty(zt_df) and data_frame_util.is_not_empty(real_time_df_high_chg):
        real_time_df_high_chg = real_time_df_high_chg[['symbol',
                                                       'name',
                                                       'now_price',
                                                       "flow_mv"]]
        return real_time_df_high_chg

    real_time_df_high_chg = real_time_df_high_chg.loc[~(real_time_df_high_chg['symbol'].isin(list(zt_df['symbol'])))]
    if data_frame_util.is_empty(real_time_df_high_chg):
        return zt_df

    real_time_df_high_chg = real_time_df_high_chg[['symbol',
                                                   'name',
                                                   'chg',
                                                   'now_price']]

    real_time_df_high_chg['connected_boards_numbers'] = 1

    real_time_df_high_chg['statistics_detail'] = '1/1'

    real_time_df_high_chg['zt_flag'] = False

    zt_df = pd.concat([zt_df, real_time_df_high_chg], ignore_index=True)
    zt_df = zt_df.fillna('0')
    return zt_df


if __name__ == '__main__':
    while True:
        res = get_zt_reason()
        print(res)
