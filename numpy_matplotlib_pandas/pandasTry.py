import pandas as pd
import numpy as np

data = [
    {'query': 'xiaomi', 'exposecount': 10, 'clickcount': 9, 'catId': 'C9'},
    {'query': 'huawei', 'exposecount': 10, 'clickcount': 4, 'catId': 'C4'},
    {'query': 'pants', 'exposecount': 10, 'clickcount': 5, 'catId': 'C5'},
    {'query': 'phone', 'exposecount': 1024, 'clickcount': 30, 'catId': 'C3'},
    {'query': 'xiaomi', 'exposecount': 10, 'clickcount': 10, 'catId': 'C10'},
    {'query': 'xiaomi', 'exposecount': 10, 'clickcount': 13, 'catId': 'C13'},
    {'query': 'xiaomi', 'exposecount': 10, 'clickcount': 14, 'catId': 'C14'},
    {'query': 'huawei', 'exposecount': 10, 'clickcount': 5, 'catId': 'C5'},
    {'query': 'pants', 'exposecount': 10, 'clickcount': 9, 'catId': 'C9'},
    {'query': 'shoes', 'exposecount': 8, 'clickcount': 8, 'catId': 'C8'},
    {'query': 'clothes', 'exposecount': 101, 'clickcount': 1, 'catId': 'C9'},
    {'query': 'watches', 'exposecount': 10, 'clickcount': 0, 'catId': 'C9'},
]

df = pd.DataFrame(data)
df = df.sort_values(by=['query', 'clickcount'], ascending=[True, False])

print(df)

df1 = df.groupby(by='query').aggregate({'exposecount': 'sum', 'clickcount': 'sum', 'catId': lambda x: list(x)[0:3]})
df1['ctr'] = df1['clickcount'] / df1['exposecount']

print(df1)

test1 = df1[(df1['exposecount'] >= 1000) & (df1['ctr'] >= 0.01)]
test2 = df1[(df1['exposecount'] < 1000) & (df1['exposecount'] > 10) & (df1['ctr'] >= 0.01)]
test3 = df1[((df1['exposecount'] < 10) & (df1['ctr'] >= 0.01)) | ((df1['clickcount'] > 0) & (df1['ctr'] < 0.01))]
test4 = df1[(df1['clickcount'] == 0)]

print(df1)

print('\n\ntest dataset 1')
print(test1)
print('\n\ntest dataset 2')
print(test2)
print('\n\ntest dataset 3')
print(test3)
print('\n\ntest dataset 4')
print(test4)

one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
    'Marks_scored': [98, 90, 87, 69, 78]},
    index=[1, 2, 3, 4, 5])
two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5'],
    'Marks_scored': [89, 80, 79, 97, 88]},
    index=[1, 2, 3, 4, 5])
rs = pd.concat([one, two], ignore_index=True)
print(rs)

left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']})
right = pd.DataFrame(
    {'id': [1, 2, 3, 4, 5],
     'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
     'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']})
rs = pd.merge(left, right, on='subject_id', how='inner')
print(rs)

# change data in dataframe
# df.loc[df['query'] == query, 'label'] = label

# import pandas as pd
#
# labeled_df = pd.read_excel('result1.xlsx')
# result_df = pd.read_csv('result1.csv')
#
# for _,row in result_df.iterrows():
#     labeled_row = labeled_df[(labeled_df['query'] == row['query'])].iloc[-1]
#     result_df.loc[result_df['query'] == row['query'], '统计命中'] = str(labeled_row['统计命中'])
#     if row['pred_catId'] == labeled_row['模型分类ID']:
#         result_df.loc[result_df['query'] == row['query'], '模型命中'] = str(labeled_row['模型命中'])
#     elif row['pred_catId'] == labeled_row['统计分类ID']:
#         result_df.loc[result_df['query'] == row['query'], '模型命中'] = str(labeled_row['统计命中'])
#
# result_df.to_csv('new_result1.csv',index=False)


data = {
    'itemid': np.linspace(1, 300, 300, dtype=int),
    'category': np.random.randint(1, 31, 300),
    'ctr': np.random.random(300)
}

df = pd.DataFrame(data)
df = df.sort_values(['category', 'ctr'], ascending=False).groupby(['category'], as_index=False).head(5).reset_index(
    drop=True)
pd.set_option('display.max_rows', None)
print(df)
