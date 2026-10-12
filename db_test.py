import asyncio
import os
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host=os.environ["db_host"],
        port=int(os.environ["db_port"]),
        user=os.environ["db_user"],
        password=os.environ["db_pwd"],
        database=os.environ["db_name"],
        timeout=5,
    )
    print("PostgreSQL login successful")
    await conn.close()

asyncio.run(main())
