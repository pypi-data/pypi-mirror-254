#Version 1.0.29

#修改记录
#1.0.4
#---------------------
#增加提取指数权重功能

#1.0.5
#---------------------
#增加个股日收益率序列功能

#1.0.6
#---------------------
#增加getStockReturnsExactdate函数
#增加getIndexReturnsExactdate函数
#exactdate类函数要求起始日期要精准匹配，不会自动缩小范围到有数据的日期

#1.0.7
#---------------------
#增加getMarketTradingCode函数
#增加getIndexWeightBetween函数
#getStockPrice 函数返回数据 更改

#1.0.8
#---------------------
#更改getMarketTradingCode函数,加上内存表取数据
#memtables quote_mem  增加 'f8_1425', 'f9_1425'两列。

#1.0.9
#---------------------
# getMarketTradingCode 加上 MemtablesTablename

#1.0.10
#----------------------------
#修改getMarketTradingCode函数，将opdate最早日期限制在2013年之后，避免提取早期清单为空的现象

#1.0.11
#----------------------------
#增加提取综合指数和申万指数固定周期收益率函数

#1.0.12
#----------------------------
#增加交易日历提取功能函数

#1.0.13
#----------------------------
#增加halfLifeWeight半衰期功能函数

#1.0.14
#----------------------------
#增加获取每周任意交易日（遇节假日往后延迟）的功能函数

#1.0.15
#----------------------------
#增加获取factor的功能函数，支持Barra/machine/alpha101/artificial

#1.0.16
#----------------------------
#增加获取TTM_data的功能函数

#1.0.17
#----------------------------
#更正getIndexWeight中SQL语句的BUG

#1.0.18
#---------------------------
#增加getIndexQuoteBetween，提取综合指数价格序列 

#1.0.19
#---------------------------
#更正getIndexQuoteBetween，价格序列提取后需要排序去重

#1.0.20
#----------------------------
#增加getCalendarDB函数，从数据库中提取日期序列

#1.0.21
#----------------------------
#getConn函数中增加pool_recycle参数，避免长时间计算导致接口失效

#1.0.22
#---------------------------
# 修改getFinance函数，使其支持财务衍生表derivative的查询

#1.0.23
#---------------------------
#增加getStocksInSwIndBetween函数，获取在指定时间区间内，申万行业个股名单
#增加getSwIndName函数，根据sw行业代码获取行业名称

#1.0.24
#---------------------------
#增加getStockDB函数，获取在指定时间区间内个股名单
#修改getMarketTradingCode函数，返回code_list

#1.0.25
#---------------------------
#增加fillDate函数，刷新trade_date_mem 内存表

#1.0.26
#---------------------------
# 增加函数 getNonNewCode 取上市的非次新个股

#1.0.27
#---------------------------
# 修改函数 getCashDivdend 提取分红派息 转增、送股信息

#1.0.28
#---------------------------
#修改getMarketTradingCode函数，修复不能取’0008’个股的bug

#1.0.29
#---------------------------
# quote_val_mem 增加 s_val_mv 
# 修改getStockWorth函数 增加totalWorth 

#1.0.30
#---------------------------
# quote_val_mem 增加 s_val_pe/s_val_pb_new
# 修改getStockWorth函数 增加PB

#1.0.31
#---------------------------
#增加getIPODate函数，用于提取个股的上市首日日期 by chenyang

#1.0.32
#---------------------------
# getFinance函数 增加参数isNewest 是否取截止date最新的数据

__version__ = "1.0.32"


import pandas as pd
import datetime as dt

import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

import numpy as np
import math
import itertools as it

from urllib import parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dateutil.relativedelta import relativedelta

import sys
if sys.version_info >= (3,7):
    import exchange_calendars as ecal

mysql_user = 'python'
mysql_Pwd = parse.quote_plus('Aa123@python')
mysql_host = '10.242.195.180'




memtables = {
    'quote_val_mem': {
        'dbName': 'finance',
        'From': 'quote_valuation',
        'To': 'quote_val_mem',
        'accounts': ['wind_code', 'trade_dt', 's_dq_freeturnover','s_dq_mv', 's_val_mv' , 's_val_pe' ,'s_val_pb_new' , 'opdate'],
        'dtypes': ['int', 'date', 'double','double', 'double', 'double', 'double', 'datetime'],
        'indexNames': ['index_quote_val_mem_code', 'index_quote_val_mem_dt'],
        'indexCols': ['wind_code', 'trade_dt']
    },
    'quote_mem': {
        'dbName': 'finance',
        'From': 'quote',
        'To': 'quote_mem',
        'accounts': ['f4_0001', 'f2_1425', 'f4_1425','f7_1425', 'f8_1425', 'f9_1425','f10_1425','f5_1425','f6_1425', 'f3_1425', 'f11_1425','rp_gen_datetime'],
        'dtypes': ['int', 'date', 'double','double', 'double', 'double','double','double','double','double', 'double', 'datetime'],
        'indexNames': ['index_quote_mem_code', 'index_quote_mem_dt'],
        'indexCols': ['f4_0001', 'f2_1425']
    }
    }

#生成当前系统日期时间字符串
def timeStr():
    return f"【{dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】"

