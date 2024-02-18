import sys
import os

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 14
project_path = file_path[0:end]
sys.path.append(project_path)
import akshare as ak
from loguru import logger
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from py_mini_racer import py_mini_racer
from tqdm import tqdm
import json
import pywencai


def _get_js_path_ths(name: str = None, module_file: str = None) -> str:
    """
    获取 JS 文件的路径(从模块所在目录查找)
    :param name: 文件名
    :type name: str
    :param module_file: 模块路径
    :type module_file: str
    :return: 路径
    :rtype: str
    """
    module_folder = os.path.abspath(os.path.dirname(os.path.dirname(module_file)))
    module_json_path = os.path.join(module_folder, "api", name)
    return module_json_path


def _get_file_content_ths(file_name: str = "ase.min.js") -> str:
    """
    获取 JS 文件的内容
    :param file_name:  JS 文件名
    :type file_name: str
    :return: 文件内容
    :rtype: str
    """
    setting_file_name = file_name
    setting_file_path = _get_js_path_ths(setting_file_name, __file__)
    with open(setting_file_path) as f:
        file_data = f.read()
    return file_data


"""
    同花顺-板块-概念板块-概念 获取所有概念top50 概念列表
    http://q.10jqka.com.cn/gn/detail/code/301558/
    :return: 所有概念板块的名称和链接
    :rtype: pandas.DataFrame
"""


def ths_concept_index_top_50() -> pd.DataFrame:
    try:
        url = "http://data.10jqka.com.cn/funds/gnzjl/field/tradezdf/order/desc/page/1/ajax/1/free/1/"
        js_code = py_mini_racer.MiniRacer()
        js_content = _get_file_content_ths("ths.js")
        js_code.eval(js_content)
        v_code = js_code.call('v')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Cookie': f'v={v_code}'
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content.decode("gbk"), 'lxml')

        big_df = pd.DataFrame()

        soup.find('table', attrs={'class': 'm-table J-ajax-table'}).find('tbody')
        url_list = []
        for item in soup.find('table', attrs={'class': 'm-table J-ajax-table'}).find('tbody').find_all('tr'):
            inner_url = item.find_all("td")[1].find('a')['href']
            url_list.append(inner_url)
        temp_df = pd.read_html(r.text)[0]
        temp_df['网址'] = url_list
        big_df = big_df.append(temp_df, ignore_index=True)
        big_df['代码'] = big_df['网址'].str.split("/", expand=True).iloc[:, 6]
        big_df.rename(columns={
            "排名": "index",
            "代码": "concept_code",
            "行业": "concept_name",
            "行业指数": "now_price",
            "涨跌幅": "chg",
            "流入资金(亿)": "inflows",
            "流出资金(亿)": "outflows",
            "净额(亿)": "net_flows",
            "公司家数": "company_num",
            "领涨股": "first_up_symbol_name",
            "涨跌幅.1": "first_up_symbol_chg",
            "当前价(元)": "first_up_symbol_now_price",
            "网址": "url"
        }, inplace=True)
        big_df.loc[big_df['now_price'] == '-', 'now_price'] = 0
        big_df.loc[big_df['chg'] == '-', 'chg'] = 0
        big_df.loc[big_df['inflows'] == '-', 'inflows'] = 0
        big_df.loc[big_df['outflows'] == '-', 'outflows'] = 0
        big_df.loc[big_df['net_flows'] == '-', 'net_flows'] = 0
        big_df.loc[big_df['company_num'] == '-', 'company_num'] = 0
        big_df.loc[big_df['first_up_symbol_chg'] == '-', 'first_up_symbol_chg'] = 0
        big_df.loc[big_df['first_up_symbol_now_price'] == '-', 'first_up_symbol_now_price'] = 0
        big_df['chg'] = big_df['chg'].apply(
            lambda x: x.replace("%", "0"))
        big_df['first_up_symbol_chg'] = big_df['first_up_symbol_chg'].apply(
            lambda x: x.replace("%", "0"))
        big_df["now_price"] = pd.to_numeric(big_df["now_price"])
        big_df["chg"] = pd.to_numeric(big_df["chg"])
        big_df["inflows"] = pd.to_numeric(big_df["inflows"])
        big_df["outflows"] = pd.to_numeric(big_df["outflows"])
        big_df["net_flows"] = pd.to_numeric(big_df["net_flows"])
        big_df["company_num"] = pd.to_numeric(big_df["company_num"])
        big_df["first_up_symbol_chg"] = pd.to_numeric(big_df["first_up_symbol_chg"])
        big_df["first_up_symbol_now_price"] = pd.to_numeric(big_df["first_up_symbol_now_price"])
        return big_df
    except Exception as e:
        logger.error("获取同花顺概念指数异常:{}", e)
        return None


