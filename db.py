from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='postgres://super_admin:admin@localhost:5432/tammytanuka',
        modules={'models': ['models']}
    )