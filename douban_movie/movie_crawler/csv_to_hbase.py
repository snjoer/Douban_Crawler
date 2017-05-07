import sys
import csv
import happybase

__author__ = 'Pw-Chen'

def show(csvfile):
  with open(csvfile, 'rb') as csv_fd:
    count = 0
    iters = csv.reader(csv_fd)
    for row in iters:
      print ' || '.join(row)
      count = count + 1 
      print '=' * 20
      if count == 10:
        sys.exit()

def connectToHBase():
  conn = happybase.Connection(host = host,\
          table_prefix = namespace,\
          table_prefix_separator = ":")
  conn.open()
  table = conn.table(table_name)
  batch = table.batch(batch_size = batch_size)
  return conn, batch

def insert_row(batch, item):
  batch.put(item[2],\ 
        {"Review:MovieName":item[0],\
        "Review:MovieLink":item[1],\
        "Review:ReviewAuthor":item[3],\
        "Review:AuthorLink":item[4],\
        "Review:Content":item[5],\
        "Review:UpNumber":item[6],\
        "Review:DownNumber":item[7],\
        "Review:Rate"item[8]})      

def csv_iter(csvfile):
  with open(csvfile, 'rb') as csv_fd:
    iters = csv.reader(csv_fd)
    for row in iters:
      yield row


def csv_to_hbase(csvfile):
  conn, batch = connectToHBase()
  iters = csv_iter(csvfile)
  for i in iters:
    insert_row(batch, i)


if __name__ == '__main__':
    show(sys.argv[1])
    