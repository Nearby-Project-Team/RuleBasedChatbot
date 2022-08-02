from exceptions.storage_exception import StoreException
from connection import getMySQLConnection

class StorageRepositoryEntity():
    def __init__(self, host, port, username, password, db):
        try:
            self.conn = getMySQLConnection(
                host=host,
                port=port,
                username=username,
                password=password,
                db=db
            )
        except Exception as e:
            raise StoreException(*e.args, **e.kwargs)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        # can test for type and handle different situations
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise StoreException(*e.args)