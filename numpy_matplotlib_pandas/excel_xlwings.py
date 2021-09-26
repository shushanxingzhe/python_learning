import pandas as pd
import xlwings as xw
from datetime import date
import numpy as np

path = ''
file = path + '8月US薄膜键盘.xlsx'
df = pd.read_excel(file)


def insert_table(col, row, sheet, name, data):
    if type(name) == list and len(name) > 1:
        orderby = name.copy()
        orderby[-1] = '市场份额'
        index_cols_size = len(name)
        mutil_index = True
    else:
        orderby = '市场份额'
        index_cols_size = 1
        mutil_index = False

    cur = pd.pivot_table(data, index=name, values=['Asin', '预估日销', '市场份额'], observed=True,
                         aggfunc={'Asin': np.size, '预估日销': np.sum, '市场份额': np.sum})
    if mutil_index:
        index_sum = cur.groupby(by=orderby[:-1])['市场份额'].sum().reset_index().rename({'市场份额': 'index_sum'}, axis=1)
        cur.reset_index(inplace=True)
        cur = cur.merge(index_sum, how='left', on=orderby[0])
        cur.sort_values(by=['index_sum', '市场份额'], ascending=False, inplace=True)
        cur.set_index(name, inplace=True)
        cur = cur[['Asin', '预估日销', '市场份额']]
    else:
        cur.sort_values(by=orderby, ascending=False, inplace=True)
        cur = cur[['Asin', '预估日销', '市场份额']]

    start_pos = col + str(row)
    sheet.range(start_pos).value = cur
    table = sheet.tables.add(source=sheet.range(start_pos).expand(), table_style_name='TableStyleMedium21')
    table.show_autofilter = False
    table.show_table_style_row_stripes = False
    sheet.range(chr(ord(col) +2 + index_cols_size) + str(row)).expand('down').api.NumberFormat = '0.00%'
    bottom = row + len(cur) + 1
    sheet.range(col + str(bottom)).value = '总计'
    sheet.range('%s:%s' % (chr(ord(col) + index_cols_size) + str(bottom), chr(ord(col) + len(cur.columns)+index_cols_size-1) + str(bottom))).formula =\
        '=sum(%s:%s)' % (chr(ord(col) + index_cols_size) + str(row + 1), chr(ord(col) + index_cols_size) + str(bottom - 1))
    if mutil_index:
        range_index = '%s:%s' % (col + str(row+1), col + str(row+len(cur)))
        index_values = sheet.range(range_index).value
        for i in range(len(index_values)-1, 0, -1):
            if index_values[i] == index_values[i-1]:
                index_values[i] = None
        sheet.range(range_index).options(transpose=True).value = index_values

    return row + len(cur) + 3