""" 有延迟 通过资金板块获取
    同花顺-板块-概念板块-概念 获取所有概念列表
    http://q.10jqka.com.cn/gn/detail/code/301558/
    :return: 所有概念板块的名称和链接
    :rtype: pandas.DataFrame
"""


def ths_concept_index() -> pd.DataFrame:
    try:
        url = "http://data.10jqka.com.cn/funds/gnzjl/field/tradezdf/order/desc/page/1/ajax/1/free/1/"
        js_code = py_mini_racer.MiniRacer()
        js_content = _get_file_content_ths("ths.js")
        js_code.eval(js_content)
        v_code = js_code.call('v')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Cookie': f'v={v_code}'
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content.decode("gbk"), 'lxml')
        total_page = soup.find('span', attrs={'class': 'page_info'}).text.split('/')[1]
        big_df = pd.DataFrame()
        for page in tqdm(range(1, int(total_page) + 1), leave=False):
            url = f"http://data.10jqka.com.cn/funds/gnzjl/field/tradezdf/order/desc/page/{page}/ajax/1/free/1/"

            js_code = py_mini_racer.MiniRacer()
            js_content = _get_file_content_ths("ths.js")
            js_code.eval(js_content)
            v_code = js_code.call('v')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'Cookie': f'v={v_code}'
            }
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content.decode("gbk"), 'lxml')
            soup.find('table', attrs={'class': 'm-table J-ajax-table'}).find('tbody')
            url_list = []
            for item in soup.find('table', attrs={'class': 'm-table J-ajax-table'}).find('tbody').find_all('tr'):
                inner_url = item.find_all("td")[1].find('a')['href']
                url_list.append(inner_url)
            temp_df = pd.read_html(r.text)[0]
            temp_df['网址'] = url_list
            big_df = big_df.append(temp_df, ignore_index=True)
        big_df['代码'] = big_df['网址'].str.split("/", expand=True).iloc[:, 6]
        big_df.rename(columns={
            "序号": "index",
            "代码": "concept_code",
            "行业": "concept_name",
            "行业指数": "now_price",
            "涨跌幅": "chg",
            "流入资金(亿)": "inflows",
            "流出资金(亿)": "outflows",
            "净额(亿)": "net_flows",
            "公司家数": "company_num",
            "领涨股": "first_up_symbol_name",
            "涨跌幅.1": "first_up_symbol_chg",
            "当前价(元)": "first_up_symbol_now_price",
            "网址": "url"
        }, inplace=True)
        big_df.loc[big_df['now_price'] == '-', 'now_price'] = 0
        big_df.loc[big_df['chg'] == '-', 'chg'] = 0
        big_df.loc[big_df['inflows'] == '-', 'inflows'] = 0
        big_df.loc[big_df['outflows'] == '-', 'outflows'] = 0
        big_df.loc[big_df['net_flows'] == '-', 'net_flows'] = 0
        big_df.loc[big_df['company_num'] == '-', 'company_num'] = 0
        big_df.loc[big_df['first_up_symbol_chg'] == '-', 'first_up_symbol_chg'] = 0
        big_df.loc[big_df['first_up_symbol_now_price'] == '-', 'first_up_symbol_now_price'] = 0
        big_df['chg'] = big_df['chg'].apply(
            lambda x: x.replace("%", "0"))
        big_df['first_up_symbol_chg'] = big_df['first_up_symbol_chg'].apply(
            lambda x: x.replace("%", "0"))
        big_df["now_price"] = pd.to_numeric(big_df["now_price"])
        big_df["chg"] = pd.to_numeric(big_df["chg"])
        big_df["inflows"] = pd.to_numeric(big_df["inflows"])
        big_df["outflows"] = pd.to_numeric(big_df["outflows"])
        big_df["net_flows"] = pd.to_numeric(big_df["net_flows"])
        big_df["company_num"] = pd.to_numeric(big_df["company_num"])
        big_df["first_up_symbol_chg"] = pd.to_numeric(big_df["first_up_symbol_chg"])
        big_df["first_up_symbol_now_price"] = pd.to_numeric(big_df["first_up_symbol_now_price"])
        return big_df
    except Exception as e:
        logger.error("获取同花顺概念指数异常:{}", e)
        return None


