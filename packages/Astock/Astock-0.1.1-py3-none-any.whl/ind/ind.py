

import mysqlFuns as mf
import datetime as dt
conn=mf.getConn()



def getXSfy():
    # 按申万一级行业，拆解各行业一季度的销售费用增长情况
    stocks  = mf.getMarketTrading(conn,dt.datetime(2021,12,1),dt.datetime(2021,12,31))
    data = mf.getFinance(conn, stocks.code.tolist(), dt.datetime.today(), "F12_1854", "income")
    data = data[data.reportPeriod.apply(lambda x: x.month) == 3]
    data.sort_values(by=["code", "reportPeriod", "reportDate"],ascending=[True, True, False],inplace=True)
    data.drop_duplicates(subset=['code','reportPeriod'],keep='first')
    data.set_index('code',inplace=True)
    sw = mf.getSwInd(conn, data.index.tolist(), dt.datetime.today())
    sw.set_index('code',inplace=True)
    data = data.join(sw)
    inddata = data.groupby(["sw_name", "reportPeriod"]).mean()
    inddata = inddata.groupby('sw_name').apply(lambda x:x/x.shift(1)) - 1 
    inddata.unstack().to_csv('result.csv',encoding='gbk')

def getZCFZL():
    # 按申万一级行业，拆解固定资产投资情况
    stocks  = mf.getMarketTrading(conn,dt.datetime(2021,12,1),dt.datetime(2021,12,31))
    