# 建立连接
def getConn(host: str = mysql_host, user: str = mysql_user, pwd: str = mysql_Pwd, port: str = '3306' , database:str='finance'):
    '''
    返回数据库接口conn
    '''
    try:
        conn = sql.create_engine(f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{database}?charset=utf8",pool_recycle = 3600*4)
    except:
        raise RuntimeError('建立数据库连接失败')
    return conn

# 关闭连接
def closeConn(conn):
    '''
    关闭数据库接口conn
    '''
    conn.dispose()

# 创建内存表
def createMemTable(conn, structureData, silent: bool = True):
    '''
    创建内存表，
    From 源表名， To 内存表名， accounts 需要复制到内存表中的字段名， dtypes 各字段的数据类型，不能是text/blob类型，与accounts的顺序对应
    indexNames 索引名， indexCols 索引字段，与索引名对应，如为多重索引用','隔开
    silent 是否显示创建过程
    '''
    From = structureData['From']
    To = structureData['To']
    accounts = structureData['accounts']
    dtypes = structureData['dtypes']
    indexNames = structureData['indexNames']
    indexCols = structureData['indexCols']

    Session = sessionmaker(bind=conn)
    session = Session()
    session.execute(f"use {structureData['dbName']}")
    exist = session.execute(f"show tables like '{To}'").fetchall()
    if len(exist) != 0:
        if session.execute(f"select count(1) from `{To}` limit 10;").fetchall()[0][0] != 0:
            # 已有内存表
            return
    if not silent:
        print('creating price series in memory...')
    old_heapsize = session.execute("select @@max_heap_table_size/1024/1024").fetchall()[0][0]
    session.execute("use information_schema")
    s = session.execute(
        f"select round(sum(data_length/1024/1024),2) as data from tables where table_schema='{structureData['dbName']}' and table_name='{From}';")
    table_size = s.fetchall()[0][0]
    if float(table_size) * 1.2 > float(old_heapsize):
        session.execute(f"set @@max_heap_table_size= {int((float(table_size) * 1.2) * 1024 * 1024)}")
        session.execute(f"set @@tmp_table_size= {int((float(table_size) * 1.2) * 1024 * 1024)}")

    oldInnodbBufferPoolSize = session.execute("select @@innodb_buffer_pool_size/1024/1024").fetchall()[0][0]
    if oldInnodbBufferPoolSize < 64 * 1024 * 1024:
        session.execute(f"set GLOBAL innodb_buffer_pool_size= {int(64 * 1024 * 1024)}")
    session.commit()
    session.execute(f"use {structureData['dbName']}")
    session.execute(f'''CREATE TABLE IF NOT EXISTS {To}(
        {', '.join([f'{x[0]} {x[1]}' for x in zip(accounts, dtypes)])}
        {f', ' + ', '.join([f'INDEX {x[0]}({x[1]})' for x in zip(indexNames, indexCols)]) if len(indexNames) and len(indexCols) else ''}
        )ENGINE=MEMORY DEFAULT CHARSET=utf8;
        ''')
    session.execute(f"INSERT INTO  `{To}` select {', '.join(accounts)} from {From}")
    session.commit()
    if not silent:
        print(f'table {To} in memory has been created.')
    session.close()

# 删除内存表
def cleanMemTables(conn, schemas: list, tablenames: list):
    '''
    删除内存表
    conn 数据库接口
    schemas List类型，每个表对应的库schema名称
    tablenames List类型，表名
    '''
    Session = sessionmaker(bind=conn)
    session = Session()
    for schema, name in zip(schemas, tablenames):
        session.execute(f"use {schema}")
        session.execute(f'DROP TABLE IF EXISTS {name}')
    session.commit()
    session.close()

# 提取交易日历(原始提取方法) 暂时放弃使用 替换为getCalendarDB
def getCalendar(startDate:dt.datetime,endDate:dt.datetime,freq:str='d'):
    #freq可取值与pandas.date_range中freq一致，d为每天，w-mon为每周一，w-fri为每周五
    cal = ecal.get_calendar('XSHG')
    schedule = cal.schedule.loc[startDate.strftime('%Y-%m-%d'):endDate.strftime('%Y-%m-%d')]
    c = list(map(lambda x: pd.to_datetime(x.strftime('%Y-%m-%d')),schedule.index.tolist()))
    d = list(filter(lambda x: x not in [dt.datetime(2022,9,12),dt.datetime(2022,10,6),dt.datetime(2022,10,7),dt.datetime(2023,5,2),dt.datetime(2023,5,3),dt.datetime(2023,6,23)], c))
    dpd = pd.date_range(startDate,endDate,freq=freq)
    trade_list = list(filter(lambda x: x in dpd, d))
    return sorted(trade_list)

#提取交易股票，需要接入conn，从数据库提取日期数据
def getCalendarDB(conn,startDate:dt.datetime,endDate:dt.datetime,freq:str='d'):
    # conn finance库
    #freq可取值与pandas.date_range中freq一致，d为每天，w-mon为每周一，w-fri为每周五
    d = pd.read_sql(f'''SELECT date FROM trade_date_mem
               WHERE
                     date >= '{startDate.strftime("%Y%m%d")}'
                AND
                     date <= '{endDate.strftime("%Y%m%d")}'
''',conn)
    trade_list = d['date'].tolist()
    if freq !='d':
        def cal_trade_day(x):
            if x in trade_list:
                return x
            else:
                x = x - relativedelta(days=1)
                return cal_trade_day(x)
        dpd = pd.date_range(startDate,endDate,freq=freq)
        trade_list = list(set(map(lambda y: cal_trade_day(y), dpd)))
        # trade_list = list(set(dpd.tolist()).intersection(set(trade_list)))
    return sorted(trade_list)

#提取交易日个股，需要接入conn，从内存表提取数据
def getStockDB(conn,startDate:dt.datetime,endDate:dt.datetime):
    # conn finance库
    #freq可取值与pandas.date_range中freq一致，d为每天，w-mon为每周一，w-fri为每周五
#     d = pd.read_sql(f'''SELECT f4_0001 as code FROM quote_mem
#                WHERE
#                      `f2_1425` between '{startDate.strftime("%Y%m%d")}'
#                 AND
#                     '{endDate.strftime("%Y%m%d")}'
# ''',conn)
    
    d = pd.read_sql(f'''SELECT distinct(f4_0001) FROM quote_mem
               WHERE `f11_1425` = -1  AND
                     `f2_1425` between '{startDate.strftime("%Y%m%d")}'
                AND
                    '{endDate.strftime("%Y%m%d")}'
''',conn)
    code_list = d['f4_0001'].unique().tolist()

    return code_list

def fillDate(conn, recreate=True):
    print(f'{timeStr()} update trade_date_mem table')
    table_exist = pd.read_sql('''select count(1) from information_schema.tables where TABLE_SCHEMA = 'finance' and TABLE_NAME = 'trade_date_mem';''',conn)
    table_exist = table_exist.iloc[0,0]==1
    #如果表存在，则要做增量更新，则要找到更新起始日期
    if table_exist and not recreate:
        latestday = pd.read_sql("select max(date) from trade_date_mem",conn)
        if latestday.applymap(lambda x: isinstance(x,dt.date)).iloc[0,0]:#查到上次更新的日期
            start_date = latestday.iloc[0,0] + relativedelta(days=1)
    Session = sessionmaker(bind=conn)
    session = Session()
    if recreate or not table_exist:
        cleanMemTables(conn,['finance'],['trade_date_mem'])
        #建立新的内存表
        session.execute(f"use finance")
        session.execute(f'''create table trade_date_mem(
                    date datetime not null primary key,
                    index dateindex(date))
                    engine = memory default charset = utf8''')
        session.commit()
        session.execute(f'''INSERT INTO trade_date_mem
                        SELECT DISTINCT f2_1425 as date FROM quote where f4_0001 not like '5%%' ORDER BY f2_1425 DESC
                        ;''')
        session.commit()
    else:#增量更新
        session.execute(f'''INSERT INTO trade_date_mem
                    SELECT DISTINCT f2_1425 as date FROM quote 
                    WHERE f2_1425 >='{start_date.strftime("%Y%m%d")}' and f4_0001 not like '5%%' ORDER BY f2_1425 DESC
                ;''')
        session.commit()
    session.close()
    print(f'{timeStr()} trade_date_mem done')

# 提取三张表里的数据，滚动到date日可获得的最新数据，可一次查询多次股票，可一次查询多股
# 增加财务衍生数据表
def getFinance(conn, codelist: list, date: dt.datetime, accounts: str, table: str,
               repType: str = '合并报表', singleSeason: bool = False,
               years: int = 5, isNewest: bool = False
               ) -> pd.DataFrame:
    # account 为要查找的数据名称，按表中原始表头查询，多个字段中用半角,号分隔
    # table 为表名
    # codes 为股票代码，可用半角,分隔查询多个
    # date 为日期
    # repType 默认为合并报表，可选 母公司|合并报表
    # years 回取几年的数据，默认5年，这里以实际披露日期为准
    # isNewest 是否取最新的数据.如果一次性取出历史的数据，为False.若滚动到date日可获得的最新数据，为True.

    # host 服务器地址
    # user 数据库用户名
    # pwd 用户密码
    # port 数据库端口
    tables = {
        'balance': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1853': 'reportPeriod',
            'f3_1853': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1853': 'reportType'
        },
        'income': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1854': 'reportPeriod',
            'f3_1854': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1854': 'reportType'
        },
        'cash': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1855': 'reportPeriod',
            'f3_1855': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1855': 'reportType'
        },
        'derivative':{
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f3_5034': 'reportPeriod',
            'f4_5034': 'reportType',
        }
    }
    bunchSize = 100  # 每次sql提取股票数量上限
    searchFor = list(
        filter(
            lambda x: x not in tables[table].keys(), [] if not len(accounts) else accounts.split(',')
        )
    )  # 要查询字段，剔除tables中的筛选使用的字段

    if table!='derivative':
        dateTableName = list(tables[table].keys())[
            list(tables[table].values()).index('reportDate')]  # 获取要查询的表中，reportDate的header名
    periodTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportPeriod')]  # 获取要查询的表中，reportPeriod的header名
    typeTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportType')]  # 获取要查询的表中，reportType的header名
    res = pd.DataFrame()
    mpres = []
    with ThreadPoolExecutor(max_workers=4) as e:
        for i in range(math.ceil(len(codelist) / bunchSize)):  # 每个循环最多提取bunchSize只股票数据
            codestr = ",".join([f"\'{x}\'" for x in codelist[i * bunchSize:i * bunchSize + bunchSize]])
            # sigleStr = f'and {typeTableName} like \'%%单季%%\'' if sigleSeason else f'and {typeTableName} not like \'%%单季%%\''
            # t = pd.read_sql(
            #     f'select {",".join(list(tables[table].keys()) + searchFor)} from {table} where f4_0001 in ({codestr}) and \
            #     {dateTableName} between \'{(date + relativedelta(years=-1*years)).strftime("%Y%m%d")}\' and \'{date.strftime("%Y%m%d")}\' and \
            #     {typeTableName} like \'%%{repType}%%\' {sigleStr}', conn)
            if table!='derivative':
                mpres.append(
                    e.submit(
                        pd.read_sql,
                        f'''
                        SELECT
                            {",".join(list(tables[table].keys()) + searchFor)}
                        FROM
                            {table}
                        WHERE
                            f4_0001 in ({codestr}) 
                        AND
                            {dateTableName} BETWEEN 
                                \'{(date + relativedelta(years=-1 * years)).strftime("%Y%m%d")}\'
                            AND
                                \'{date.strftime("%Y%m%d")}\'
                        AND
                            {typeTableName} like \'%%{repType}%%\'
                        ORDER BY
                                {periodTableName} DESC,
                                {dateTableName} DESC
                            ''',
                        conn,
                        parse_dates={
                            dateTableName: '%Y%m%d',
                            periodTableName: '%Y%m%d'
                        }
                    )
                )
            else:
                mpres.append(
                    e.submit(
                        pd.read_sql,
                        f'''
                        SELECT
                            {",".join(list(tables[table].keys()) + searchFor)}
                        FROM
                            {table}
                        WHERE
                            f4_0001 in ({codestr}) 
                        AND
                            {periodTableName} BETWEEN 
                                \'{(date + relativedelta(years=-1 * years)).strftime("%Y%m%d")}\'
                            AND
                                \'{date.strftime("%Y%m%d")}\'
                        AND
                            {typeTableName} like \'%%{repType}%%\'
                        ORDER BY
                                {periodTableName} DESC
                            ''',
                        conn,
                        parse_dates={
                            periodTableName: '%Y%m%d'
                        }
                    )
                )

    for futrue in as_completed(mpres):
        t = futrue.result().copy()
        t = t[t[typeTableName].str.contains('单季') ^ (not singleSeason)]  # 筛选单季
        if not t.empty:
            t.rename(columns=tables[table], inplace=True)
            if isNewest:
                res = res.append(t.groupby(by=['code', 'reportPeriod']).head(1))
            else:
                res = res.append(t)

    return res.reset_index(drop=True)


def getFinance_derivative(conn, codelist: list, periodDate: dt.datetime, accounts: str, table: str = 'derivative',
                          repType: str = '合并报表',
                          years: int = 5
                          ) -> pd.DataFrame:
    # account 为要查找的数据名称，按表中原始表头查询，多个字段中用半角,号分隔
    # table 为表名
    # codes 为股票代码，可用半角,分隔查询多个
    # date 为日期
    # repType 默认为合并报表，可选 母公司|合并报表
    # years 回取几年的数据，默认5年，这里以实际披露日期为准

    # host 服务器地址
    # user 数据库用户名
    # pwd 用户密码
    # port 数据库端口
    tables = {
        'derivative':
            {'f4_0001': 'code',
             'f6_0001': 'name',
             'f3_5034': 'reportPeriod',
             'f4_5034': 'reportType'}
    }
    bunchSize = 100  # 每次sql提取股票数量上限
    searchFor = list(
        filter(
            lambda x: x not in tables[table].keys(), [] if not len(accounts) else accounts.split(',')
        )
    )  # 要查询字段，剔除tables中的筛选使用的字段

    periodTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportPeriod')]  # 获取要查询的表中，reportPeriod的header名
    typeTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportType')]  # 获取要查询的表中，reportType的header名
    res = pd.DataFrame()
    mpres = []
    with ThreadPoolExecutor(max_workers=4) as e:
        for i in range(math.ceil(len(codelist) / bunchSize)):  # 每个循环最多提取bunchSize只股票数据
            codestr = ",".join([f"\'{x}\'" for x in codelist[i * bunchSize:i * bunchSize + bunchSize]])
            mpres.append(
                e.submit(
                    pd.read_sql,
                    f'''
                    SELECT
                        {",".join(list(tables[table].keys()) + searchFor)}
                    FROM
                        {table}
                    WHERE
                        f4_0001 in ({codestr}) 
                    AND
                        {periodTableName} BETWEEN 
                            \'{(periodDate + relativedelta(years=-1 * years)).strftime("%Y%m%d")}\'
                        AND
                            \'{periodDate.strftime("%Y%m%d")}\'
                    AND
                        {typeTableName} like \'%%{repType}%%\'
                    ORDER BY
                            {periodTableName} DESC
                        ''',
                    conn,
                    parse_dates={
                        periodTableName: '%Y%m%d'
                    }
                )
            )
    for futrue in as_completed(mpres):
        t = futrue.result().copy()
        if not t.empty:
            t.rename(columns=tables[table], inplace=True)
            res = res.append(t.groupby(by=['code', 'reportPeriod']).head(1))
    return res.reset_index(drop=True)