# 同步同花顺所有概念模块 通过概念板块
def stock_board_concept_name_ths():
    try:
        stock_board_industry_name_ths = ak.stock_board_concept_name_ths()
        stock_board_industry_name_ths = stock_board_industry_name_ths.rename(columns={"日期": "create_date",
                                                                                      "概念名称": "concept_name",
                                                                                      "成分股数量": "company_num",
                                                                                      "网址": "url",
                                                                                      "代码": "concept_code"})
        stock_board_industry_name_ths['_id'] = stock_board_industry_name_ths['concept_code']
        stock_board_industry_name_ths.create_date = stock_board_industry_name_ths.create_date.astype(str)
        return stock_board_industry_name_ths
    except Exception as e:
        logger.error("获取同花顺概念异常:{}", e)
        return None


"""
 概念板块的成份股 根据概念代码获取
"""


def ths_concept_symbol_list(symbol: str = "305794") -> pd.DataFrame:
    try:
        """
        http://q.10jqka.com.cn/gn/detail/code/305794/
        :param symbol: 行业板块或者概念板块的代码
        :type symbol: str
        :return: 概念板块的成份股
        :rtype: pandas.DataFrame
        """
        js_code = py_mini_racer.MiniRacer()
        js_content = _get_file_content_ths("ths.js")
        js_code.eval(js_content)
        v_code = js_code.call('v')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Cookie': f'v={v_code}'
        }
        url = f'http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/1/ajax/1/code/{symbol}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        try:
            page_num = int(soup.find_all('a', attrs={'class': 'changePage'})[-1]['page'])
        except IndexError as e:
            page_num = 1
        big_df = pd.DataFrame()
        for page in tqdm(range(1, page_num + 1), leave=False):
            v_code = js_code.call('v')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'Cookie': f'v={v_code}'
            }
            url = f'http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/{page}/ajax/1/code/{symbol}'
            r = requests.get(url, headers=headers)
            temp_df = pd.read_html(r.text)[0]
            big_df = big_df.append(temp_df, ignore_index=True)
        big_df.rename({
            "序号": "index",
            "代码": "symbol",
            "名称": "name",
            "现价": "now_price",
            "涨跌": "change",
            "量比": "quantity_ratio",
            "成交额": "amount",
            "流通股": "flow_shares",
            "流通市值": "flow_mv",
            "市盈率": "pe",
            "涨跌幅(%)": "chg",
            "涨速(%)": "speed_chg",
            "换手(%)": "exchange",
            "振幅(%)": "pct_chg",
        }, inplace=True, axis=1)
        del big_df['加自选']
        big_df = big_df[
            big_df["index"] != '暂无成份股数据']
        big_df['symbol'] = big_df['symbol'].astype(str).str.zfill(6)
        big_df.loc[big_df['now_price'] == '-', 'now_price'] = 0
        big_df.loc[big_df['change'] == '-', 'change'] = 0
        big_df.loc[big_df['quantity_ratio'] == '-', 'quantity_ratio'] = 0
        big_df.loc[big_df['amount'] == '-', 'amount'] = 0
        big_df.loc[big_df['flow_shares'] == '-', 'flow_shares'] = 0
        big_df.loc[big_df['flow_mv'] == '-', 'flow_mv'] = 0
        big_df.loc[big_df['pe'] == '-', 'pe'] = 0
        big_df.loc[big_df['chg'] == '-', 'chg'] = 0
        big_df.loc[big_df['speed_chg'] == '-', 'speed_chg'] = 0
        big_df.loc[big_df['exchange'] == '-', 'exchange'] = 0
        big_df.loc[big_df['pct_chg'] == '-', 'pct_chg'] = 0

        big_df.loc[big_df['now_price'] == '--', 'now_price'] = 0
        big_df.loc[big_df['change'] == '--', 'change'] = 0
        big_df.loc[big_df['quantity_ratio'] == '--', 'quantity_ratio'] = 0
        big_df.loc[big_df['amount'] == '--', 'amount'] = 0
        big_df.loc[big_df['flow_shares'] == '--', 'flow_shares'] = 0
        big_df.loc[big_df['flow_mv'] == '--', 'flow_mv'] = 0
        big_df.loc[big_df['pe'] == '--', 'pe'] = 0
        big_df.loc[big_df['chg'] == '--', 'chg'] = 0
        big_df.loc[big_df['speed_chg'] == '--', 'speed_chg'] = 0
        big_df.loc[big_df['exchange'] == '--', 'exchange'] = 0
        big_df.loc[big_df['pct_chg'] == '--', 'pct_chg'] = 0
        big_df.amount = big_df.amount.astype(str)
        big_df.flow_shares = big_df.flow_shares.astype(str)
        big_df.flow_mv = big_df.flow_mv.astype(str)
        big_df['amount'] = big_df['amount'].apply(
            lambda x: x.replace("亿", ""))
        big_df['flow_shares'] = big_df['flow_shares'].apply(
            lambda x: x.replace("亿", ""))
        big_df['flow_mv'] = big_df['flow_mv'].apply(
            lambda x: x.replace("亿", ""))

        big_df["now_price"] = pd.to_numeric(big_df["now_price"])

        big_df["change"] = pd.to_numeric(big_df["change"])

        big_df["quantity_ratio"] = pd.to_numeric(big_df["quantity_ratio"])
        big_df["amount"] = pd.to_numeric(big_df["amount"])

        big_df["flow_shares"] = pd.to_numeric(big_df["flow_shares"])

        big_df["flow_mv"] = pd.to_numeric(big_df["flow_mv"])

        big_df["pe"] = pd.to_numeric(big_df["pe"])

        big_df["chg"] = pd.to_numeric(big_df["chg"])

        big_df["speed_chg"] = pd.to_numeric(big_df["speed_chg"])

        big_df["exchange"] = pd.to_numeric(big_df["exchange"])

        big_df["pct_chg"] = pd.to_numeric(big_df["pct_chg"])

        return big_df
    except Exception as e:
        logger.error("获取同花顺概念列表信息异常:{}", e)
        return None


