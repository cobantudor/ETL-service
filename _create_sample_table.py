import psycopg2

from app.config import Config


def create_sample_user_orders_table():
    connection = None
    try:
        connection = psycopg2.connect(
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
            host=Config.POSTGRES_HOST,
            port=Config.POSTGRES_PORT,
            database=Config.POSTGRES_DATABASE
        )

        cursor = connection.cursor()
        sql_command = """
            create table user_orders
            (
                id                  serial not null,
                created_at          timestamp,
                date_tz             timestamp,
                item_count          integer,
                order_id            varchar,
                receive_method      varchar,
                status              varchar,
                store_id            varchar,
                subtotal            float,
                tax_percentage      float,
                total               float,
                total_discount      float,
                total_gratuity      float,
                total_tax           float,
                updated_at          timestamp,
                user_id             bigint,
                fulfillment_date_tz timestamp,
                user_first_name     varchar,
                user_last_name      varchar,
                user_merchant_id    varchar,
                user_phone_number   bigint,
                user_created_at     timestamp,
                user_updated_at     timestamp,
                primary key (id)
            )
            """

        cursor.execute(sql_command)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_sample_user_orders_table()
