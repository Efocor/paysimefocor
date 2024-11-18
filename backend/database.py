import asyncpg
import asyncio
from typing import Optional

DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Cambia estos valores

async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn

async def close_connection(conn):
    await conn.close()