# 根据名称获取概念组成详细信息
def ths_concept_name_detail(concept_name):
    try:
        stock_board_concept_cons_ths_df = ak.stock_board_concept_cons_ths(
            symbol=concept_name)
        stock_board_concept_cons_ths_df.rename(columns={"序号": "index",
                                                        "代码": "symbol",
                                                        "名称": "name",
                                                        "现价": "now_price",
                                                        "涨跌幅": "chg",
                                                        "涨跌": "change",
                                                        "涨速": "r_increase",
                                                        "换手": "exchange",
                                                        "量比": "q_ratio",
                                                        "振幅": "pct_chg",
                                                        "成交额": "amount",
                                                        "流通股": "tradable_shares",
                                                        "流通市值": "market_value",
                                                        "市盈率": "pe"
                                                        }, inplace=True)
        stock_board_concept_cons_ths_df = stock_board_concept_cons_ths_df[
            stock_board_concept_cons_ths_df["index"] != '暂无成份股数据']
        stock_board_concept_cons_ths_df.chg = stock_board_concept_cons_ths_df.chg.astype(str)
        stock_board_concept_cons_ths_df['chg'] = stock_board_concept_cons_ths_df['chg'].apply(
            lambda x: x.replace("--", "0"))
        stock_board_concept_cons_ths_df.chg = stock_board_concept_cons_ths_df.chg.astype(float)
        return stock_board_concept_cons_ths_df
    except Exception as e:
        logger.error("获取同花顺概念详细信息异常:{}", e)
        return None


def ths_stock_concept(code):
    try:
        stock_board_cons_ths_df = ak.stock_board_cons_ths(symbol=code)
        if stock_board_cons_ths_df is None:
            return
        stock_board_cons_ths_df.rename(columns={"序号": "index",
                                                "代码": "symbol",
                                                "名称": "name",
                                                "现价": "now_price",
                                                "涨跌幅": "chg",
                                                "涨跌": "change",
                                                "涨速": "r_increase",
                                                "换手": "exchange",
                                                "量比": "q_ratio",
                                                "振幅": "pct_chg",
                                                "成交额": "amount",
                                                "流通股": "tradable_shares",
                                                "流通市值": "flow_mv",
                                                "市盈率": "pe"
                                                }, inplace=True)
        stock_board_cons_ths_df = stock_board_cons_ths_df[
            stock_board_cons_ths_df["index"] != '暂无成份股数据']

        if stock_board_cons_ths_df is None or stock_board_cons_ths_df.shape[0] == 0:
            return
        length = len(list(stock_board_cons_ths_df))
        stock_board_cons_ths_df.insert(length, 'concept_code', code)

        stock_board_cons_ths_df['amount'] = stock_board_cons_ths_df['amount'].apply(
            lambda x: pd.to_numeric(x.replace('亿', ''), errors="coerce"))

        stock_board_cons_ths_df['tradable_shares'] = stock_board_cons_ths_df['tradable_shares'].apply(
            lambda x: pd.to_numeric(x.replace('亿', ''), errors="coerce"))

        stock_board_cons_ths_df['flow_mv'] = stock_board_cons_ths_df['flow_mv'].apply(
            lambda x: pd.to_numeric(x.replace('亿', ''), errors="coerce"))

        return stock_board_cons_ths_df
        logger.info("同步概念代码数据:{}", code)
    except BaseException as e:
        logger.error("获取详情异常:{},异常信息:{}", code, e)


