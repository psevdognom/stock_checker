from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='postgres://super_admin:SomeSecretPassword@localhost:5432/postgres',
        modules={'models': ['models']}
    )