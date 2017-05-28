import json
import redis
import happybase

def connectRedis():
    conn = redis.StrictRedis(host='localhost', port=6379)
    return conn

def connectToHBase():
    conn = happybase.Connection(host = host,\
            table_prefix = namespace,\
            table_prefix_separator = ":")
    conn.open()
    table = conn.table(table_name)
    batch = table.batch(batch_size = batch_size)
    return conn, batch

def insert_row(batch, item):
    batch.put(item['ReviewTitle'],\ 
            {"Review:MovieName":item['MovieName'],\
            "Review:MovieLink":item['MovieLink'],\
            "Review:ReviewAuthor":item['ReviewAuthor'],\
            "Review:AuthorLink":item['AuthorLink'],\
            "Review:Content":item['Content'],\
            "Review:UpNumber":item['UpNumber'],\
            "Review:DownNumber":item['DownNumber'],\
            "Review:Rate"item['Rate']})

def main():
    redis_conn = connectRedis()
    conn, batch = connectToHBase()
    while True:
        try:
            source, data = redis_conn.blpop(['review:items'])
            item = json.loads(data)
            insert_row(batch, item)
        finally:
            conn.close()