def get_company_info_detail(symbol: str = "305794") -> pd.DataFrame:
    try:
        url = f'https://basic.10jqka.com.cn/basicapi/company_info/merge_info/v1/base_info/?code={symbol}&market=33&type=stock'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Host': 'basic.10jqka.com.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'v=A0CN8EBXN21LtMtpV6ldAxf6Ec8XySSbxq14l7rRDNvuNe77Ytn0Ixa9SDQJ',
            'Upgrade-Insecure-Requests': '1',

        }
        r = requests.get(url, headers=headers)
        data_json = r.json()
        status_code = data_json['status_code']
        status_msg = data_json['status_msg']
        if status_code != 0 or status_msg != 'success':
            logger.error("获取symbol公司详细信息异常:{}", symbol)
        if len(data_json['data']['industry']) == 0:
            return None
        data_df = pd.DataFrame(data_json['data']['industry'], index=[0])
        data_df = data_df[[
            'hy',
            'hycode',
            'hy2',
            'hy2code',
            'hy3',
            'hy3code',
        ]]

        business_nature = data_json['data']['business_nature']
        name = data_json['data']['code_name']
        base_business = data_json['data']['base_business']
        address = data_json['data']['address']
        data_df['symbol'] = symbol
        data_df['name'] = name

        data_df['business_nature'] = business_nature

        if len(data_json['data']['management']['holder_controller']) > 0:
            holder_controller = pd.DataFrame(data_json['data']['management']['holder_controller'])
            holder_controller_name = str(list(holder_controller['name'])).strip('[').strip(']').replace("'", "")
            holder_controller_rate = holder_controller['rate']
            data_df['holder_controller_name'] = holder_controller_name
            data_df['holder_controller_rate'] = sum(holder_controller_rate)
        else:
            data_df['holder_controller_name'] = '暂无'
            data_df['holder_controller_rate'] = 0
        if len(data_json['data']['management']['final_controller']) > 0:
            final_controller = pd.DataFrame(data_json['data']['management']['final_controller'])
            final_controller_name = str(list(final_controller['name'])).strip('[').strip(']').replace("'", "")
            final_controller_rate = sum(final_controller['rate'])
            data_df['final_controller_name'] = final_controller_name
            data_df['final_controller_rate'] = final_controller_rate
        else:
            data_df['final_controller_name'] = '暂无'
            data_df['final_controller_rate'] = 0
        if len(data_json['data']['management']['actual_controller']) > 0:
            actual_controller = pd.DataFrame(data_json['data']['management']['actual_controller'])
            actual_controller_name = str(list(actual_controller['name'])).strip('[').strip(']').replace("'", "")
            actual_controller_rate = sum(actual_controller['rate'])
            data_df['actual_controller_name'] = actual_controller_name
            data_df['actual_controller_rate'] = actual_controller_rate
        else:
            data_df['actual_controller_name'] = '暂无'
            data_df['actual_controller_rate'] = 0

        data_df['base_business'] = base_business
        data_df['address'] = address
        market_id = data_json['data']['market_id']
        data_df['market_id'] = market_id

        return data_df
    except BaseException as e:
        logger.error("获取symbol公司详细信息异常:{},{}", symbol, e)


# 获取股票基本信息
# https://basic.10jqka.com.cn/mobile/301016/companyprofilen.html?showtab=1&broker=anelicaiapp
def get_company_info(symbol: str = "305794") -> pd.DataFrame:
    try:
        url = f"http://basic.10jqka.com.cn/mobile/{symbol}/companyprofilen.html?broker=pingan"
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iOS AYLCAPP/9.1.2.0/h4526a24eb9445522492fd64caae11b1f scheme/anelicaiapp deviceinfo/I|9.1.2.0|NA|h4526a24eb9445522492fd64caae11b1f pastheme/0",
            "Cookie": "ps_login_app_name=AYLCAPP;ps_login_token_id=N_C993F777ACC500B354C762A2627A8862348FC8163799A08EBEB2301C28A2135D220475787D0E81425C1134E15D8CC8761D639FEDBD46C00FE8EA6482C1E42D9801B19918FB3F5C34;ps_login_union_id=edc29089a2b64e3882062297030a0386;PAS.CURRENTUNIONID=edc29089a2b64e3882062297030a0386"
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content.decode("utf-8"), 'lxml')
        soup.find('table', attrs={'class': 'leveldatail-tab'}).find_all('tr')
        temp_df = pd.read_html(r.content)[0]
        temp_df = temp_df.T
        temp_df = temp_df.iloc[1:2]
        temp_df.rename(columns={
            0: "name",
            1: "former_name",
            2: "registered_address",
            3: "chairman",
            4: "board_secretary",
            5: "main_business",
            6: "company_type",
            7: "controlling_shareholder",
            8: "actual_controller",
            9: "ultimate_controller",
            10: "list_date",
            11: "issue_price",
            12: "number_workers",
            13: "tel",
            14: "url",
            15: "email"
        }, inplace=True)

        return temp_df
    except BaseException:
        logger.error("获取symbol控制人基本信息异常:{}", symbol)


