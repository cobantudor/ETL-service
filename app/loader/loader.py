import psycopg2

from app.config import Config
from .user_orders_sql_operations import getInsert


class Loader:
    def __init__(self):
        pass

    def load(self, user_orders):
        connection = None
        sql_command = getInsert()

        try:
            connection = psycopg2.connect(
                user=Config.POSTGRES_USER,
                password=Config.POSTGRES_PASSWORD,
                host=Config.POSTGRES_HOST,
                port=Config.POSTGRES_PORT,
                database=Config.POSTGRES_DATABASE
            )
            cursor = connection.cursor()
            cursor.executemany(sql_command, user_orders)
            cursor.close()
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
