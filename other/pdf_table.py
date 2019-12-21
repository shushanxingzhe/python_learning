import camelot
import os
import re
import pandas as pd

# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
#
# def getPdfInfo(path):
#     res = {}
#
#     # 创建一个文档分析器
#     parser = PDFParser(path)
#     # 创建一个PDF文档对象存储文档结构
#     document = PDFDocument(parser)
#     # 判断文件是否允许文本提取
#     if not document.is_extractable:
#         raise PDFTextExtractionNotAllowed
#     else:
#         # 创建一个PDF资源管理器对象来存储资源
#         resmag = PDFResourceManager()
#         # 设定参数进行分析
#         laparams = LAParams()
#         # 创建一个PDF设备对象
#         # device=PDFDevice(resmag)
#         device = PDFPageAggregator(resmag, laparams=laparams)
#         # 创建一个PDF解释器对象
#         interpreter = PDFPageInterpreter(resmag, device)
#         paypal_id = re.compile(r'PayPal( ID|用户名)\: (.*)\n')
#         date = re.compile(r'(\d+)/(\d+)/(\d+) \- \d+/\d+/\d+\n')
#         # 处理每一页
#         for page in PDFPage.create_pages(document):
#             interpreter.process_page(page)
#             # 接受该页面的LTPage对象
#             layout = device.get_result()
#             for y in layout:
#                 text = y.get_text()
#                 id_match = paypal_id.match(text)
#                 if id_match:
#                     res['paypal_id'] = id_match.group(2)
#                 else:
#                     date_match = date.match(text)
#                     if date_match:
#                         res['date'] = "%s-%s" % (date_match.group(3), date_match.group(1))
#                         return res


directories = os.listdir('data')

translate_map = {'退单调整': 'Chargeback Adjustments',
                 '退单放款': 'Chargeback Releases',
                 '退单冻结': 'Chargeback Hold',
                 '退单活动': 'Chargeback Activity',
                 '退单撤销': 'Chargeback Reversals'}

result = []
paypal_id = re.compile(r'PayPal( ID|用户名)\: (.*)')
date = re.compile(r'(\d+)/(\d+)/(\d+) \- \d+/\d+/\d+')

for f in directories:
    fpath = 'data/' + f
    # with open(fpath, mode='rb') as file:
    #     info = getPdfInfo(file)
    try:
        tables = camelot.read_pdf(fpath, pages='3,4', flavor='stream')
    except Exception as e:
        print('no page:', fpath)
        continue

    item = {'date': '', 'user': '', 'Currency': '', 'Chargeback Activity': 0,
            'Chargeback Adjustments': 0, 'Chargeback Hold': 0, 'Chargeback Releases': 0, 'Chargeback Reversals': 0,
            'Total': 0}

    for table in tables:
        yes = False
        data = {}
        col_map = {}

        if fpath in ['data/moremoremoneycomehere@gmail.com-201911.PDF', 'data/paymentsfromkingdomofbeer@gmail.com-201911.PDF', 'data/Wearewaitingforyoubaby@gmail.com-201911.PDF']:
            fpath
        line = ''.join(table.data[0])
        head = table.data[0]
        if line == 'PayPal ID:' or line == 'PayPal用户名:':
            head = table.data[1]
        for v in head:
            id_match = paypal_id.match(v)
            if id_match:
                item['user'] = id_match.group(2)
            else:
                date_match = date.match(v)
                if date_match:
                    item['date'] = "%s-%s" % (date_match.group(3), date_match.group(1))
                    if len(item['user']) == 0:
                        item['user'] = ''.join(table.data[2]).strip()
                    break

        for row in table.data:
            if row[0] == 'C\nhargeback' or row[0] == '退\n单':
                yes = True
                continue
            if yes:
                if row[0] == 'Description' or row[0] == '说明':
                    col_map = {}
                    for idx, col in enumerate(row[1:]):
                        col_map[idx] = col
                else:
                    for idx, col in enumerate(row[1:]):
                        if col_map[idx] not in data:
                            data[col_map[idx]] = {}

                        if row[0] in translate_map:
                            row[0] = translate_map[row[0]]
                        data[col_map[idx]][row[0]] = col.strip().replace(',', '')

        for cur in data:
            row = item.copy()
            if len(row['user']) == 0 or len(row['date']) == 0:
                print('user date:', fpath)
            row['Currency'] = cur
            keep = False
            for k in data[cur]:
                row[k] = data[cur][k]
                if len(data[cur][k]) and float(data[cur][k]) > 0.0:
                    keep = True
            if keep:
                result.append(row)

df = pd.DataFrame(result)
df.index += 1
df.to_excel('result.xlsx', index_label='序号', columns=['date', 'user', 'Currency', 'Chargeback Adjustments',
                                                   'Chargeback Releases', 'Chargeback Hold', 'Chargeback Activity',
                                                   'Chargeback Reversals'],
          header=['日期', '账号', '币别', 'Chargeback Adjustments(退单调整)', 'Chargeback Releases(退单放款)',
                  'Chargeback Hold(退单冻结)', 'Chargeback Activity(退单活动)', 'Chargeback Reversals(退单撤销)'])
