import psycopg2 as ps
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DatabasePy(object):
    def __init__(self, name="testing"):
        self.db_name = name
        self.user = 'postgres'
        self.password = 'baka'
        self.host = '127.0.0.1'
        # connect db postgres and check our db
        self.connection = self.connect_db("postgres")
        with self.connection.cursor() as cur:
            cur.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = %s", (self.db_name,))
            if not cur.fetchone():
                self.create_db(self.db_name)
        self.connection.close()
        # -------------------------------------------
        self.connection = self.connect_db(self.db_name)
        with self.connection.cursor() as cur:
            with open("commands.sql", "r") as commands_sql:
                cur.execute(commands_sql.read(1002))
                self.create_tables()
                cur.execute(commands_sql.read())

    def connect_db(self, name):
        return \
            ps.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=name
            )

    def user_change(self, name):
        self.user = name

    def is_db(self):
        with self.connection.cursor() as cur:
            cur.execute(open("create.sql", "r").read())
            cur.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = %s", (self.db_name,))
            return cur.fetchone()

    def create_db(self, name):
        self.db_name = name
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with self.connection.cursor() as cur:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(self.db_name))
            )

    def __del__(self):
        if self.connection:
            self.connection.close()
        del self

    def drop_db(self):
        if self.connection:
            self.connection.close()
        self.connection = self.connect_db("postgres")
        self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with self.connection.cursor() as cur:
            cur.execute(sql.SQL(f"DROP DATABASE {self.db_name}"))

        print("database was dropped")
        self.__del__()

    def create_clients(self):
        with self.connection.cursor() as cur:
            cur.callproc("create_tab_clients")
        self.connection.commit()

    def create_branches(self):
        with self.connection.cursor() as cur:
            cur.callproc("create_tab_branches")
        self.connection.commit()

    def create_tos(self):
        with self.connection.cursor() as cur:
            cur.callproc("create_tab_types_of_services")
        self.connection.commit()

    def create_services(self):
        with self.connection.cursor() as cur:
            cur.callproc("create_tab_services")
        self.connection.commit()

    def create_tables(self):
        self.create_clients()
        self.create_branches()
        self.create_tos()
        self.create_services()

    def get_clients(self):
        with self.connection.cursor() as cur:
            cur.callproc("get_clients")
            return cur.fetchall()

    def get_branches(self):
        with self.connection.cursor() as cur:
            cur.callproc("get_branches")
            return cur.fetchall()

    def get_tos(self):
        with self.connection.cursor() as cur:
            cur.callproc("get_tos")
            return cur.fetchall()

    def get_services(self):
        with self.connection.cursor() as cur:
            cur.callproc("get_services")
            return cur.fetchall()

    def add_to_clients(self, id, name, surname, telephone):
        with self.connection.cursor() as cur:
            cur.callproc("add_to_clients", (id, name, surname, telephone,))

    def add_to_branches(self, id, name, address, telephone):
        with self.connection.cursor() as cur:
            cur.callproc("add_to_branches", (id, name, address, telephone,))

    def add_to_tos(self, id, name, type_tos, price):
        with self.connection.cursor() as cur:
            cur.callproc("add_to_tos", (id, name, type_tos, price,))

    def add_to_services(self, br_id, tos_id, client_id, date):
        with self.connection.cursor() as cur:
            cur.callproc("add_to_services", (br_id, tos_id, client_id, date,))