from tortoise import Tortoise, run_async

async def init():
    await Tortoise.init(
        db_url='postgres://super_admin:SomeSecretPassword@localhost:5432/postgres',
        modules={'models': ['models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

# run_async is a helper function to run simple async Tortoise scripts.
run_async(init())