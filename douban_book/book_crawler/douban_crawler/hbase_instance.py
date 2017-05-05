import happybase
import logging


class HbaseInstance(object):

    def __init__(self, setting):
        self.backlog_count_ = 0
        self.backlog_upper_bound_ = 20
        self.table_ = None
        self.batch_ = None

        self.batch_size_ = int(setting.get('batch_size'))

        self.connection_ = happybase.Connection(
            host=setting['host'],
            table_prefix=setting['namespace'],
            table_prefix_separator=setting['namespace_separator'],
            autoconnect=False)

    def open(self):
        self.connection_.open()

    def close(self):
        if self.batch_ is not None:
            self.batch_.send()

        self.connection_.close()

    def specify_table(self, table_name):
        self.table_ = self.connection_.table(table_name)

        if self.batch_ is not None:
            self._send()

        self.batch_ = self.table_.batch(batch_size=self.batch_size_)

    def _send(self):
        logging.debug('send op to table %s' % self.table_.name)
        self.batch_.send()
        self.backlog_count_ = 0

    def force_send(self):
        self._send()

    def batch_put(self, row, data):
        # TODO  Does happybase convert str to byte automaticly?
        # fix this function if not

        if self.batch_ is None or self.table_ is None:
            raise ValueError('please specify table')

        logging.debug('put data to table:%s in row %s' %
                      (self.table_.name, row))

        self.batch_.put(row, data)

        self.backlog_count_ = self.backlog_count_ + 1
        if self.batch_size_ is not None and self.backlog_count_ >= self.backlog_upper_bound_:
            self._send()
