# 获取股票的每日交易信息作为分析基础
# 导入JQData库
from jqdatasdk import *
import pandas as pd

# ID是申请时所填写的手机号；Password为聚宽官网登录密码
auth(ID,Password) 

# 获取HS300每日收盘价
#  field的范围['open', 'close', 'high', 'low', 'volume', 'money', 'avg', 'high_limit', 'low_limit', 'pre_close', 'paused', 'factor', 'price', 'open_interest']
stocks = {
    "沪深300": "000300",
    "洛阳钼业": "603993",
    "中国重工": "601989",
    "中国银行": "601988",
    "贵州茅台": "600519"
}
for v in stocks.values():
    s = '{}.XSHG'.format(v)
    df = get_price(s, start_date='2005-01-01', end_date='2020-10-31', frequency='daily', fields=['open','close','high','low'], skip_paused=False, fq='pre')
    df.to_csv(s)
