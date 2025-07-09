import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

connection_pool = None  # Initialize the connection pool

try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1, 20,
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        host=os.getenv('DATABASE_HOST'),
        port=os.getenv('DATABASE_PORT'),
        database=os.getenv('DATABASE_NAME')
    )
    if connection_pool:
        print("Connection pool created successfully")
except Exception as e:
    print(f"Error creating connection pool: {e}")
