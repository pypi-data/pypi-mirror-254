import os
import datetime as dt
import re
import mysqlFuns as mf

import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import os

#工具函数
def medWithNan(group):
    #group中位数，先用中位数填充nan值，再返回中位值
    d = pd.DataFrame(group)
    d.name = group.name
    d.fillna(value=d.median(skipna=True,numeric_only=True))
    return d.median()
#参数设置
stock_drvFin_year = 10

#多进程函数及设置
def deal(stock):
    return stock.getData()

#多线程函数及设置
def deal_threading(stock):
    stock.finData

mutliProcessMaxNum = os.cpu_count()-1
multiThreadMaxNum = os.cpu_count()*2
class SwInd():
    #缓存所有行业的SwInd对象，避免重复读取
    #使用new来获取对象
    swlist={}
    @staticmethod
    def new(code:str):
        #使用newSwInd来获得行业对象，而不要直接使用类创建，可避免重复创建
        code = code[:10] if len(code)>10 else code
        if code in SwInd.swlist.keys():
            return SwInd.swlist[code]
        else:
            return SwInd(code)
        
    def __init__(self,code:str):
        self.code=code[:10] if len(code)>10 else code
        tmpConn=mf.getConn()
        self.name = mf.getSwIndName(tmpConn,self.code)
        stocks = mf.getStocksInSwIndBetween(tmpConn,self.code)
        self._stocklist={}
        self._stockCodes=None
        self._indData=None
        if not stocks.empty:
            tmp = stocks[['code','name']]
            self._stockCodes = tmp[tmp['code'].str.match(re.compile(r'^[603]\d{5}'))]
            for code in self._stockCodes['code']:
                #use stock.new to create new stock object
                self._stocklist[code]=stock.new(code)
        mf.closeConn(tmpConn)
        if self.code not in SwInd.swlist.keys():
            SwInd.swlist[self.code] = self
    #填写所有个股财务数据
    @property
    def indData(self):
        if self._indData is not None:
            #防止外部修改
            return self._indData.copy()
        
        # 多线程提数据
        with ThreadPoolExecutor(min(multiThreadMaxNum,len(self._stocklist.values()))) as pool:
            pool.map(deal_threading,self._stocklist.values())

        tmp = None
        for stock in self._stocklist.values():
            if stock.finData.empty:
                continue
            if tmp is None:
                tmp = stock.finData
            else:
                tmp = pd.concat([tmp,stock.finData])
                
        if not tmp.empty:
            self._indData = tmp.groupby('reportPeriod')['reportType'].count()
            targetCols = tmp.columns[tmp.columns.tolist().index('reportType')+1:]

            self._indData = self._indData.rename('count').to_frame().join(tmp.groupby('reportPeriod')[targetCols].apply(medWithNan))
        #防止外部修改
        return self._indData.copy()
    
    @property
    def stocks(self):
        #防止外部修改
        return {'info': self._stockCodes.copy(), 'data':self._stocklist.copy()}

        

