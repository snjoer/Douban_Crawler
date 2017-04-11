
def extract_movie_data_from_item(item, family):
    return {'%s:PostUrl' % family: item['PostUrl'],
            '%s:Director' % family: item['Director'],
            '%s:ReleaseTime' % family: item['ReleaseTime'],
            '%s:Area' % family: item['Area'],
            '%s:Performers' % family: item['Performers']}


def send_movie_data_to_hbase(hbase, row, movie_data):
    hbase.batch_put(row, movie_data)


def process_movie_item(hbase, row, family, item):
    data = extract_movie_data_from_item(item, family)
    send_movie_data_to_hbase(hbase, row, data)
