import logging
import happybase
import process_item
from hbase_instance import HbaseInstance

logging.getLogger().addHandler(logging.StreamHandler())

hbase_cfg = {
    'host': '120.77.217.120',
    'batch_size': 100,
    'namespace': "wsh",
    # 'row_count': 0,
    'table_name': "movie",
    'family': 'Movie',
    'namespace_separator': ':'
}


def test_hbase_basic():

    hbase = HbaseInstance(hbase_cfg)
    hbase.open()
    hbase.close()


def test_hbase_put():
    hbase = HbaseInstance(hbase_cfg)
    hbase.open()
    hbase.specify_table(hbase_cfg['table_name'])
    hbase.batch_put('testmovie1', {'test1:d1': 'data1',
                                   'test2:d2': 'data22',
                                   'test3:d3': 'data33'})
    hbase.force_send()
    hbase.close()


def test_hbase_movie_item_put():
    hbase = HbaseInstance(hbase_cfg)
    hbase.open()
    hbase.specify_table(hbase_cfg['table_name'])
    item = {'PostUrl': 'post_url',
            'Director': 'director',
            'ReleaseTime': 'releaseTime',
            'Area': 'area',
            'Performers': 'performers',
            'MovieName': 'Overwatch'}

    process_item.process_movie_item(
        hbase, item['MovieName'], hbase_cfg['family'], item)

    hbase.force_send()
    hbase.close()
