import psycopg2
from psycopg2 import errors, sql
from configparser import ConfigParser
from Exceptions import DatabaseException
import os
from typing import Union


class ResultSetDict(dict):
    def __getitem__(self, item):
        if type(item) is not str:
            return None
        return super().__getitem__(item.lower())


class ResultSet:
    # constructor
    def __init__(self, description=None, results=None):
        self.rows = []
        self.cols_header = []
        self.cols = ResultSetDict()
        self.__fromQuery(description, results)

    def __getitem__(self, row):
        return self.__getRow(row)

    # so you can use print(ResultSet)
    def __str__(self):
        string = ""
        for col in self.cols_header:
            string += str(col) + "   "
        string += '\n'
        for row in self.rows:
            for val in row:
                string += str(val) + "   "
            string += '\n'
        return string

    # what is the size of the ResultSet?
    def size(self):
        return len(self.rows)

    # is the ResultSet empty?
    def isEmpty(self):
        return self.size() == 0

    def __getRow(self, row: int):
        if len(self.rows) <= row:
            print('Invalid row ' + str(row))
            return ResultSetDict()
        row_to_return = ResultSetDict()
        for val, col in zip(self.rows[row], self.cols_header):
            row_to_return[col] = val
        return row_to_return

    def __fromQuery(self, description, results: list):
        if results is None or len(results) == 0:  # no results
            self.cols = ResultSetDict()
        else:
            self.rows = results.copy()
            self.cols_header = [d.name for d in description]
            self.cols = ResultSetDict()
            for col, index in zip(self.cols_header, range(len(results[0]))):
                self.cols[col] = index


class DBConnector:
    # constructor
    def __init__(self):
        try:
            # Obtain the configuration parameters
            params = DBConnector.__config()
            self.connection = psycopg2.connect(**params)
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
        except Exception as e:
            self.connection = None
            self.cursor = None
            raise DatabaseException.ConnectionInvalid("Could not connect to database")

    # close connection
    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()

    # commit connection's changes
    def commit(self):
        if self.connection is not None:
            try:
                self.connection.commit()
            except Exception:
                raise DatabaseException.ConnectionInvalid("Could not commit changes")

    # rollback connection's changes
    def rollback(self):
        if self.connection is not None:
            try:
                self.connection.rollback()
            except Exception:
                raise DatabaseException.ConnectionInvalid("Could not rollback changes")

    # executes the query, if it is SELECT you may ask to print the results with printSchema
    # returns the number of rows effected and a ResultSet (for SELECT)
    def execute(self, query: Union[str, sql.Composed], printSchema=False) -> (int, ResultSet):
        if self.connection is None:
            raise DatabaseException.ConnectionInvalid("Connection Invalid")

        # try execute the query
        try:
            self.cursor.execute(query)
            row_effected = max(self.cursor.rowcount, 0)
            self.commit()
        except errors.lookup("23502"):
            raise DatabaseException.NOT_NULL_VIOLATION("NOT_NULL_VIOLATION")
        except errors.lookup("23503"):
            raise DatabaseException.FOREIGN_KEY_VIOLATION("FOREIGN_KEY_VIOLATION")
        except errors.lookup("23505"):
            raise DatabaseException.UNIQUE_VIOLATION("UNIQUE_VIOLATION")
        except errors.lookup("23514"):
            raise DatabaseException.CHECK_VIOLATION("CHECK_VIOLATION")

        # get entries in case of SELECT
        if self.cursor.description is not None:
            entries = ResultSet(self.cursor.description, self.cursor.fetchall())
        else:
            entries = ResultSet()

        # print SELECT entries
        if printSchema:
            print(entries)

        return row_effected, entries

    # grant credentials
    @staticmethod
    def __config(filename=os.path.join(os.path.join(os.getcwd(), ""), 'database.ini'),
                 section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            # file not found
            db = DBConnector.__config(
                filename=os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'Utility'), 'database.ini'))
            if db is None:
                raise DatabaseException.database_ini_ERROR("Please modify database.ini file under Utility")
        return db