# 获取概念名称信息
def get_concept_name(symbol: str = "881121") -> pd.DataFrame:
    try:
        url = f"http://q.10jqka.com.cn/thshy/detail/code/{symbol}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iOS AYLCAPP/9.1.2.0/h4526a24eb9445522492fd64caae11b1f scheme/anelicaiapp deviceinfo/I|9.1.2.0|NA|h4526a24eb9445522492fd64caae11b1f pastheme/0",
            "Cookie": "ps_login_app_name=AYLCAPP;ps_login_token_id=N_C993F777ACC500B354C762A2627A8862348FC8163799A08EBEB2301C28A2135D220475787D0E81425C1134E15D8CC8761D639FEDBD46C00FE8EA6482C1E42D9801B19918FB3F5C34;ps_login_union_id=edc29089a2b64e3882062297030a0386;PAS.CURRENTUNIONID=edc29089a2b64e3882062297030a0386"
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content.decode("gbk"), 'lxml')
        temp_df = soup.find(attrs={'class': 'board-hq'}).find_all('h3')
        temp_df = str(temp_df)
        startIndex = temp_df.index('[<h3>')
        if startIndex >= 0:
            startIndex += len('[<h3>')
        endIndex = temp_df.index('<span>')
        return temp_df[startIndex:endIndex]

    except BaseException:
        logger.error("获取symbol基本信息异常:{}", symbol)


# 获取概念资金流入信息
def get_stock_fund_flow():
    stock_fund_flow_concept_df = ak.stock_fund_flow_concept(symbol="即时")
    stock_fund_flow_concept_df = stock_fund_flow_concept_df.rename(columns={
        "序号": "index",
        "行业": "concept_name",
        "行业指数": "concept_index",
        "行业-涨跌幅": "concept_chg",
        "流入资金": "inflows",
        "流出资金": "outflow",
        "净额": "netflow",
        "公司家数": "company_num",
        "领涨股": "leading_stock",
        "领涨股-涨跌幅": "leading_chg",
        "当前价": "now_price",
    })
    return stock_fund_flow_concept_df


# 获取同花顺新概念信息--APP 端接口 容易被封
def get_new_concept_list_app(symbol: str = "886019") -> pd.DataFrame:
    try:
        url = f'https://d.10jqka.com.cn/v2/blockrank/{symbol}/199112/d1000.js'
        headers = {

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'v=A2A7Vv5CF9c_javTJ4_ZJx3_N283aUQt5k2YN9pxLHsO1Q5bgnkUwzZdaMEp; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1668578108',
            'Host': 'd.10jqka.com.cn',
            'If-Modified-Since': "Wed, 16 Nov 2022 09:31:32 GMT",
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:106.0) Gecko/20100101 Firefox/106.0",

        }
        r = requests.get(url, headers=headers)
        result = r.content.decode("unicode-escape")

        startIndex = result.index('{"block"')
        endIndex = result.index('}]}')

        result = result[startIndex:endIndex + 3]

        data_json = json.loads(result)
        block = data_json['block']
        items = data_json['items']

        items_df = pd.DataFrame(items)
        items_df = items_df.rename(columns={
            "5": "symbol",
            "199112": "chg",
            "264648": "change",
            "2034120": "pe",
            "3475914": "flow_mv",
            "3541450": "total_mv",
            "1968584": "exchange",
            "10": "now_price",
            "7": "open",
            "8": "high",
            "9": "low",
            "13": "volume",
            "19": "amount",
            "55": "name",
            "6": "last_day_price",

        })
        items_df['concept_code'] = symbol
        items_df['concept_name'] = block['name']
        items_df['index'] = 0
        items_df['pct_chg'] = 0
        items_df['q_ratio'] = 0
        items_df = items_df[
            [
                'index',
                'symbol',
                'name',
                'now_price',
                'chg',
                'change',
                'exchange',
                'q_ratio',
                'pct_chg',
                'amount',
                'flow_mv',
                'total_mv',
                'pe',
                'concept_code',
                'concept_name',
            ]
        ]
        return items_df
    except BaseException:
        logger.error("获取新概念信息异常:{}", symbol)
        return None


