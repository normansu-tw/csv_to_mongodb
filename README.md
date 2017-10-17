# csv_to_mongodb
The handy utility for importing CSV data to mongoDB, writen by Python with pandas, pymongo 

Prerequisite
==================

*    Python3
*    pip3
*    pandas
*    pymongo

Usages
==================

    usage: csv_to_mongodb.py [-h] [--host HOST] [--port PORT] [--user USER]
                             [--pwd PWD] [--delimiter DELIMITER]
                             db collection csv
    
    positional arguments:
      db                    mongoDB database name
      collection            mongoDB collection name
      csv                   csv file

    optional arguments:
      -h, --help            show this help message and exit
      --host HOST           mongoDB host
      --port PORT           mongoDB port
      --user USER           mongoDB user
      --pwd PWD             mongoDB pwd
      --delimiter DELIMITER set delimiter(comma/space/tab), default comma
