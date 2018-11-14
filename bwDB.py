import sqlite3

__version__ = '1.2.0'

class bwDB:
    def __init__(self, **kwargs):
        '''
        db = bwDB( [ table = ''] [, filename = ''] )
        constructor method
            table is for CRUD methods
            filename is for connecting to the database file
        '''
        self._filename = kwargs.get('filename')
        self._table = kwargs.get('table', '')

    def set_table(self, tablename):
        self._table = tablename
        
