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
    batch.put(item['MovieName'],\ 
            {"Movie:PostUrl":item['PostUrl'],\
            "Movie:Director":item['Director'],\
            "Movie:ReleaseTime":item['ReleaseTime'],\
            "Movie:Area":item['Area'],\
            "Movie:Performers"item['Performers']})

def main():
    redis_conn = connectRedis()
    conn, batch = connectToHBase()
    while True:
        try:
            source, data = redis_conn.blpop(['movieContent:items'])
            item = json.loads(data)
            insert_row(batch, item)
        finally:
            conn.close()
