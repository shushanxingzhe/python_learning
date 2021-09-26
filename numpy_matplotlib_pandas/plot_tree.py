from anytree import Node, RenderTree
import pandas as pd

# import pymongo
#
# client = pymongo.MongoClient('10.60.47.53', 10086)
# db = client.get_database('search')
# category = db['category_info_10002']
# gearbest_category_data = list(category.find({}))
#
# category_name_map = {}
# for item in gearbest_category_data:
#     category_name_map[item['category_id']] = item['category_name']
#
# source_df = pd.read_csv('F:/Download/gearbest_category.csv')
#
# result = []
# for _,row in source_df.iterrows():
#     row = row.to_dict()
#     if row['catid'] not in category_name_map:
#         print(row['catid'])
#         continue
#     row['catname'] = category_name_map[row['catid']]
#     result.append(row)
#
# df = pd.DataFrame(result)
#
#
# catlevel1 = list(df[df['parent_id'] == 0]['catid'].values)
# df.loc[(df['catid'].isin(catlevel1)), 'cat_level'] = str(1)
#
# catlevel2 = list(df[df['parent_id'].isin(catlevel1)]['catid'].values)
# df.loc[(df['catid'].isin(catlevel2)), 'cat_level'] = str(2)
#
# catlevel3 = list(df[df['parent_id'].isin(catlevel2)]['catid'].values)
# df.loc[(df['catid'].isin(catlevel3)), 'cat_level'] = str(3)
#
# catlevel4 = list(df[df['parent_id'].isin(catlevel3)]['catid'].values)
# df.loc[(df['catid'].isin(catlevel4)), 'cat_level'] = str(4)
#
# df.to_csv('F:\Download\gearbest_category_with_layers.csv',index=False)


df = pd.read_csv('F:\Download\gb_category_with_layers.csv')
# df = df[((df['cat_level'] == 1) | (df['cat_level'] == 2))]
df = df.sort_values(by='parent_id',ascending=True)
cat_map = {}
# catid	catname	parent_id
root = Node("Root")
cat_map[0] = root
for index, row in df.iterrows():
    cur = Node(row['catname'] + "-"+str(row['catid']))
    cat_map[row['catid']] = cur

for index, row in df.iterrows():
    cur = cat_map[row['catid']]
    cur.parent = cat_map[row['parent_id']]


for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
from anytree.exporter import DotExporter

DotExporter(root).to_picture("category.png")




