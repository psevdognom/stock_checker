import asynctest
from tortoise.transactions import in_transaction, atomic

from .db import init_db
from models import Stock
from main import update_stock


class StockTestCase(asynctest.TestCase):

    async def setUp(self):
        await init_db()
        async with in_transaction() as connection:
            test_stock = Stock(title='test', url='url', in_stock='lllll')
            await test_stock.save(using_db=connection)

    @atomic
    async def test_tovar_pomenyalos_nalychie(self):
        await update_stock([{'title': 'test', 'url': 'lolo', 'in_stock': ''}])
        test_stock = await Stock.filter(title='test').first()
        assert test_stock.in_stock == True

    async def test_tovar_propal(self):
        await update_stock([{'title': 'test2', 'url': 'lolo', 'in_stock': ''}])
        test_stock = await Stock.filter(title='test2').first()
        assert test_stock == Stock(title='test2')
        await update_stock([])
        test_stock = await Stock.all()
        assert len(test_stock) == False

    async def tearDown(self):
        await Stock.filter(title='test').delete()