# 提TTM数据，支持三张表
def getTTM(conn, codelist: list, date: dt.datetime, accounts: str, table: str, repType: str = '合并报表',
           ttmYears=3) -> pd.DataFrame:
    tables = {
        'balance': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1853': 'reportPeriod',
            'f3_1853': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1853': 'reportType'
        },
        'income': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1854': 'reportPeriod',
            'f3_1854': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1854': 'reportType'
        },
        'cash': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1855': 'reportPeriod',
            'f3_1855': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1855': 'reportType'
        },
    }
    temp = getFinance(conn, codelist=codelist, date=date, accounts=accounts, table=table, singleSeason=False,
                      repType=repType, years=ttmYears + 2)  # years要在ttm的基础上+2以涵盖足够的数据
    searchFor = list(filter(lambda x: x not in tables[table].keys(), [] if not len(accounts) else accounts.split(',')))
    gvalues = list()
    gindex = list()
    gcolumns1 = list()
    gcolumns2 = list()

    def cal_TTM(x, searchFor, table, gvalues, gindex, gcolumns1, gcolumns2):
        startFrom = x.reportPeriod.max()
        if table == 'balance' or startFrom.month == 12:
            date = [startFrom - relativedelta(years=i) for i in range(ttmYears)]  # 计算需要的报告期
            tmp = x[x.reportPeriod.isin(date)][searchFor]  # 提取报告期数据
            n = tmp.shape[0]
            if n:
                values = tmp.values.flatten()  # 数据重列
                gvalues = gvalues.append(values.reshape(-1, len(searchFor)).T.flatten())
                # titles = np.array([ f"{name}_{n-i-1}" for i in range(n) for name in searchFor])

        else:
            lastdate = x.reportPeriod.max()
            date_add_1 = [dt.datetime(lastdate.year - i - 1, 12, 31) for i in range(ttmYears)]  # 需要相加的报告期
            date_add_2 = [lastdate - relativedelta(years=i) for i in range(ttmYears)]  # 需要相加的报告期
            date_sub = [lastdate - relativedelta(years=i + 1) for i in range(ttmYears)]  # 需要相减的报告期
            tmp = x[x.reportPeriod.isin(date_add_1 + date_add_2 + date_sub)]  # 提取所需数据
            dates = [*zip(date_add_2, date_add_1, date_sub)]  # 组合计算过程
            ts = tmp[searchFor + ['reportPeriod']].set_index('reportPeriod')
            values = list()
            for i, datelist in enumerate(dates):
                try:
                    # d = ts.loc[list(datelist)]
                    # ans=ans.append((d.iloc[0]+d.iloc[1]-d.iloc[2]).rename(f"{{}}_{i}".format))
                    # xx=(ts.loc[list(datelist)[0]]+ts.loc[list(datelist)[1]]-ts.loc[list(datelist)[2]])
                    xx = ts.apply(lambda ss: ss[datelist[0]] + ss[datelist[1]] - ss[datelist[2]], axis=0)
                    # xx = xx.rename(lambda x: (x,i))
                    # ans=ans.append(xx)
                    values = values + xx.values.tolist()
                except:
                    # ans=ans.append(pd.Series([np.NaN]*len(searchFor),index=list(map(lambda x: (x,i),searchFor))))
                    values = values + [np.NaN] * len(searchFor)
            gvalues.append(np.array(values).reshape(-1, len(searchFor)).T.flatten())
        gindex.append(temp.loc[x.index[0]].code)
        for vi in filter(lambda x: x not in gcolumns1, searchFor):
            gcolumns1.extend([vi] * ttmYears)
            gcolumns2.extend([*range(ttmYears)])

            # tt = ans.rename(x.index[-1])
            # tt = pd.DataFrame([values],columns=vindex,index=[x.code.iloc[0]])
            # tt = tt.to_frame()
            # tt=tt.T
            # rr = x.join(tt)

    temp.groupby('code').apply(
        lambda x: cal_TTM(x, searchFor, table, gvalues=gvalues, gindex=gindex, gcolumns1=gcolumns1,
                          gcolumns2=gcolumns2))
    temp_TTM = pd.DataFrame(gvalues, index=gindex, columns=[gcolumns1, gcolumns2])
    return temp_TTM  # temp_TTM.dropna(subset=list(filter(lambda x: any([y in x[0] and x[0] != y for y in searchFor]), temp_TTM.columns.tolist())),how='all',axis=0)


# #填充市值数据，原数据中需要有code,date字段，提取对应code,date日的市值数据,accounts为需要查询的字段
# def fillDailyValue(conn,data,accounts:str,codestr:str='code',datestr:str='date', opdate:dt.datetime=None )->None:
#     #日期数据需要为dt.datetime格式
#     search = data[[codestr,datestr]].drop_duplicates()
#     if opdate is None:
#         opdate = search[datestr].max() + relativedelta(days=1)
#     d=pd.read_sql(
#         f'''
#         SELECT
#             wind_code as {codestr},
#             trade_dt as {datestr},
#             {accounts}
#         FROM
#             quote_valuation
#         WHERE
#                 wind_code in ({','.join([f"'{code}'" for code in search[codestr].tolist()])})
#             AND
#                 trade_dt BETWEEN
#                     {search[datestr].min().strftime('%Y%m%d')}
#                 AND
#                     {search[datestr].max().strftime('%Y%m%d')}
#             AND
#                 opdate <= '{opdate.strftime("%Y-%m-%d")}'
#         ORDER BY
#             opdate DESC
#         ''',conn,parse_dates={datestr:'%Y%m%d'}
#     )
#     #数据去重
#     d.drop_duplicates(subset=[codestr,datestr],keep='first',inplace=True)
#     if not isinstance(data[datestr].iloc[0],type(d[datestr].iloc[0])) and isinstance(data[datestr].iloc[0],dt.datetime):
#         d.loc[:,datestr]=d[datestr].dt.datetime #处理可能出现的dt.datetimetime64与dt.datetime类型不一致的问题
#     return pd.merge(data,d,on=[codestr,datestr])

# 提取分红派息 转增、送股信息
def getCashDivdend(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, byPeriod=False) -> pd.DataFrame:
    # startDate和endDate对应除权除息日的起始
    d = pd.read_sql(
        f'''select distinct
                f4_0001 as code,
                f5_1093/10 as StockGivePerShare,
                f7_1093/10 as StockTransformPerShare,
                f10_1093/10 as DivPerShareAfterTax,
                f9_1093/10 as DivPerShareBeforeTax,
                f26_1093 as rightLostDay,
                f40_1093 as shares,
                f41_1093 as reportDate,
                f10_1093*f40_1093*1000 as totalAmount,
                f24_1093 as period
            from bonus
            where
                    f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
                and
                    {'f24_1093' if byPeriod else 'f26_1093'} between {startDate.strftime('%Y%m%d')} and {endDate.strftime('%Y%m%d')}\
             ''', conn, parse_dates={
            'rightLostDay': '%Y%m%d',
            'period': '%Y%m%d'
        })
    d = d.dropna(subset=['totalAmount'])
    e = d.drop_duplicates(subset=['code', 'period','rightLostDay'])
    return e

# 取日均流通市值数据
def getAverMV(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime,
              opdate: dt.datetime = None) -> pd.DataFrame:
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    d = pd.read_sql(
        f'''SELECT
                wind_code as code,
                trade_dt as date,
                s_dq_mv as currentWorth
            FROM quote_valuation
            WHERE
                wind_code in ({','.join([f"'{code}'" for code in codelist])})
            AND
                trade_dt BETWEEN 
                   '{startDate.strftime('%Y%m%d')}'
                AND
                   '{endDate.strftime('%Y%m%d')}'
            ORDER BY
                opdate DESC
            ''', conn, parse_dates={
            'date': '%Y%m%d'
        })
    # 去重
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    return d.groupby('code')['currentWorth'].mean().to_frame().reset_index()

# 截止日取最新报告期日期
def getLatestReportPeriod(conn, codelist: list, date: dt.datetime, checkThreeSheets: bool = False) -> pd.DataFrame:
    # date 截止日期
    if checkThreeSheets:
        return pd.read_sql(
            f'''SELECT
                code,
                min(reportPeriod) as reportPeriod
            FROM
                (
                    SELECT
                        f4_0001 as code,
                        max(f2_1853) as reportPeriod
                    FROM
                        balance
                    WHERE
                            f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
                        and
                            f3_1853 <= \'{date.strftime('%Y%m%d')}\'
                    GROUP BY
                        f4_0001
                    UNION
                    SELECT
                        f4_0001,
                        max(f2_1854) as reportPeriod
                    FROM
                        income
                    WHERE
                            f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
                        and
                            f3_1854 <= \'{date.strftime('%Y%m%d')}\'
                    GROUP BY
                        f4_0001
                    UNION
                    SELECT
                        f4_0001,
                        max(f2_1855) as reportPeriod
                    FROM
                        cash
                    WHERE
                            f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
                        and
                            f3_1855 <= \'{date.strftime('%Y%m%d')}\'
                    GROUP BY
                        f4_0001
                ) tmptable
            GROUP BY
                code;
                ''', conn, parse_dates={'reportPeriod': '%Y%m%d'})
    else:
        return pd.read_sql(
            f'''SELECT
                    f4_0001 as code,
                    max(f2_1853) as reportPeriod
                FROM
                    balance
                WHERE
                        f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
                    and
                        f3_1853 <= \'{date.strftime('%Y%m%d')}\'
                GROUP BY
                    f4_0001''', conn, parse_dates={'reportPeriod': '%Y%m%d'})

# 取一定时期内，所有定期报告披露日期
def getReportDate(conn,codelist:list,startDate:dt.datetime,endDate:dt.datetime)->pd.DataFrame:
    return pd.read_sql(f'''
    SELECT
        DISTINCT
        f4_0001 as code,
        f2_1853 as period,
        f3_1853 as reportDate
    FROM
        balance
    WHERE
        f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
    AND
        f3_1853 BETWEEN
            '{startDate.strftime("%Y%m%d")}'
        AND
            '{endDate.strftime("%Y%m%d")}'
    ORDER BY
        f4_0001, f2_1853, f3_1853
    ''',conn,parse_dates={'period':'%Y%m%d','reportDate':'%Y%m%d'})

