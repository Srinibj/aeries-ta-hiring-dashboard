
import os
import psycopg
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, "config", ".env")

load_dotenv(ENV_PATH)


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


if __name__ == "__main__":
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT current_database(), version();"
                )
                result = cursor.fetchone()

                print("PostgreSQL connection successful!")
                print("Database:", result[0])
                print("Version:", result[1])

    except Exception as error:
        print("Database connection failed:")
        print(error)
