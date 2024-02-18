import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)
# 大单同步表
BIG_DEAL_NAME = "ths_big_deal_fund"
# 大单选择表
BIG_DEAL_CHOOSE_NAME = "big_deal_fund_choose"
# 实时行情表
REAL_TIME_QUOTES_NOW = 'realtime_quotes_now'
# 当前实时涨停表
TODAY_ZT_POOL = 'today_zt_pool'
# 集合竞价表
CALL_AUCTION_DB_NAME = 'call_auction_signal'
# 实时竞价表
CALL_AUCTION_DB_NAME_REAL_TIME = 'call_auction_signal_realtime'
# 涨停打板表
NOW_TIME_ZT_DA_BAN = 'now_time_zt_da_ban'
# 开盘啦精选指数表
KPL_BEST_CHOOSE_INDEX = 'kpl_best_choose_index'
# 开盘啦详细组成
KPL_BEST_CHOOSE_INDEX_DETAIL = "kpl_best_choose_index_detail"

# 同花顺概念表
THS_CONCEPT_LIST = "ths_concept_list"

# 同花顺概念详情表
THS_STOCK_CONCEPT_DETAIL = "ths_stock_concept_detail"
# 今日排除买入股票
TODAY_EXCLUDE_STOCK = "today_exclude_stocks"
# 今日买入股票
BUY_STOCK_NAME = 'trade_stocks'
#  COMPANY_INFO
COMPANY_INFO = 'company_info'
# TODAY_NEW_CONCEPT_LIST
TODAY_NEW_CONCEPT_LIST = 'today_new_concept_list'