# 根据个股取申万行业分类
def getSwInd(conn, codelist: list, date: dt.datetime, level: int = 1) -> pd.DataFrame:
    # level可以设置为1、2、3，对应申万一级、二级、三级行业分类标准
    d = pd.read_sql(
        f'''
        SELECT
            s_info_code code,
            industriesname sw_name,
            industriescode sw_code
        FROM
        (
            SELECT
                s_info_code,
                sw_ind_code
            FROM
                nsw_industry_class
            WHERE
                s_info_code in ({','.join([f"'{code}'" for code in codelist])})
            AND
                entry_dt<='{date.strftime('%Y%m%d')}'
            AND
                    (remove_dt>'{date.strftime('%Y%m%d')}'
                OR
                    remove_dt is NULL)
        ) a
        JOIN
            sw_industry_info b
        ON
            b.industriescode like concat(substr(a.sw_ind_code,1,{2 + 2 * level}),'%%')
        WHERE
            b.levelnum = {level + 1}
        ''', conn
    )
    return d.drop_duplicates()


# 取指定个股在指定区间内所属申万行业分类
def getSwIndDuring(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, level: int = 1) -> pd.DataFrame:
    # level可以设置为1、2、3，对应申万一级、二级、三级行业分类标准
    d = pd.read_sql(
        f'''
        SELECT  DISTINCT
            s_info_code code,
            industriesname sw_name,
            entry_dt,
            remove_dt,
            cur_sign
        FROM
        (
            SELECT
                s_info_code,
                sw_ind_code,
                entry_dt,
                remove_dt,
                cur_sign
            FROM
                nsw_industry_class
            WHERE
                s_info_code in ({','.join([f"'{code}'" for code in codelist])})
            AND
                entry_dt<='{endDate.strftime('%Y%m%d')}'
            AND
                    (remove_dt>'{startDate.strftime('%Y%m%d')}'
                OR
                    remove_dt is NULL)
        ) a , sw_industry_info b
        WHERE
            b.levelnum = {level + 1}
        AND
            b.industriescode like concat(substr(a.sw_ind_code,1,{2 + 2 * level}),'%%')
        ''', conn, parse_dates={'entry_dt': '%Y%m%d', 'remove_dt': '%Y%m%d'}
    )

    data = pd.DataFrame(it.product(codelist, pd.date_range(start=startDate, end=endDate, name='date').tolist()),
                        columns=['code', 'date'])
    data = pd.merge(data, d)
    data = data[(data.date >= data.entry_dt) & ((data.date <= data.remove_dt) | (data.cur_sign == '1'))].reset_index(
        drop=True)
    # data['date'] = data['date'].apply(lambda x:x.strftime('%Y%m%d'))
    return data[['code', 'date', 'sw_name']]


# 取所有申万行业分类
def getAllSwInd(conn, level: int = 1) -> pd.DataFrame:
    # level可以设置为1、2、3，对应申万一级、二级、三级行业分类标准
    return pd.read_sql(
        f'''
        SELECT 
        DISTINCT industriescode,industriesname
        FROM
            sw_industry_info
        WHERE
                levelnum = '{level + 1}'
            AND
                industriescode LIKE '76%'
        ''', conn
    )


# 取指定时间区间内，所有申万行业指数行数数据
def getAllSwIndQuote(conn, startDate: dt.datetime, endDate: dt.datetime, level: int = 1) -> pd.DataFrame:
    # level可以设置为1、2、3，对应申万一级、二级、三级行业分类标准
    # 返回数据为时间升序
    d = pd.read_sql(
        f'''
        WITH tmp AS(
            SELECT
                DISTINCT industriescode,industriesname
            FROM
                sw_industry_info
            WHERE
                    levelnum = '{level + 1}'
                AND
                    industriescode LIKE '76%%'
        )
        SELECT
            code,
            industriesname sw_name,
            date,
            a.industriesCode,
            pre_close,
            open,
            high,
            low,
            close,
            volume,
            amount,
            pe,
            pb,
            currentWorth,
            TotalWorth
        FROM
            (SELECT
                s_info_windcode code,
                s_info_industrycode industriesCode,
                trade_dt date,
                s_dq_preclose pre_close,
                s_dq_open open,
                s_dq_high high,
                s_dq_low low,
                s_dq_close close,
                s_dq_volume volume,
                s_dq_amount amount,
                s_val_pe pe,
                s_val_pb pb,
                s_dq_mv currentWorth,
                s_val_mv totalWorth
            FROM
                sw_index_quote
            WHERE
                s_info_industrycode in (
                    SELECT
                        industriescode
                    FROM
                        tmp)
            AND
                    trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
            ORDER BY
                trade_dt) a
        LEFT JOIN
            tmp
        ON
            a.industriesCode = tmp.industriescode
        ''', conn, parse_dates={'date': '%Y%m%d'}
    )
    # d中可以出现复制行，其中一行没有pe,pb,currentWorth值
    # 残缺行通常出现在另一行的前端
    return d.groupby(['code', 'date']).tail(1)


# 取日均换手率
# speed:slow, mid(mem)
def getFreeTurnover(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, memtableName: str = None,
                    opdate: dt.datetime = None, isMean:bool=True) -> pd.DataFrame:
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    d = pd.read_sql(
        f'''
        SELECT
            wind_code code,
            trade_dt date,
            s_dq_freeturnover freeTurnover,
            opdate
        FROM
            {memtableName if memtableName else 'quote_valuation'}
        WHERE
                wind_code in ({','.join(list(map(lambda c: str(int(c)), codelist))) if memtableName else ','.join([f"'{code}'" for code in codelist])})
            AND
                trade_dt BETWEEN
                    '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
                AND
                    '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d') }'
        ''', conn,parse_dates={'date':'%Y-%m-%d' if memtableName else '%Y%m%d'}
    )
    # 将code类型从int转换为str
    if memtableName:
        d.loc[:, 'code'] = d['code'].astype(str).str.zfill(6)
    d.sort_values(by=['code','date','opdate'],ascending=[True,True,False],inplace=True)
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    d.loc[:, 'freeTurnover'] = d['freeTurnover'].astype(float)
    if isMean:
        return d.groupby('code')['freeTurnover'].mean().to_frame().reset_index()
    else:
        return d


# 取涨跌幅
# speed:mid(mem),slow 
def getStockReturns(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, memtableName: str = None,
                    opdate: dt.datetime = None) -> pd.DataFrame:
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    d = pd.read_sql(f'''
        SELECT
            f4_0001 code,
            f7_1425 close,
            f2_1425 date
        FROM
            {'quote' if memtableName is None else memtableName}
        WHERE
            f4_0001 in ({','.join([str(int(code)) for code in codelist])})
        AND
            f2_1425 BETWEEN
                '{startDate.strftime("%Y%m%d") if memtableName is None else startDate.strftime("%Y-%m-%d")}'
            AND
                '{endDate.strftime("%Y%m%d") if memtableName is None else endDate.strftime("%Y-%m-%d")}'
        ORDER BY
            f2_1425,
            rp_gen_datetime DESC
        ''', conn, parse_dates={'date': '%Y%m%d' if memtableName is None else '%Y-%m-%d'})
    if memtableName:
        d.loc[:, 'code'] = d['code'].astype(str).str.zfill(6)
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    returns = d.groupby('code')['close'].apply(lambda x: x.iloc[-1] / x.iloc[0] - 1).rename('returns')
    return d.groupby('code')['date'].agg([min, max]).rename(columns={'max': 'endDate', 'min': 'startDate'}).join(
        returns)

#取涨跌幅，精准匹配起始日期
#速度快
def getStockReturnsExactdate(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, memtableName: str = None,
                    opdate: dt.datetime = None, logReturn:bool=False) -> pd.DataFrame:
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    d = pd.read_sql(f'''
        SELECT
            open.f4_0001 code,
            {'close.close/open.open-1' if not logReturn else 'LOG(close.close/open.open)' } as returns
        FROM
        (
            SELECT
                f4_0001,
                f7_1425 open
            FROM
                {'quote' if memtableName is None else memtableName}
            WHERE
                f4_0001 in ({','.join([str(int(code)) for code in codelist])})
            AND
                F2_1425 = '{startDate.strftime("%Y%m%d")}'
        )open
        JOIN
        (
            SELECT
                f4_0001,
                f7_1425 close
            FROM
                {'quote' if memtableName is None else memtableName}
            WHERE
                f4_0001 in ({','.join([str(int(code)) for code in codelist])})
            AND
                F2_1425 = '{endDate.strftime("%Y%m%d")}'
        )close
        ON
            open.f4_0001=close.f4_0001
        ''', conn)
    if memtableName:
        d.loc[:, 'code'] = d['code'].astype(str).str.zfill(6)
    d.drop_duplicates(subset=['code'], keep='first', inplace=True)
    return d


#取交易日
def getTradingDays(conn, startDate:dt.datetime,endDate:dt.datetime,memtableName:str=None)->pd.DataFrame:
    return pd.read_sql(
        f'''
        SELECT
            DISTINCT(`f2_1425`) date
        FROM
            {memtableName if memtableName else 'quote'}
        WHERE
            `f2_1425` BETWEEN 
                '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
            AND
                '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d')}'
        ''',
        conn,parse_dates={'date': '%Y-%m-%d' if memtableName else '%Y%m%d'}
    )


# 取个股价格
def getStockPricePlusName(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, pType: str = 'fore',
                  accounts: str = 'close', memtableName: str = None, opdate: dt.datetime = None) -> pd.DataFrame:
    # pType:fore 后复权, back 前复权, origin 不复权
    # 返回的数据按日期降序排列
    # 使用内存表时，注意所查询字段已经复制到内存表中，才可以使用
    # 使用原始收盘价或者前复权价时，注意f10_1425字段需要复制到内存表中
    names = {
        'close': 'f7_1425',
        'low': 'f6_1425',
        'high': 'f5_1425',
        'open': 'f4_1425',
        'pre_close': 'f3_1425',
        'volume': 'f8_1425',
        'amount': 'f9_1425',
        'status': 'f11_1425'
    }
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    listAc = [names[ac.lower()] for ac in accounts.split(',')]
    # f3-f7有复权因子
    if pType.lower() == 'origin':
        listAc = [*map(lambda x: x + '/f10_1425' if x[1] in list('34567') else x, listAc)]
    # 原始数据为后复权数据
    # 如需前复权数据，先提取后复权数据，然后缩放到最新价
    listAc = [f'{k[0]} {k[1]}' for k in [*zip(listAc, accounts.split(','))]]
    if pType.lower() == 'back':
        listAc = listAc + ['f10_1425 factor_test']
    d = pd.read_sql(
        f'''
        SELECT
            f4_0001 code,
            f6_0001 name,
            f2_1425 date,
            rp_gen_datetime opdate,
            {','.join(listAc)}
        FROM
            {memtableName if memtableName else 'quote'}
        WHERE
                f4_0001 in ({','.join(list(map(lambda c: str(int(c)), codelist))) if memtableName else ','.join([f"'{code}'" for code in codelist])})
            AND
                f2_1425 BETWEEN
                    '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
                AND
                    '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d')}'
        ''', conn, parse_dates={'date': '%Y%m%d' if memtableName is None else '%Y-%m-%d'}
    )
    # 内存表为hash索引，不支持orderby加速，在外层来order
    d.sort_values(by=['code', 'date', 'opdate'], ascending=[True, True, False], inplace=True)
    # 去重
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    # 排序
    d.sort_values('date', ascending=False, inplace=True)
    if pType.lower() == 'back':
        latestPrice = d.groupby('code').apply(lambda x: x.loc[x['date'].idxmax()]).reset_index(drop=True)
        d = pd.merge(d.drop('factor_test', axis=1), latestPrice[['code', 'factor_test']], how='left', on='code')
        for col in filter(lambda x: x in ['close', 'open', 'high', 'low', 'preclose'], d.columns.tolist()):
            d.loc[:, col] = d[col] / d['factor_test']
    # 将code类型从int转换为str
    if memtableName:
        d.loc[:, 'code'] = d.code.astype(str).str.zfill(6)
    return d


