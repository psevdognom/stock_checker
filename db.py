from tortoise import Tortoise

async def init_db(test=False):
    await Tortoise.init(
        db_url=f'postgres://super_admin:SomeSecretPassword@localhost:5432/{"test_" if test else ""}postgres',
        modules={'models': ['models']}
    )