class stock():
    stocklist={}
    #使用new函数来获得对象，而不要直接使用函来创建，可避免重复创建
    @staticmethod
    def new(code:str):
        if code in stock.stocklist.keys():
            return stock.stocklist[code]
        else:
            return stock(code,True)
        
    def __init__(self, code:str, fromNew = False):
        #禁止外部使用stock()方法来创建新对象
        if not fromNew:
            raise Exception('请使用stock.new("code")来创建新的对象')
        #行业信息
        self.sw_industry={
            'sw1':{
                'code':'',
                'name':''
            },
            'sw2':{
                'code':'',
                'name':''
            },
            'sw3':{
                'code':'',
                'name':''
            },
        }
        #历史财务数据
        self._finData=None
        #行业信息
        self._swInd=None
        #财务数据列表
        self._finList = None
        self.code = code
        tmpConn = mf.getConn()
        #填写行业信息
        for i in range(3):
            data = mf.getSwInd(tmpConn,[code],dt.datetime.today(),level=i+1)
            if data.empty:
                continue
            else:
                self.sw_industry[f'sw{i+1}']['name']=data['sw_name'].iloc[0]
                self.sw_industry[f'sw{i+1}']['code']=data['sw_code'].iloc[0]
        #关闭接口
        mf.closeConn(tmpConn)
        stock.stocklist[code]=self
    
    #单独的计算数据函数，用于多进程计算
    def _getData(self):
        tmpConn = mf.getConn()
        valueList_drv = {
            'f56_5034':'ROIC',
            'f95_5034':'营业周期',
            'f41_5034':'毛利率',
            'f123_5034':'单季度毛利率',
            'f6_5034':'扣非净利润',
            'f69_5034':'资产负债率',
            'f45_5034':'销售费用占总营收',
            'f43_5034':'销售期间费用率',
            'f46_5034':'管理费用占总营收',
            'f79_5034':'流动比率',
            'f142_5034':'稀释每股收益同比增长率',
            'f153_5034':'总营收同比增长率',
            'f147_5034':'扣非同比增长率',
            'f96_5034':'存货周转天数',
            'f97_5034':'应收周转天数',
            'f70_5034':'权益乘数',
            'f28_5034':'每股净资产'
        }
        valueList_inc = {
            'f9_1854':'营业收入',
            'f80_1854':'基本每股收益',
            'f81_1854':'稀释每股收益',
            'f103_1854':'研发费用',
            'f12_1854':'销售费用',
            'f19_1854':'利息收入',
            'f13_1854':'管理费用'
        }
        valueList_bla = {
            'f9_1853':'货币资金',
            'f75_1853':'短期借款',
            'f94_1853':'长期借款',
            'f17_1853':'存货',
            'f39_1853':'商誉',
            'f18_1853':'消耗性生物资产',
            'f35_1853':'生产性生物资产',
            'f31_1853':'固定资产',
            'f140_1853':'股东权益',
        }
        data =  mf.getFinance(tmpConn,[self.code],dt.datetime.today(),\
                              ','.join(valueList_drv.keys()),table='derivative',\
                                years=stock_drvFin_year)
        if not data.empty:
            data.rename(columns=valueList_drv,inplace=True)
            
            tmp = mf.getFinance(tmpConn,[self.code],dt.datetime.today(),\
                                ','.join(valueList_inc.keys()),table='income',\
                                    years=stock_drvFin_year)
        
            tmp.rename(columns=valueList_inc,inplace=True)
            data = pd.merge(data,tmp.drop(['code','name','reportDate','reportType'],axis=1),how='inner',on='reportPeriod')
            
            tmp = mf.getFinance(tmpConn,[self.code],dt.datetime.today(),\
                                ','.join(valueList_bla.keys()),table='balance',\
                                    years=stock_drvFin_year)
            tmp.rename(columns=valueList_bla,inplace=True)
            data = pd.merge(data,tmp.drop(['code','name','reportDate','reportType'],axis=1),how='inner',on='reportPeriod')
            data = data.drop(['code','name'],axis=1)
        #关闭接口
        mf.closeConn(tmpConn)
        return data
    
    #设置_finData参数，用于返回多进程计算结果
    def _setData(self,data):
        self._finData = data.copy()

    @property
    def finData(self):
        if self._finData is not None:
            return self._finData
        self._finData = self._getData()
        return self._finData
        
    
    @property
    def rivals(self):
        #返回同行信息，info为代码和名称,data为每个个股的实例，可以直接使用
        tmp =  self.swInd.stocks
        data  = tmp['data']
        del data[self.code]
        info = tmp['info']
        info = info[info['code']!=self.code]
        return {'info':info,'data':data}

    #获取申万行业信息，默认是3级行业
    @property
    def swInd(self):
        if self._swInd is not None:
            return self._swInd
        self._swInd = SwInd.new(self.sw_industry['sw3']['code'])
        #关闭接口
        return self._swInd
    
    @property
    def finList(self):
        #提取字段名
        if self._finList:
            return self._finList
        data = self.finData
        self._finList = data.columns[data.columns.tolist().index('reportType')+1:].tolist()
        return self._finList
        
            
    def findBetter(self,accountList:list,asscentList:list=None,reportDateList:list=None):
        #根据某些字段和指定方向，查找行业中更好的公司
        #asscentList中为true值，则为寻找方向为大于等于
        #否则寻找方向为小于
        #reportDate可以指定报告期，否则为最近一期
        finList = self.finList
        for acc in accountList:
            if acc not in finList:
                print(f'{acc} 科目不存在，请修改条件或添加模块数据')
                return None
        if asscentList is None:
            print('没有指定排序顺序，默认以数值越大越优')
            asscentList = [True]* len(accountList)
        res_stock = {}
        res_info = self.rivals['info'].copy()
        
        stocklist = list(self.rivals['data'].values())
        stocklist.append(self)

        # 多线程提数据
        with ThreadPoolExecutor(min(multiThreadMaxNum,len(stocklist))) as pool:
            pool.map(deal_threading,stocklist)
        # #多进程刷数据
        # with mp.Pool(min(mutliProcessMaxNum,len(stocklist))) as pool:
        #     res = pool.map(deal,stocklist)
        # for stock,data in zip(stocklist,res):
        #     stock.setData(data)
        # del res
        for code,stock in zip(self.rivals['data'].keys(),self.rivals['data'].values()):
            data_a = stock.finData.copy()
            #这里有可能会出现空值
            if(data_a.empty):
                res_info = res_info[res_info['code']!=code]
                continue
            data_a = data_a.set_index('reportPeriod')[accountList]
            data_b = self.finData.copy().set_index('reportPeriod')[accountList]
            index = data_a.index.intersection(data_b.index)
            if reportDateList and len(index.intersection(reportDateList)):
                index = index.intersection(reportDateList)
            else:
                index = index[:1]
            data_a=data_a.loc[index]
            data_b=data_b.loc[index]
            if (data_a>=data_b).all().tolist() == asscentList:
                #记录个股数据（从零补充）
                res_stock[code]=stock
            else:
                #删除个股信息（从满删除）
                res_info = res_info[res_info['code']!=code]
        return {'info':res_info.reset_index(drop=True),'data':res_stock}
                    
    def getRival(self,code:str):
        #返回指定竞争对手，可以在筛选时改变比较标的
        if code in self.rivals['data'].keys():
            return self.rivals['data'][code]
        else:
            print(f'行业中不存在代码为{code}的公司，请检查')


        







        