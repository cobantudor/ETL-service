import psycopg2

from app.config import Config


class Loader:
    def __init__(self):
        pass

    def load(self, user_orders):
        connection = None
        sql_command = """
            INSERT INTO user_orders(id, created_at, date_tz, item_count, order_id,
                    receive_method, status, store_id, subtotal, tax_percentage, total,
                    total_discount, total_gratuity, total_tax, updated_at, user_id,
                    fulfillment_date_tz, user_first_name, user_last_name, user_merchant_id,
                    user_phone_number, user_created_at, user_updated_at)
            values (%(id)s, %(created_at)s, %(date_tz)s, %(item_count)s, %(order_id)s,
                       %(receive_method)s, %(status)s, %(store_id)s, %(subtotal)s, %(tax_percentage)s, %(total)s,
                       %(total_discount)s, %(total_gratuity)s, %(total_tax)s, %(updated_at)s, %(user_id)s,
                       %(fulfillment_date_tz)s, %(user_first_name)s, %(user_last_name)s, %(user_merchant_id)s,
                       %(user_phone_number)s, %(user_created_at)s, %(user_updated_at)s)
        """

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
