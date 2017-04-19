
def extract_movie_data_from_item(item, family):
    return {'%s:PostUrl' % family: item['PostUrl'],
            '%s:Director' % family: item['Director'],
            '%s:ReleaseTime' % family: item['ReleaseTime'],
            '%s:Area' % family: item['Area'],
            '%s:Performers' % family: item['Performers']}


def send_data_to_hbase(hbase, row, movie_data):
    hbase.batch_put(row, movie_data)


def extrace_review_data_from_item(item, family):
    return {'%s:MovieLink' % family: item['MovieLink'],
            '%s:ReviewTitle' % family: item['ReviewTitle'],
            '%s:ReviewAuthor' % family: item['ReviewAuthor'],
            '%s:AuthorLink' % family: item['AuthorLink'],
            '%s:ReviewContent' % family: item['ReviewContent'],
            '%s:UpNumber' % family: item['UpNumber'],
            '%s:DownNumber' % family: item['DownNumber'],
            '%s:Rate' % family: item['Rate']}


def process_movie_item(hbase, row, family, item):
    data = extract_movie_data_from_item(item, family)
    send_data_to_hbase(hbase, row, data)


def process_review_item(hbase, row, family, item):
    data = extrace_review_data_from_item(item, family)
    send_data_to_hbase(hbase, row, data)
