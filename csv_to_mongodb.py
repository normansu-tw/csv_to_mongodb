#!/usr/bin/env python3
import sys, os
import pandas as pd
import pymongo
import json

def import_content(url, db, collection, filepath, delimiter):
    mng_client = pymongo.MongoClient(url)
    mng_db = mng_client[db] 
    db_cm = mng_db[collection]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    if delimiter == "comma":
        data = pd.read_csv(file_res)
    elif delimiter == "tab":
        data = pd.read_csv(file_res, sep='\t')
    elif delimiter == "space":
        data = pd.read_csv(file_res, sep='\s+')
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, help='mongoDB host')
    parser.add_argument('--port', type=int, help='mongoDB port')
    parser.add_argument('--user', type=str, help='mongoDB user')
    parser.add_argument('--pwd', type=str, help='mongoDB pwd')
    parser.add_argument('--delimiter', type=str, help='set delimiter(comma/space/tab), default comma')
    parser.add_argument('db', type=str, help='mongoDB database name')
    parser.add_argument('collection', type=str, help='mongoDB collection name')
    parser.add_argument('csv', type=str, help='csv file')
    args = parser.parse_args()

    host = 'localhost'
    if args.host:
        host = args.host
    port = 27017
    if args.port:
        port = args.port
    db = args.db
    if args.user:
        if args.pwd:
            url = "mongodb://%s:%s@%s:%d/%s" % (args.user, args.pwd, host, port, db)
        else:
            print("--user and --pwd must be assigned simultaneously!\n")
            args.print_help()
            sys.exit(1)
    else:
        if args.pwd:
            print("--user and --pwd must be assigned simultaneously!\n")
            args.print_help()
            sys.exit(1)
        else:
            url = "mongodb://%s:%d/%s" % (host, port, db)
    collection = args.collection
    csv = args.csv
    delimiter = 'comma'
    if args.delimiter:
      if args.delimiter in ['comma','tab','space']:
        delimiter = args.delimiter
      else:
        print("Bad delimiter!\n")
        args.print_help()
        sys.exit(1)
    import_content(url, db, collection, csv, delimiter)
