import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 7
project_path = file_path[0:end]
sys.path.append(project_path)
import mns_common.api.akshare.stock_bid_ask_api as stock_bid_ask_api


# 获取最新价格
def get_new_buy_price(symbol):
    stock_bid_ask_df = stock_bid_ask_api.stock_bid_ask_em(symbol)
    sell_5 = list(stock_bid_ask_df['sell_5'])[0]
    if sell_5 != 0:
        return sell_5
    sell_4 = list(stock_bid_ask_df['sell_4'])[0]
    if sell_4 != 0:
        return sell_4

    sell_3 = list(stock_bid_ask_df['sell_4'])[0]
    if sell_3 != 0:
        return sell_4

    sell_2 = list(stock_bid_ask_df['sell_2'])[0]
    if sell_2 != 0:
        return sell_2

    sell_1 = list(stock_bid_ask_df['sell_1'])[0]
    if sell_1 != 0:
        return sell_1
    # 打板价格
    buy_1 = list(stock_bid_ask_df['buy_1'])[0]
    if buy_1 != 0:
        return buy_1


if __name__ == '__main__':
    price = get_new_buy_price('002903')
    print(price)
