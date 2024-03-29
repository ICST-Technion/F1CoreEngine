from abc import ABC, abstractmethod


class DBAdapter(ABC):
    @abstractmethod
    def insert_new_experiment(self, params):
        pass

    @abstractmethod
    def finish_experiment(self, params):
        pass

    @abstractmethod
    def insert_into_car_state(self, params):
        pass

    @abstractmethod
    def insert_into_drive_instructions(self, params):
        pass


"""
class DBAdapter:
    def __init__(self, connection_string):
        # connection = "postgres://username:password@host:port/dbname"
        # self.connection_string = "postgres://postgres:password@localhost:5432/formulaDB"
        # connection = "dbname =formulaDB user=postgres password=password host=localhost.com port=5432 sslmode=require"
        self.connection_string = connection_string
        self.conn = psycopg2.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def insert_into_car_state(self, params):
        # TODO: implement in the child class
"""