# 取个股价格
def getStockPrice(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, pType: str = 'fore',
                  accounts: str = 'close', memtableName: str = None, opdate: dt.datetime = None) -> pd.DataFrame:
    # pType:fore 后复权, back 前复权, origin 不复权
    # 返回的数据按日期降序排列
    # 使用内存表时，注意所查询字段已经复制到内存表中，才可以使用
    # 使用原始收盘价或者前复权价时，注意f10_1425字段需要复制到内存表中
    names = {
        'close': 'f7_1425',
        'low': 'f6_1425',
        'high': 'f5_1425',
        'open': 'f4_1425',
        'pre_close': 'f3_1425',
        'volume': 'f8_1425',
        'amount': 'f9_1425',
        'status': 'f11_1425'
    }
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    listAc = [names[ac.lower()] for ac in accounts.split(',')]
    # f3-f7有复权因子
    if pType.lower() == 'origin':
        listAc = [*map(lambda x: x + '/f10_1425' if x[1] in list('34567') else x, listAc)]
    # 原始数据为后复权数据
    # 如需前复权数据，先提取后复权数据，然后缩放到最新价
    listAc = [f'{k[0]} {k[1]}' for k in [*zip(listAc, accounts.split(','))]]
    if pType.lower() == 'back':
        listAc = listAc + ['f10_1425 factor_test']
    d = pd.read_sql(
        f'''
        SELECT
            f4_0001 code,
            f2_1425 date,
            rp_gen_datetime opdate,
            {','.join(listAc)}
        FROM
            {memtableName if memtableName else 'quote'}
        WHERE
                f4_0001 in ({','.join(list(map(lambda c: str(int(c)), codelist))) if memtableName else ','.join([f"'{code}'" for code in codelist])})
            AND
                f2_1425 BETWEEN
                    '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
                AND
                    '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d')}'
        ''', conn, parse_dates={'date': '%Y%m%d' if memtableName is None else '%Y-%m-%d'}
    )
    # 内存表为hash索引，不支持orderby加速，在外层来order
    d.sort_values(by=['code', 'date', 'opdate'], ascending=[True, True, False], inplace=True)
    # 去重
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    # 排序
    d.sort_values('date', ascending=False, inplace=True)
    if pType.lower() == 'back':
        latestPrice = d.groupby('code').apply(lambda x: x.loc[x['date'].idxmax()]).reset_index(drop=True)
        d = pd.merge(d.drop('factor_test', axis=1), latestPrice[['code', 'factor_test']], how='left', on='code')
        for col in filter(lambda x: x in ['close', 'open', 'high', 'low', 'pre_close'], d.columns.tolist()):
            d.loc[:, col] = d[col] / d['factor_test']
    # 将code类型从int转换为str
    if memtableName:
        d.loc[:, 'code'] = d.code.astype(str).str.zfill(6)
    return d

# 取个股日收益率序列
def getStockDailyReturns(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, logReturn:bool=False) -> pd.DataFrame:
    d = getStockPrice(conn,codelist,startDate,endDate).pivot(columns='code',values='close',index='date')
    #d = d.dropna(axis=0) #去掉没有报价的个股
    if logReturn:
        return (d/d.shift(1)).applymap(math.log)
    else:
        return (d/d.shift(1))-1


# 取个股区间市值数据，注意去重
def getStockWorth(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime,
                  opdate: dt.datetime = None, memtableName:str=None) -> pd.DataFrame:
    # opdate 为数据录入的时间
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    d = pd.read_sql(f'''
    SELECT
        wind_code code,
        trade_dt date,
        s_dq_mv currentWorth,
        s_val_mv totalWorth,
        s_val_pb_new PB,   
        opdate{",s_val_pe_ttm PETTM,s_val_ps_ttm PSTTM" if memtableName is None else ""}
    FROM
        {"quote_valuation" if memtableName is None else memtableName}
    WHERE
        wind_code IN ({','.join([f"'{code}'" for code in codelist])})
        
        AND
            trade_dt BETWEEN
                '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
            AND
                '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d')}'
    ''', conn, parse_dates={'date': '%Y%m%d' if memtableName is None else '%Y-%m-%d'}
    )
    # 对于d中重复数据，按opdate最新原则去重
    d.sort_values(by=['code','date','opdate'],ascending=[True,True,False],inplace=True)
    d.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    # 将code类型从int转换为str
    if memtableName:
        d.loc[:, 'code'] = d['code'].astype(str).str.zfill(6)
    return d.sort_values('date')


# 取上市 非次新个股
def getNonNewCode(conn, endDate: dt.datetime) -> list:
    # 返回值 非次新股列表
    a = pd.read_sql(f'''
    SELECT
        f4_0001 as code,
        f17_1090 as N_date
    FROM
        stock_info
    ''', conn,parse_dates={'N_date': '%Y%m%d'})
    # 去重
    a['endDate'] = endDate
    a['days_delta'] = a['endDate'] - a['N_date']
    a = a[a['days_delta'] > dt.timedelta(days=365)]
    code_list = a['code'].unique().tolist()
    return code_list


# 取个股上市日期
def getIPODate(conn,codelist) -> pd.DataFrame:
    # 返回值 非次新股列表
    return pd.read_sql(f'''
    SELECT
        f4_0001 as code,
        f17_1090 as IPODate
    FROM
        stock_info
    WHERE
        f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
    ''', conn,parse_dates={'IPODate': '%Y%m%d'})
 


# 取区间市场成交情况，可用于提取在指定时间段有成交的个股代码
def getMarketTrading(conn, startDate: dt.datetime, endDate: dt.datetime, opdate: dt.datetime = None, memtableName:str = None) -> pd.DataFrame:
    # 返回值分别为vol区间累计成交量,amount区间累计成交金额,turnover区间累计自由换手率
    if opdate is None:
        opdate = endDate + relativedelta(days=1)
    a = pd.read_sql(f'''
    SELECT
        wind_code code,
        trade_dt date,
        s_dq_freeturnover
    FROM
         {'quote_valuation' if memtableName is None else memtableName}
    WHERE
            wind_code NOT LIKE '8%%'
        AND
            wind_code NOT LIKE '4%%'
        AND
            trade_dt between '{startDate.strftime('%Y%m%d')}'
        AND
            '{endDate.strftime('%Y%m%d')}'
    ORDER BY
        opdate DESC
    ''', conn)
    # 去重
    a.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    # 调整格式
    a.loc[:, 's_dq_freeturnover'] = a['s_dq_freeturnover'].astype(float)
    # 计算均值
    turnover = a.groupby('code')['s_dq_freeturnover'].mean().to_frame().reset_index()

    b = pd.read_sql(f'''
    SELECT
        f4_0001 code,
        f2_1425 date,
        f8_1425 vol,
        f9_1425 amount
    FROM
        quote
    WHERE
            f4_0001 NOT LIKE '8%%'
        AND
            f4_0001 NOT LIKE '4%%'
        AND
            f2_1425 BETWEEN '{startDate.strftime('%Y%m%d')}'
        AND
            '{endDate.strftime('%Y%m%d')}'  
    ORDER BY
        rp_gen_datetime DESC
    ''', conn)
    # 去重
    b.drop_duplicates(subset=['code', 'date'], keep='first', inplace=True)
    volamountSum = b.groupby('code')[['vol', 'amount']].sum().reset_index()
    return turnover.merge(volamountSum, how='left', on=['code'])


# 取区间市场成交个股，可用于提取在指定时间段有成交的个股代码
def getMarketTradingCode(conn, startDate: dt.datetime, endDate: dt.datetime, opdate: dt.datetime = None,memtableName:str = None) -> pd.DataFrame:
    # 返回值分别为vol区间累计成交量,amount区间累计成交金额,turnover区间累计自由换手率
    # if opdate is None:
    #     opdate = endDate + relativedelta(days=1)
    #     #数据库中opdate最早记录于2012年2月24日
    #     if opdate < dt.datetime(2013,1,1):
    #         opdate = dt.datetime(2013,1,1)
    a = pd.read_sql(f'''
    SELECT
        distinct(wind_code)
    FROM
        {'quote_valuation' if memtableName is None else memtableName}
    WHERE
            `wind_code` NOT LIKE '8_____'
        AND
            `wind_code` NOT LIKE '4_____'
        AND
            `trade_dt` between '{startDate.strftime('%Y%m%d') if memtableName is None else startDate.strftime('%Y-%m-%d')}'
        AND
            '{endDate.strftime('%Y%m%d') if memtableName is None else endDate.strftime('%Y-%m-%d')}'
   
    ''', conn)
    # 去重
    a['wind_code'] = a['wind_code'].apply(lambda x:str(x).zfill(6))
    code_list = a['wind_code'].unique().tolist()
    return code_list


# 返回申万行业指数行情和每日pe,pb
def getSwIndQuote(conn, sw_name: str, startDate: dt.datetime, endDate: dt.datetime) -> pd.DataFrame:
    return pd.read_sql(
        f'''
        SELECT
            s_info_windcode code,
            trade_dt date,
            s_dq_preclose pre_close,
            s_dq_open open,
            s_dq_high high,
            s_dq_low low,
            s_dq_close close,
            s_dq_volume volume,
            s_dq_amount amount,
            s_val_pe pe,
            s_val_pb pb,
            s_val_mv totalWorth,
            s_dq_mv currentWorth
        FROM
            sw_index_quote
        WHERE
            s_info_windcode = (
                SELECT
                    s_info_windcode
                FROM
                    sw_index_quote
                WHERE
                    s_info_industryname = '{sw_name}'
                LIMIT 1)
        AND
                trade_dt between '{startDate.strftime('%Y%m%d')}'
            AND
                '{endDate.strftime('%Y%m%d')}'
        ORDER BY
            trade_dt
        ''', conn, parse_dates={'date': '%Y%m%d'}
    )