try:
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(file)

    exist = False
    sheet_name = '数据分析'
    for sht in wb.sheets:
        if sht.name == sheet_name:
            exist = True
            break

    if exist:
        del wb.sheets[sheet_name]

    sheet = wb.sheets.add(sheet_name, after=wb.sheets[0])

    sample = df['预估日销'].sum()
    sales_volume = int(sample / 0.8)

    month = date.today().strftime('%Y年%m月')
    sheet.range('A1').options(expand='table').value = [['一、基本情况', None, None], ['时间', '采样值', '市场容量'], [month, sample, sales_volume]]
    sheet.range('A1').autofit()
    sheet.range('A1:C1').color = (255, 192, 0)
    sheet.range('B:B').options(ndim=1).api.HorizontalAlignment = -4108
    sheet.range('I:I').options(ndim=1).api.HorizontalAlignment = -4108
    sheet.range('P:P').options(ndim=1).api.HorizontalAlignment = -4108

    left_height = middle_height = right_height = 5
    # 是否有线	是否带支架	结构	 键区	光效	 外观	材质	 连接方式	是否可充电	颜色
    left_height = insert_table('A', left_height, sheet, '是否有线', df)
    left_height = insert_table('A', left_height, sheet, '是否带支架', df)
    left_height = insert_table('A', left_height, sheet, '结构', df)
    left_height = insert_table('A', left_height, sheet, '连接方式', df)
    left_height = insert_table('A', left_height, sheet, '是否可充电', df)
    left_height = insert_table('A', left_height, sheet, '光效', df)
    left_height = insert_table('A', left_height, sheet, '键区', df)

    middle_height = insert_table('H', middle_height, sheet, '外观', df)
    middle_height = insert_table('H', middle_height, sheet, '材质', df)
    middle_height = insert_table('H', middle_height, sheet, '颜色', df)
    middle_height = insert_table('H', middle_height, sheet, '价格区间', df)

    right_height = insert_table('O', right_height, sheet, '品牌', df)
    right_height = insert_table('O', right_height, sheet, '评分区间', df)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 1
    sheet.range('A' + str(left_height)).value = '二、品牌维度'
    sheet.range('A' + str(left_height)).autofit()
    sheet.range('A' + str(left_height)).color = (255, 192, 0)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 2

    left_height = insert_table('A', left_height, sheet, ['是否带支架', '品牌'], df)
    left_height = insert_table('A', left_height, sheet, ['结构', '品牌'], df)
    left_height = insert_table('A', left_height, sheet, ['连接方式', '品牌'], df)
    left_height = insert_table('A', left_height, sheet, ['外观', '品牌'], df)

    middle_height = insert_table('H', middle_height, sheet, ['材质', '品牌'], df)
    middle_height = insert_table('H', middle_height, sheet, ['价格区间', '品牌'], df)
    middle_height = insert_table('H', middle_height, sheet, ['是否有线', '品牌'], df)
    middle_height = insert_table('H', middle_height, sheet, ['键区', '品牌'], df)

    right_height = insert_table('O', right_height, sheet, ['颜色', '品牌'], df)
    right_height = insert_table('O', right_height, sheet, ['光效', '品牌'], df)
    right_height = insert_table('O', right_height, sheet, ['是否可充电', '品牌'], df)
    right_height = insert_table('O', right_height, sheet, ['评分区间', '品牌'], df)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 1
    sheet.range('A' + str(left_height)).value = '三、价格区间维度'
    sheet.range('A' + str(left_height)).autofit()
    sheet.range('A' + str(left_height)).color = (255, 192, 0)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 2

    left_height = insert_table('A', left_height, sheet, ['结构', '价格区间'], df)
    left_height = insert_table('A', left_height, sheet, ['键区', '价格区间'], df)
    left_height = insert_table('A', left_height, sheet, ['外观', '价格区间'], df)

    middle_height = insert_table('H', middle_height, sheet, ['是否有线', '价格区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['是否带支架', '价格区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['连接方式', '价格区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['光效', '价格区间'], df)

    right_height = insert_table('O', right_height, sheet, ['颜色', '价格区间'], df)
    right_height = insert_table('O', right_height, sheet, ['是否可充电', '价格区间'], df)
    right_height = insert_table('O', right_height, sheet, ['材质', '价格区间'], df)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 1
    sheet.range('A' + str(left_height)).value = '四、评分维度'
    sheet.range('A' + str(left_height)).autofit()
    sheet.range('A' + str(left_height)).color = (255, 192, 0)

    left_height = middle_height = right_height = max(left_height, middle_height, right_height) + 2

    left_height = insert_table('A', left_height, sheet, ['结构', '评分区间'], df)
    left_height = insert_table('A', left_height, sheet, ['光效', '评分区间'], df)
    left_height = insert_table('A', left_height, sheet, ['外观', '评分区间'], df)

    middle_height = insert_table('H', middle_height, sheet, ['材质', '评分区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['是否有线', '评分区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['是否带支架', '评分区间'], df)
    middle_height = insert_table('H', middle_height, sheet, ['连接方式', '评分区间'], df)

    right_height = insert_table('O', right_height, sheet, ['键区', '评分区间'], df)
    right_height = insert_table('O', right_height, sheet, ['颜色', '评分区间'], df)
    right_height = insert_table('O', right_height, sheet, ['是否可充电', '评分区间'], df)

    wb.save(file.replace('.xlsx', '-结果.xlsx'))
finally:
    app.quit()



# result_df = pd.DataFrame()
# app = xw.App(visible=False, add_book=False)
# wb = app.books.open('inventory_price_template.xlsm')
# sheet = wb.sheets['Default']
# # row_counter = 4
# # for row in result:
# #     sheet.range('A'+str(row_counter)).value = [row.sku, row.price,row.quantity]
# #     row_counter += 1
# sheet.range('A4').options(transpose=True).value = result_df['sku'].values
# sheet.range('C4').options(transpose=True).value = result_df['price'].values
# sheet.range('D4').options(transpose=True).value = result_df['quantity'].values
#
# wb.save('inventory_price.xlsm')
# app.quit()