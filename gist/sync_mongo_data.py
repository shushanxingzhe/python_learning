import pymongo
from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import time
import os

online_ip = '192.168.0.100'
online_port = 27017
offline_ip = '127.0.0.1'
offline_port = 27017

log_file = 'logs/sync_data'
dirname = os.path.dirname(log_file)
if not os.path.exists(dirname):
    os.makedirs(dirname, exist_ok=True)

formatter = logging.Formatter(fmt="[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s")
log_file_handler = TimedRotatingFileHandler(filename=log_file, when="midnight", interval=1, backupCount=30)
log_file_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_file_handler)

online_client = pymongo.MongoClient(online_ip, online_port)
online_db = online_client.get_database('search')
offline_client = pymongo.MongoClient(offline_ip, offline_port)
offline_db = offline_client.get_database('search')

all_online_collections = online_db.list_collection_names()
all_offline_collections = offline_db.list_collection_names()
today = datetime.today()

sync_collections = []

weekday = today.weekday()
weekday = 4
for colname in all_online_collections:
    # only friday sync category and goods
    if ('category_info_' in colname or 'goods_info_' in colname) and weekday == 4:
        sync_collections.append(colname)
    elif (colname not in all_offline_collections) and ('search_10002_' in colname or 'search_10013_' in colname \
                                                       or 'searchpv_10002_' in colname or 'searchpv_10013_' in colname):
        sync_collections.append(colname)
for colname in sync_collections:
    logger.info('start sync %s' % colname)
    start = time.time()
    data = online_db[colname].find(projection={'_id': False})
    if colname in all_offline_collections:
        offline_db.get_collection(colname).drop()
    offline_db.create_collection(colname).insert_many(data)
    end = time.time()
    logging.info('sync %s spent time: %.2f seconds' % (colname,end - start))
