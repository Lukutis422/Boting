import aiosqlite

async def init_db():
    async with aiosqlite.connect("database.sqlite3") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS warnings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guild_id INTEGER,
            user_id INTEGER,
            reason TEXT
        )
        """)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS xp (
            guild_id INTEGER,
            user_id INTEGER,
            xp INTEGER DEFAULT 0,
            PRIMARY KEY (guild_id, user_id)
        )
        """)
        await db.commit()