# 获取申万行业指数回报和PEPB
def getSwIndReturnsAvePEPB(conn, sw_name: str, startDate: dt.datetime, endDate: dt.datetime) -> pd.DataFrame:
    # 返回的pe和pb数据为期间PEPB均值
    return pd.read_sql(
        f'''
        WITH tmp1 AS( #行业PE与PB数据
            SELECT
                s_info_windcode,
                avg(s_val_pe) pe,
                avg(s_val_pb) pb
            FROM
                sw_index_quote
            WHERE
                s_info_windcode = (
                    SELECT
                        s_info_windcode
                    FROM
                        sw_index_quote
                    WHERE
                        s_info_industryname = '{sw_name}'
                    ORDER BY
                        trade_dt DESC
                    LIMIT 1)
            AND
                    trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
            GROUP BY
                s_info_windcode
        ),
        tmp AS( #行业行情起止日期
            SELECT
                s_info_windcode,
                max(trade_dt) end,
                min(trade_dt) start
            FROM
                sw_index_quote
            WHERE
                s_info_windcode = (
                    SELECT
                        s_info_windcode
                    FROM
                        sw_index_quote
                    WHERE
                        s_info_industryname = '{sw_name}'
                    ORDER BY
                        trade_dt DESC
                    LIMIT 1)
            AND
                    trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
            GROUP BY
                s_info_windcode
        )
        SELECT 
            tmp1.s_info_windcode index_code,
            tmp1.pe,
            tmp1.pb,
            tmp3.returns
        FROM 
        (
            SELECT
                a.s_info_windcode,
                end_close/start_close-1  returns
            FROM    
            (
                SELECT
                    s_info_windcode,
                    s_dq_close start_close
                FROM
                    sw_index_quote s
                WHERE
                    s.s_info_windcode = (SELECT s_info_windcode FROM tmp)
                AND
                    s.trade_dt = (SELECT start FROM tmp)
                LIMIT 1
                ) a 
            JOIN
            (
                SELECT
                    s_info_windcode,
                    s_dq_close end_close
                FROM
                    sw_index_quote s
                WHERE
                    s.s_info_windcode = (SELECT s_info_windcode FROM tmp)
                AND
                    s.trade_dt = (SELECT end FROM tmp)
                LIMIT 1
                ) b
            ON
                a.s_info_windcode=b.s_info_windcode
            ) tmp3
            JOIN
                tmp1
            ON
                tmp3.s_info_windcode = tmp1.s_info_windcode
        ''', conn
    )

# 获取某个时间段内，某申万行业指数的所有个股
# 所有进入在该时间段内，存在于该行业的个股，都会被列示出来
def getStocksInSwIndBetween(conn,sw_code:str,startDate:dt.datetime=dt.datetime.today(),endDate:dt.datetime=dt.datetime.today())->pd.DataFrame:
    if len(sw_code)>10:
        sw_code = sw_code[:10]
    return pd.read_sql(f'''
    SELECT
        s_info_code     code,
        s_info_name     name,
        entry_dt,
        remove_dt
    FROM
        nsw_industry_class
    WHERE
        sw_ind_code = '{sw_code}'
    AND
        entry_dt <= '{endDate.strftime("%Y%m%d")}'
    AND
        (remove_dt is null
        OR
        remove_dt > '{startDate.strftime("%Y%m%d")}')
''',conn,parse_dates={'entr_dt':'%Y%m%d','remove_dt':'%Y%m%d'})
    
#根据申万行业代码获取行业名称
def getSwIndName(conn,sw_code:str)->str:
    if len(sw_code)<16:
        sw_code = sw_code+''.join(['0']*(16-len(sw_code)))
    elif len(sw_code)>16:
        sw_code=sw_code[:16]
    name = pd.read_sql(f'''
SELECT DISTINCT 
    industriesname name
FROM
    sw_industry_info
WHERE
    industriescode = '{sw_code}'
''',conn)
    if name.empty:
        return ''
    else:
        return name.iloc[0,0]
    
# 获取申万行业指数回报和PEPB，多行业同时取
def getSwIndReturnsAvePEPB_list(conn, sw_names: list, startDate: dt.datetime, endDate: dt.datetime) -> pd.DataFrame:
    return pd.read_sql(
        f'''
        WITH tmp1 AS( #行业PE与PB数据
            SELECT
                s_info_windcode,
                s_info_industryname,
                avg(s_val_pe) pe,
                avg(s_val_pb) pb
            FROM
                sw_index_quote
            WHERE
                s_info_windcode in (
                    SELECT
                        s_info_windcode
                    FROM
                        (select distinct s_info_windcode, s_info_industryname from sw_index_quote) code_name
                    WHERE
                        s_info_industryname in ({','.join([f"'{x}'" for x in sw_names])})
                    ORDER BY
                        trade_dt DESC
                    )
            AND
                    trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
            GROUP BY
                s_info_windcode,s_info_industryname
        ),
        tmp AS( #行业行情起止日期
            SELECT
                s_info_windcode,
                max(trade_dt) end,
                min(trade_dt) start
            FROM
                sw_index_quote
            WHERE
                s_info_windcode in (
                    SELECT
                        s_info_windcode
                    FROM
                        (select distinct s_info_windcode, s_info_industryname from sw_index_quote) code_name
                    WHERE
                        s_info_industryname in ({','.join([f"'{x}'" for x in sw_names])})
                    ORDER BY
                        trade_dt DESC
                    )
            AND
                    trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
            GROUP BY
                s_info_windcode
        )        
        SELECT 
            tmp1.s_info_windcode index_code,
            s_info_industryname sw_name,
            tmp1.pe,
            tmp1.pb,
            tmp3.returns
        FROM 
        (
            SELECT
                a.s_info_windcode,
                end_close/start_close-1  returns
            FROM    
            (
                SELECT
                    data.s_info_windcode,
                    s_dq_close start_close
                FROM
                    (
                        SELECT s_info_windcode, s_dq_close, trade_dt
                        FROM sw_index_quote
                        WHERE s_info_windcode in (SELECT s_info_windcode FROM tmp)
                        AND trade_dt in (SELECT start FROM tmp)
                        AND s_val_pe is not NULL
                    ) data
                    JOIN tmp
                    ON
                        data.s_info_windcode = tmp.s_info_windcode
                    AND
                        data.trade_dt = tmp.start
            ) a  #取起点行业指数收盘价
            JOIN
            (
                SELECT
                    data.s_info_windcode,
                    s_dq_close end_close
                FROM
                    (
                        SELECT s_info_windcode, s_dq_close, trade_dt
                        FROM sw_index_quote
                        WHERE s_info_windcode in (SELECT s_info_windcode FROM tmp)
                        AND trade_dt in (SELECT end FROM tmp)
                        AND s_val_pe is not NULL
                    ) data
                    JOIN tmp
                    ON
                        data.s_info_windcode = tmp.s_info_windcode
                    AND
                        data.trade_dt = tmp.end
            ) b #取终点行业指数收盘价

            ON
                a.s_info_windcode=b.s_info_windcode
            ) tmp3
            JOIN
                tmp1
            ON
                tmp3.s_info_windcode = tmp1.s_info_windcode
        ''', conn
    )

#获取多个申万行业指数固定周期涨跌幅数据，周度为week/w,月度为month/m
def getSwIndReturnsInPeriods(conn, sw_names: list, startDate: dt.datetime, endDate: dt.datetime,freqNum:int=1,freqType:str='month') -> pd.DataFrame:
    #生成日期序列
    pt = freqType.lower()
    if pt == 'month' or pt=='m':
        dateR = pd.date_range(start=startDate,end=endDate,freq=f'{freqNum if freqNum != 1 else ""}BM') #每月工作日最后一天
    elif pt=='week' or pt=='w':
        dateR = pd.date_range(start=startDate,end=endDate,freq=f'{freqNum if freqNum != 1 else ""}W-FRI') #每周五
    else:
        raise('getSwIndReturnsInPeriods: freqType参数设置错误')
    data = pd.read_sql(f'''
        SELECT
            s_info_windcode,
            s_info_industryname,
            trade_dt,
            s_dq_close,
            opdate
        FROM
            sw_index_quote
        WHERE
            trade_dt between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
        AND
            s_info_industryname in ({','.join([f"'{x}'" for x in sw_names])})
    ''',conn,parse_dates={'trade_dt':'%Y%m%d'})
    #日期筛选
    data = data[data['trade_dt'].isin(dateR.to_pydatetime())]
    #排序
    data.sort_values(['s_info_windcode','trade_dt','opdate'],inplace=True)
    #剔重
    data.drop_duplicates(subset=['s_info_windcode','trade_dt'],keep='last',inplace=True)
    #分组计算收益
    data['simple_returns']=data.groupby('s_info_windcode')['s_dq_close'].apply(lambda x: x / x.shift(1)-1)
    data['log_returns']=data.groupby('s_info_windcode')['s_dq_close'].apply(lambda x: x.apply(math.log) - x.shift(1).apply(math.log))

    return data.pivot(index='trade_dt',columns=['s_info_industryname'],values=['simple_returns','log_returns'])


#获取多个综合指数固定周期涨跌幅数据，周度为week/w,月度为month/m
def getIndexReturnsInPeriods(conn, indexCodes: list, startDate: dt.datetime, endDate: dt.datetime,freqNum:int=1,freqType:str='month') -> pd.DataFrame:
    #生成日期序列
    pt = freqType.lower()
    if pt == 'month' or pt=='m':
        dateR = pd.date_range(start=startDate,end=endDate,freq=f'{freqNum if freqNum != 1 else ""}BM') #每月工作日最后一天
    elif pt=='week' or pt=='w':
        dateR = pd.date_range(start=startDate,end=endDate,freq=f'{freqNum if freqNum != 1 else ""}W-FRI') #每周五
    else:
        raise('getIndexReturnsInPeriods: freqType参数设置错误')
    data = pd.read_sql(f'''
        SELECT
            f4_0001 code,
            f6_0001 name,
            f2_1425 trade_dt,
            f7_1425 close,
            rp_gen_datetime

        FROM
            index_quote
        WHERE
            f2_1425 between '{startDate.strftime('%Y%m%d')}'
                AND
                    '{endDate.strftime('%Y%m%d')}'
        AND
            f4_0001 in ({','.join([f"'{x}'" for x in indexCodes])})
    ''',conn,parse_dates={'trade_dt':'%Y%m%d'})
    #日期筛选
    data = data[data['trade_dt'].isin(dateR.to_pydatetime())]
    #排序
    data.sort_values(['trade_dt','rp_gen_datetime'],inplace=True)
    #剔重
    data.drop_duplicates(subset=['code','trade_dt'],keep='last',inplace=True)
    #分组计算收益
    data['simple_returns']=data.groupby('code')['close'].apply(lambda x: x / x.shift(1)-1)
    data['log_returns']=data.groupby('code')['close'].apply(lambda x: x.apply(math.log) - x.shift(1).apply(math.log))

    return data.pivot(index='trade_dt',columns=['code'],values=['simple_returns','log_returns'])

