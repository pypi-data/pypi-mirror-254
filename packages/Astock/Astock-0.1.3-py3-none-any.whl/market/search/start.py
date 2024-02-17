import pandas as pd
import pkg_resources

def start():
    sheetsNames = ['资产负债表','利润表','现金流量表','财务衍生表']
    sheetsInMysql = ['balance','income','cash','derivative']
    data = None
    for sheet,sqlName in zip(sheetsNames,sheetsInMysql):
        filename = pkg_resources.resource_filename(__name__,'finance_keys_20201023.xlsx')
        tmp = pd.read_excel(filename,sheet_name=sheet)
        tmp = tmp[['字段名','字段中文名']]
        tmp['sheetName']=sqlName
        data = pd.concat([data,tmp])
    data.drop_duplicates(subset=['字段名','字段中文名'],inplace=True)
    print('输入需要查询的字段，输入 exit 则退出')
    keyword = ''
    while(keyword.lower()!='exit'):
        keyword = input("\033[1;31m查询\033[0m  ")
        if keyword.lower()=='exit':
            break
        print('----------------查询结果--------------')
        tmp = data[data['字段中文名'].str.contains(keyword)]
        if tmp.empty:
            print('没有匹配的选项，请重新查询')
            continue
        
        maxLen = [tmp['字段中文名'].apply(len).max()*2,tmp['字段名'].apply(len).max(),tmp['sheetName'].apply(len).max()]
        tablen=4
        w0='\033[7m字段中文名\033[0m'
        w1='\033[7m字段名\033[0m'
        w2='\033[7m表名\033[0m'
        print(f"{w0:<{maxLen[0]+3+tablen}}{w1:<{maxLen[1]+5+tablen}}{w2:<{maxLen[2]+2+tablen}}")
        for line in tmp.iterrows():
            chineseNum =0
            for char in line[1]['字段中文名']:
                if u'\u4e00'<= char<=u'\u9fa5' or char in [r'／',r'、',r'：']:
                    chineseNum+=1
            print(f"{line[1]['字段中文名']:<{maxLen[0]-chineseNum+tablen}}{line[1]['字段名'].lower():<{maxLen[1]+tablen}}{line[1]['sheetName']:<{maxLen[2]+tablen}}")