# 获取同花顺APP 端搜索概念结果
def get_new_concept_code_app(symbol: str = "886019"):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'v=A2A7Vv5CF9c_javTJ4_ZJx3_N283aUQt5k2YN9pxLHsO1Q5bgnkUwzZdaMEp; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1668578108',
        'Host': 'd.10jqka.com.cn',
        'If-Modified-Since': "Wed, 16 Nov 2022 09:31:32 GMT",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:106.0) Gecko/20100101 Firefox/106.0",

    }
    # userId 随便写 https://dict.hexin.cn:9531/stocks?pattern=886019&isauto=1&associate=1&pl=i&isrealcode=1&json=1&br=sc&style=1&userid=656258250&markettype=2	200	GET	dict.hexin.cn:9531	/stocks?pattern=886019&isauto=1&associate=1&pl=i&isrealcode=1&json=1&br=sc&style=1&userid=656258250&markettype=2
    url = f'https://dict.hexin.cn:9531/stocks?pattern={symbol}&isauto=1&associate=1&pl=i&isrealcode=1&json=1&br=sc&style=1&userid=603985000&markettype=2'

    try:
        r = requests.get(url, headers)
        data_json = r.json()
        type = data_json['type']
        if type == '0':

            body_list = data_json['data']['body']
            concept_code = body_list[0][0]
            concept_name = body_list[0][1]
            concept = {
                'concept_code': concept_code,
                'concept_name': concept_name
            }

            return pd.DataFrame([concept], index=[0])

            return concept
        else:
            return None

    except BaseException as e:
        logger.error("获取新概念信息异常:{}", e)
        return None


# 获取单个股票新增概念  https://basic.10jqka.com.cn/basicph/briefinfo.html#/concept?broker=anelicaiapp&showtab=1&code=301016&code_name=%E9%9B%B7%E5%B0%94%E4%BC%9F&market_id=33
def get_symbol_add_new_concept(symbol: str = "305794") -> pd.DataFrame:
    try:
        url = f"http://basic.10jqka.com.cn/api/stockph/conceptdetail/{symbol}"
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iOS AYLCAPP/9.1.2.0/h4526a24eb9445522492fd64caae11b1f scheme/anelicaiapp deviceinfo/I|9.1.2.0|NA|h4526a24eb9445522492fd64caae11b1f pastheme/0",
            "Cookie": "ps_login_app_name=AYLCAPP;ps_login_token_id=N_C993F777ACC500B354C762A2627A8862348FC8163799A08EBEB2301C28A2135D220475787D0E81425C1134E15D8CC8761D639FEDBD46C00FE8EA6482C1E42D9801B19918FB3F5C34;ps_login_union_id=edc29089a2b64e3882062297030a0386;PAS.CURRENTUNIONID=edc29089a2b64e3882062297030a0386"
        }
        r = requests.get(url, headers=headers)
        data_json = r.json()
        data_concept = data_json['data']
        return data_concept
    except BaseException:
        logger.error("获取symbol概念信息异常:{}", symbol)