# 获取一段时间的TTM
def getTTMBetween(conn, codelist: list, startDate: dt.datetime, endDate: dt.datetime, accounts: str, table: str,
                  repType: str = '合并报表',
                  ttmYears=3, opdata: dt.datetime = None, fillDate=True) -> pd.DataFrame:
    # startDate和endDate对应报表披露日期
    tables = {
        'balance': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1853': 'reportPeriod',
            'f3_1853': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1853': 'reportType'
        },
        'income': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1854': 'reportPeriod',
            'f3_1854': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1854': 'reportType'
        },
        'cash': {
            'f4_0001': 'code',
            'f6_0001': 'name',
            'f2_1855': 'reportPeriod',
            'f3_1855': 'reportDate',  # 实际时间为头一天晚间，即此日期为信息已披露的第一天
            'f4_1855': 'reportType'
        },
    }
    dateTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportDate')]  # 获取要查询的表中，reportDate的header名
    periodTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportPeriod')]  # 获取要查询的表中，reportPeriod的header名
    typeTableName = list(tables[table].keys())[
        list(tables[table].values()).index('reportType')]  # 获取要查询的表中，reportType的header名
    data = pd.read_sql(f'''
    SELECT
        f4_0001 code,
        f6_0001 name,
        {periodTableName} periodDate,
        {dateTableName} reportDate,
        {accounts}
    FROM
        {table}
    WHERE
        f4_0001 in ({",".join([f"'{x}'" for x in codelist])})
    AND
        {typeTableName} LIKE '%%{repType}%%'
    AND
        {typeTableName} NOT LIKE '%%单季%%'
    AND
        {dateTableName} BETWEEN
        '{(startDate - relativedelta(years=ttmYears + 2)).strftime('%Y%m%d')}'
        AND
        '{endDate.strftime('%Y%m%d')}'
    ''', conn, parse_dates={'periodDate': '%Y%m%d', 'reportDate': '%Y%m%d'})


    def calTTM(x):
        # print(f'股票代码：{x.name}')
        x.sort_values(by=['periodDate','reportDate'], ascending=[True, True], inplace=True)
        dataToDeal = x.drop_duplicates(subset=['periodDate'], keep='last')
        x.fillna(0, inplace=True)

        def getTTM(dates, stock_data, code):
            columnNames = list(set(stock_data.columns.tolist()).difference(set(['name', 'periodDate', 'reportDate'])))
            # 分报告期计算
            tmp = pd.DataFrame(columns=columnNames)
            if dates.reportDate.month == 12:
                for i in range(ttmYears):
                    # 最近i+1年数据
                    tmpdata = stock_data[
                        (stock_data.periodDate == dates.periodDate - relativedelta(years=i)) &
                        (stock_data.reportDate <= dates.reportDate)].tail(1)[columnNames]
                    if tmpdata.empty:
                        tmpdata.loc[i] = [None] * len(columnNames)
                    else:
                        tmpdata.index = [i]
                    tmp = pd.concat(
                        [tmp,
                         tmpdata]
                    )
            else:
                for i in range(ttmYears):
                    # 最近i+1年数据
                    tmpdata = stock_data[(stock_data.periodDate == dates.periodDate - relativedelta(years=i)) &
                                         (stock_data.reportDate <= dates.reportDate)].tail(1)[columnNames].reset_index(
                        drop=True) - \
                              stock_data[(stock_data.periodDate == dates.periodDate - relativedelta(years=i + 1)) &
                                         (stock_data.reportDate <= dates.reportDate)].tail(1)[columnNames].reset_index(
                                  drop=True) + \
                              stock_data[(stock_data.periodDate == dates.periodDate - relativedelta(years=i + 1,
                                                                                                    month=12, day=31)) &
                                         (stock_data.reportDate <= dates.reportDate)].tail(1)[columnNames].reset_index(
                                  drop=True)
                    if tmpdata.empty:
                        tmpdata.loc[i] = [None] * len(columnNames)
                    else:
                        tmpdata.index = [i]
                    tmp = pd.concat(
                        [tmp, tmpdata]
                    )
            tmp = tmp.unstack().to_frame().T
            tmp.index = [code]
            tmp['', 'reportDate'] = dates.reportDate
            tmp['', 'periodDate'] = dates.periodDate
            return tmp

        return dataToDeal[['periodDate', 'reportDate']].apply(getTTM, stock_data=x.copy(), code=x.name, axis=1,
                                                              result_type='reduce').T.reset_index(drop=True)
    
    data.sort_values(by=['code','periodDate','reportDate'], ascending=[True, True, True], inplace=True)
    #这里只保留最后一次披露的数据，可能是事后更新的数据
    #data.drop_duplicates(subset=['code','periodDate'], keep='last', inplace=True)  # 同一报告期的，保存最后一次披露数据
    data.drop_duplicates(subset=['code','periodDate','reportDate'], keep='last', inplace=True) #数据去重
    tmpd = data.groupby('code').apply(calTTM)

    if len(codelist) == 1:
        data = pd.concat(filter(lambda u: u is not np.nan, tmpd.unstack().values))
    else:
        data = pd.concat(filter(lambda u: u is not np.nan, tmpd.unstack().values.flatten()))
    data.reset_index(inplace=True)
    
    
    data = data[data[('','reportDate')] >= startDate]
    data.sort_values(by=[('index',''),('','reportDate'),('','periodDate')],inplace=True)
    data = data[~((data[('','periodDate')]<data.shift(1)[('','periodDate')]) & (data[('index','')]==data.shift(1)[('index','')]))]
    # columns index 2级转1级
    def rename(columns):
        newNames = []
        for multiName in columns:
            singleName = ''
            nums = 0
            for name in multiName:
                if name !='':
                    if nums != 0:
                        singleName +=','
                    if len([ x for x in multiName if x!=''])>1 and isinstance(name,str):
                        singleName += f"'{name}'"
                    else:
                        singleName += f"{name}"
                    nums +=1
            if nums > 1:
                singleName = f"({singleName})"
            newNames.append(singleName)
        return newNames
    data.columns = rename(data.columns)
    data.dropna(how='all',inplace=True)
    if not fillDate:
        return data.rename(columns={'index':'code'})
    else:
        it_product = list(zip(it.product(codelist, pd.date_range(startDate, endDate))))
        returnlist = pd.DataFrame(np.array(it_product).reshape(len(it_product), 2), columns=['code', 'reportDate'])
        # returnlist = pd.DataFrame(zip(*it.product(codelist,pd.date_range(startDate,endDate))),index=['code','reportDate']).T
        returnlist = pd.merge(returnlist, data,
                            left_on=['code', 'reportDate'],
                            right_on=["index","reportDate"],
                            how="outer")
        #returnlist.rename(columns={('', 'periodDate'): 'periodDate'}, inplace=True)
        returnlist.drop('index', axis=1, inplace=True)
        return returnlist.fillna(returnlist.groupby('code').ffill()).dropna()

# 取指定指数，在指定日期的成份权重，通常只在月末有披露数据，predict可根据近期个股涨跌，推测出最新权重
def getIndexWeight(conn,indexCode:str,endDate:dt.datetime=dt.date.today(),predict:bool=False)->pd.DataFrame:
    #注意函数返回的日期，可能存在YYYY-MM-DD与YYYYMMDD两种格式
    data = pd.read_sql(f'''
    SELECT
        stock_code code,
        trade_date date,
        weight_value weight
    FROM
        index_weight
    WHERE
        index_code = '{indexCode}'
    AND
        trade_date = (
            SELECT
                MAX(trade_date)
            FROM
                index_weight
            WHERE
                index_code = '{indexCode}'
            AND
                trade_date <= '{endDate.strftime('%Y%m%d')}'
        )
    ''',conn)
    #统一日期格式
    data.loc[:,'date']=data.date.str.replace('-','')
    data.set_index('code',inplace=True)
    startDate = dt.datetime.strptime(data.date.unique()[0],'%Y%m%d')
    if predict and startDate<endDate:
        codelist = data.index.tolist()
        returns  = getStockReturns(conn,codelist,startDate,endDate).returns
        returns = returns + 1
        data = data.join(returns)
        data['predict_date']=endDate
        data.loc[:,'weight_predict']=data['weight']*data['returns']
        data.loc[:,'weight_predict']=data['weight_predict']/(data['weight_predict'].sum())*100
        data.drop('returns',axis=1,inplace=True)
    return data


# 取指定指数，在指定日期区间的的成份权重，通常只在月末有披露数据，predict可根据近期个股涨跌，推测出最新权重
def getIndexWeightBetween(conn, indexCode: str, startDate: dt.datetime, endDate: dt.datetime = dt.date.today()) -> pd.DataFrame:
    # 注意函数返回的日期，可能存在YYYY-MM-DD与YYYYMMDD两种格式
    data = pd.read_sql(f'''
    SELECT
        stock_code code,
        trade_date date,
        weight_value weight
    FROM
        index_weight
    WHERE
        index_code = '{indexCode}'
    AND
        trade_date BETWEEN {startDate.strftime('%Y%m%d')}
                 AND {endDate.strftime('%Y%m%d')}
    ''', conn)
    # 统一日期格式
    data.loc[:, 'date'] = data.date.str.replace('-', '')
    return data

