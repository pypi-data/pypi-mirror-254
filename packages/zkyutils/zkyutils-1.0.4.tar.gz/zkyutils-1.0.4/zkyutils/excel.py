# excel 读写操作
import pandas as pd


def read(filename, headers):
    result_list = []
    engine = 'openpyxl'
    if filename[-3:] == 'xls':
        engine = 'xlrd'
    df = pd.ExcelFile(filename, engine=engine)

    for sheet in df.sheet_names:
        df_data = pd.read_excel(df, sheet, usecols=headers, engine=engine)
        result_list.extend(df_to_list(df_data, headers))
    return result_list


def write(filename, data_list, headers):
    # 初始化写入信息
    result_data = {}
    for header in headers:
        result_data[header] = []

    # 将结果写入excel
    for result in data_list:
        for header in headers:
            if header in result.keys():
                result_data[header].append(result[header])
            else:
                result_data[header].append('')

    df = pd.DataFrame(result_data)
    df.to_excel(filename, sheet_name='Sheet1', index=False)  # index = False表示不写入索引


def df_to_list(df, headers):
    data_list = []
    len_data = len(df)
    for i in range(len_data):
        row = {}
        empty_row = True
        for header in headers:
            row[header] = ''
            col = df.get(header)
            if col is None:
                continue
            value = col.get(i)
            if pd.isna(value):
                value = ''
            if type(value) is str:
                value = value.strip()
            if value != '':
                empty_row = False
            row[header] = value
        if not empty_row:
            if len(headers) == 1:
                data_list.append(row[headers[0]])
            else:
                data_list.append(row)
    return data_list