# query: 个股新增概念
# urp_sort_way: desc
# urp_sort_index: 最新涨跌幅
# page: 2
# perpage: 50
# addheaderindexes:
# condition: [{"dateText":"","indexName":"所属概念","indexProperties":[],"ci":false,"source":"text2sql","type":"index","indexPropertiesMap":{},"reportType":"null","ciChunk":"个股新增概念","score":0.0,"createBy":"cache","chunkedResult":"个股新增概念","uiText":"所属概念","valueType":"_所属概念","domain":"abs_股票领域","sonSize":0,"logid":"78951d1a2de43d989afb6f5fff55538f","order":0}]
# codelist:
# indexnamelimit:
# logid: 78951d1a2de43d989afb6f5fff55538f
# ret: json_all
# sessionid: 78951d1a2de43d989afb6f5fff55538f
# source: Ths_iwencai_Xuangu
# date_range[0]: 20231031
# iwc_token: 0ac9665916987651304637922
# urp_use_sort: 1
# user_id: Ths_iwencai_Xuangu_xqei21psb40ujl9i60sjfv752bkkumeq
# uuids[0]: 24087
# query_type: stock
# comp_id: 6836372
# business_cat: soniu
# uuid: 24087
def ths_concept_wen_cai(str_day, page_number):
    try:
        # 请求头信息
        headers = {
            "Host": "www.iwencai.com",
            "Connection": "keep-alive",
            "Content-Length": "1326",
            "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
            "Pragma": "no-cache",
            "hexin-v": "AzR_iz347VCrfXnqX7tBEAuEBfmjDUzPmj3sFs6CwAxDFdon9h0oh-pBvO8d",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json, text/plain, */*",
            "Cache-control": "no-cache",
            "sec-ch-ua-platform": "\"Windows\"",
            "Origin": "https://www.iwencai.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.iwencai.com/unifiedwap/result?w=%E4%B8%AA%E8%82%A1%E6%96%B0%E5%A2%9E%E6%A6%82%E5%BF%B5",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "other_uid=Ths_iwencai_Xuangu_xqei21psb40ujl9i60sjfv752bkkumeq; ta_random_userid=zw66u7re6z; cid=78ed13c5d7b1b7d572f3b515b3dd9f7a1694788715; v=AzR_iz347VCrfXnqX7tBEAuEBfmjDUzPmj3sFs6CwAxDFdon9h0oh-pBvO8d"
        }

        # 请求体数据
        data = {
            "query": "个股新增概念",
            "urp_sort_way": "desc",
            "urp_sort_index": "最新涨跌幅",
            "page": page_number,
            "perpage": "50",
            "addheaderindexes": "",
            "condition": "[{\"dateText\":\"\",\"indexName\":\"所属概念\",\"indexProperties\":[],\"ci\":false,\"source\":\"text2sql\",\"type\":\"index\",\"indexPropertiesMap\":{},\"reportType\":\"null\",\"ciChunk\":\"个股新增概念\",\"score\":0.0,\"createBy\":\"cache\",\"chunkedResult\":\"个股新增概念\",\"uiText\":\"所属概念\",\"valueType\":\"_所属概念\",\"domain\":\"abs_股票领域\",\"sonSize\":0,\"logid\":\"78951d1a2de43d989afb6f5fff55538f\",\"order\":0}]",
            "codelist": "",
            "indexnamelimit": "",
            "logid": "78951d1a2de43d989afb6f5fff55538f",
            "ret": "json_all",
            "sessionid": "78951d1a2de43d989afb6f5fff55538f",
            "source": "Ths_iwencai_Xuangu",
            "date_range[0]": str_day,
            "iwc_token": "0ac9665916987651304637922",
            "urp_use_sort": "1",
            "user_id": "Ths_iwencai_Xuangu_xqei21psb40ujl9i60sjfv752bkkumeq",
            "uuids[0]": "24087",
            "query_type": "stock",
            "comp_id": "6836372",
            "business_cat": "soniu",
            "uuid": "24087"
        }

        # 发送POST请求
        url = "https://www.iwencai.com/gateway/urp/v7/landing/getDataList"
        response = requests.post(url, headers=headers, data=data)
        # 输出响应内容
        data_json = response.json()
        data_stock = data_json['answer']['components'][0]['data']['datas']
        data_stock_list = pd.DataFrame(data_stock)
        return data_stock_list
    except BaseException:
        logger.error("同步问财信息异常:{}", str_day, page_number)


# https://github.com/zsrl/pywencai 文档
# stock	股票
# zhishu	指数
# fund	基金
# hkstock	港股
# usstock	美股
# threeboard	新三板
# conbond	可转债
# insurance	保险
# futures	期货
# lccp	理财
# foreign_exchange	外汇
def wei_cai_api(question, q_type):
    response = pywencai.get(question=question, loop=True, query_type=q_type)
    return response


def get_concept_index():
    concept_df = wei_cai_api('同花顺概念指数', 'zhishu')
    concept_df.columns = ["code",
                          "concept_name",
                          "price",
                          "chg",
                          "detail",
                          "market_code",
                          "concept_code"]
    return concept_df


if __name__ == '__main__':
    df = ths_stock_concept('885598')
    print(df)
    # while True:
    #     concept_test()
    # company_info = get_concept_name('881121')
    # print(company_info)
    # new_concept_symbol_list = ths_stock_concept('881121')
    # print(new_concept_symbol_list)
    #
    # stock_fund_flow_concept_df = get_stock_fund_flow()
    # print(stock_fund_flow_concept_df)
    # df = get_company_info_detail("300085")
    # print(df)
    # while True:
    #     new_concept_code = get_new_concept_code_app('886026')
    #     new_concept_symbol_list = get_new_concept_list_app('886026')
    #     logger.info(new_concept_symbol_list)