#取指数在指定日期区间的涨跌幅，日期要准确匹配到交易日，非交易日会导致数据异常
def getIndexReturnsExactdate(conn,indexCodeList,startDate:dt.date,endDate:dt.date,logReturns:bool=False)->pd.DataFrame:
    return pd.read_sql(f'''
    SELECT
        open.f4_0001 as code,
        {'close.close/open.open - 1' if not logReturns else 'LOG(close.close/open.open)'} as returns
        FROM
        (
            SELECT
                f4_0001,
                f7_1425 open
            FROM
                index_quote
            WHERE
                    f4_0001 in ({','.join([f"'{code}'" for code in indexCodeList])})
                AND
                    f2_1425 = '{startDate.strftime("%Y%m%d")}'
        ) open
        JOIN
        (
            SELECT
                f4_0001,
                f7_1425 close
            FROM
                index_quote
            WHERE
                    f4_0001 in ({','.join([f"'{code}'" for code in indexCodeList])})
                AND
                    f2_1425 = '{endDate.strftime("%Y%m%d")}'
        )close
        ON
            open.f4_0001 = close.f4_0001;
    ''',conn,parse_dates={'date':'%Y%m%d'})


def getIndexDailyReturns(conn,indexCodeList,startDate:dt.date,endDate:dt.date)->pd.DataFrame:
    d = pd.read_sql(
        f'''
          SELECT
              f4_0001 code,
              f2_1425 date,
              f7_1425 close
          FROM
              index_quote
          WHERE
                  f4_0001 in ({','.join([f"'{code}'" for code in indexCodeList])})
              AND
                  f2_1425 BETWEEN
                      '{startDate.strftime('%Y%m%d')}'
                  AND
                      '{endDate.strftime('%Y%m%d')}'
          ''', conn, parse_dates={'date':'%Y%m%d'}
    )
    d.drop_duplicates(['date', 'code'], inplace=True)
    d = d.sort_values('date').reset_index(drop=True)
    d['returns'] = d.close.pct_change()
    return d

#返回指定长度的和指定半衰期的权重序列
def halfLifeWeight(length:int,halflife:int)->list:
    alpha = 1-pow(math.e , math.log(0.5)/halflife)
    return [pow(1-alpha, length-x-1) for x in range(length)]

def get_trade_list(start_date:dt.datetime, end_date:dt.datetime,n:int=3):
    # 默认n=3 周四
    day_list = list(filter(lambda x: x.weekday() == n, pd.date_range(start_date, end_date).tolist()))
    trade_list = getCalendar(start_date-relativedelta(days=30), end_date)
    # trade_list = list(filter(lambda x: x not in [dt.datetime(2022,10,6),dt.datetime(2022,10,7)],trade_list))
    def cal_trade_day(x):
        if x in trade_list:
            return x
        else:
            x = x - relativedelta(days=1)
            return cal_trade_day(x)
    day_list = list(map(lambda y: cal_trade_day(y), day_list))
    return day_list

def get_factor_data(conn,table_name:str,start_date:dt.datetime,end_date:dt.datetime,accounts=[], chunk=False, hfile=sys.stdout):
    """
    常用于 factors和alphas两个库
    """
    print(f'{timeStr()}{table_name} 获取开始!',file = hfile, flush=True)
    if chunk:
        factor_data_chunk = pd.read_sql(
            f"select * from {table_name} where date between {start_date.strftime('%Y%m%d')} and {end_date.strftime('%Y%m%d')}",
            conn, parse_dates={'Date': '%Y%m%d'},chunksize=200000)
        factor_data = pd.DataFrame()
        for chunk_i in factor_data_chunk:
            factor_data = factor_data.append(chunk_i)
     
    else:
        if accounts == []:
            factor_data = pd.read_sql(f"select * from {table_name} where date \
                                between '{start_date.strftime('%Y%m%d')}' and '{end_date.strftime('%Y%m%d')}'",conn, parse_dates={'Date': '%Y%m%d'})
        else:
            factor_data = pd.read_sql(f"select {','.join(accounts)} from {table_name} where date \
                                between '{start_date.strftime('%Y%m%d')}' and '{end_date.strftime('%Y%m%d')}'",conn,parse_dates={'Date': '%Y%m%d'})
        if accounts == []:
            factor_data = pd.read_sql(f"select * from {table_name} where date \
                                between '{start_date.strftime('%Y%m%d')}' and '{end_date.strftime('%Y%m%d')}'",conn, parse_dates={'Date': '%Y%m%d'})
        else:
            factor_data = pd.read_sql(f"select {','.join(accounts)} from {table_name} where date \
                                between '{start_date.strftime('%Y%m%d')}' and '{end_date.strftime('%Y%m%d')}'",conn,parse_dates={'Date': '%Y%m%d'})
    print(f'{timeStr()}{table_name} 获取结束！',file = hfile, flush=True)
    return factor_data

def get_TTM_data(conn, start_date:dt.datetime, end_date:dt.datetime, hfile=sys.stdout):
    print(f'{timeStr()} 开始获取TTM数据',file=hfile)
    TTM_data_chunk = pd.read_sql(
        f"select * from TTMdata where reportDate between '{start_date.strftime('%Y-%m-%d')}' and '{end_date.strftime('%Y-%m-%d')}'",
        conn,chunksize=10000)
    TTM_data = pd.DataFrame()
    for chunk_i in TTM_data_chunk:
        TTM_data = TTM_data.append(chunk_i)
    TTM_data.drop_duplicates(['code','reportDate'],keep='first',inplace=True)
    trade_list = sorted([pd.to_datetime(i.strftime('%Y-%m-%d')) for i in getCalendar(start_date,end_date+relativedelta(days=10)).to_list()])
    def cal_trade_day(x):
        if x in trade_list:
            return x
        else: 
            x = x + relativedelta(days=1)
            return cal_trade_day(x)
    TTM_data.reportDate = TTM_data.reportDate.apply(lambda x: cal_trade_day(x))
    print(f'{timeStr()} TTM数据获取结束', file=hfile)
    return TTM_data

#提取综合指数价格序列
def getIndexQuoteBetween(conn,codelist:list,start_date:dt.datetime,end_date:dt.datetime)->pd.DataFrame:
    d = pd.read_sql(        
        f'''
          SELECT DISTINCT
              f4_0001 code,
              f2_1425 date,
              f7_1425 close
          FROM
              index_quote
          WHERE
                  f4_0001 in ({','.join([f"'{code}'" for code in codelist])})
              AND
                  f2_1425 BETWEEN
                      '{start_date.strftime('%Y%m%d')}'
                  AND
                      '{end_date.strftime('%Y%m%d')}'
          ORDER BY
            f2_1425
          ''', conn, parse_dates={'date':'%Y%m%d'}
    )
    return d


if __name__ =='__main__':

    start_date = dt.datetime(2023,1,1)
    end_date = dt.datetime(2020,10,31)
    conn=getConn()
    # a = getFinance(conn,['600519'],end_date,'F9_1854,F10_1854','income')
    # a = getSwInd(conn,['688608'],end_date)
    # tmp_stock_price = getMarketTradingCode(conn, start_date, end_date,memtableName='quote_val_mem')
    # import time
    # start = time.time()
    # a = getMarketTradingCode(conn,start_date,end_date,memtableName='quote_val_mem')
    # end = time.time() - start
    # print('1:', end)
    # tmp_stock_price = getStockPrice(conn, a, start_date, end_date,
    #                                        accounts='close,amount,volume,low,high,open',memtableName='quote_mem')

    # start = time.time()
    # b = getStockDB(conn,start_date,end_date)
    # end = time.time() - start
    # print('2:', end, '个数：',len(a))

    # a = getCalendarDB(conn,dt.datetime(2023,4,20),dt.datetime(2023,5,20),freq='w-wed')
    # conn_alphas = getConn(database='alphas')
    # conn_factors = getConn(database='factors')
    # start = time.time()
    # Alpha1001_list = pd.read_sql('select * from Alpha1001_mem limit 1',con=conn_factors).columns.tolist()

    # a = pd.read_sql(f"select  {','.join(Alpha1001_list)} from Alpha1001_mem where date between '{start_date.strftime('%Y-%m-%d')}' and '{end_date.strftime('%Y-%m-%d')}'",con=conn_factors)
    # print(len(a))
    # print(time.time()-start)
    # b = pd.read_sql(f"select {','.join(Alpha1001_list)} from Alpha1001_1022 where date between '{start_date.strftime('%Y-%m-%d')}' and '{end_date.strftime('%Y-%m-%d')}'",con=conn_factors)
    # print(len(b))
    # a = get_factor_data(conn_factors,'Alpha102_mem',start_date,end_date)
    # alpha101_list = pd.read_sql('select * from worldquant101 limit 1',con=conn_alphas).columns.tolist()
    # b = get_factor_data(conn_factors,'Alpha102_155',start_date,end_date)
    # factor_data = pd.read_sql(f"select * from Alpha102_mem where date \
    #                             between '{start_date.strftime('%Y-%m-%d')}' and '{end_date.strftime('%Y-%m-%d')}'",conn_factors)
    # factor_data_1001 = pd.read_sql(f"select {','.join(Alpha102_list)} from Alpha1001_mem where date \
    #                             between '{start_date.strftime('%Y-%m-%d')}' and '{end_date.strftime('%Y-%m-%d')}'",conn_factors)
    # 

    # print(len(factor_data))
    # print(time.time()-start)
    # alpha101_mem = {
    #     'dbName': 'alphas',
    #     'From': 'worldquant101',
    #     'To': 'alpha101_mem',
    #     'accounts':alpha101_list,
    #     'dtypes': ['datetime', 'int']+['float']*(len(alpha101_list)-2),
    #     'indexNames': ['index_date'],
    #     'indexCols': ['Date']}
    # # conn=getConn()
    # cleanMemTables(conn, ['factors','factors','alphas'],['Alpha1001_mem','Alpha102_mem','alpha101_mem'])
    # createMemTable(conn,memtables['Alpha102_mem'],silent=False)
    # createMemTable(conn,memtables['Alpha1001_mem'],silent=False)
    # createMemTable(conn,alpha101_mem,silent=False)
    # mc = getMarketTradingCode(conn,start_date,end_date,memtableName='quote_val_mem')
    # codelist = mc.code.transform(lambda x: str(x).zfill(6)).unique().tolist()
    # import random
    # random.shuffle(codelist)
    # ttm = getTTMBetween(conn, codelist[:3], start_date, end_date, 
    #             'f55_1854,f9_1854,f61_1854,f83_1854','income', ttmYears=5,fillDate=False)
    fillDate(conn)
    cleanMemTables(conn, ['finance','finance'],['quote_mem','quote_val_mem'])
    # cleanMemTables(conn, ['finance'],['quote_val_mem'])
    createMemTable(conn,memtables['quote_mem'],silent=False)
    createMemTable(conn,memtables['quote_val_mem'],silent=False)
