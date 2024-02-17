Quickly start with `aiophoenixdb`
^^^^^^^^
What is `aiophoenixdb`
---------
How to install
---------

::

   pip install aiophoenixdb

How to use
---------

- Query sample

::

    import aiophoenixdb
    import asyncio

    PHOENIX_CONFIG = {
        'url': 'http://xxxxxxxxxx',
        'user': 'xxx',
        'password': 'xxx',
        'database': 'xxx'
    }

    async def query_test():
        conn = await aiophoenixdb.connect(**PHOENIX_CONFIG)
        async with conn:
            async with conn.cursor() as ps:
                # need await
                await ps.execute("SELECT * FROM xxx WHERE id = ?",  parameters=("1", ))
                res = await ps.fetchone()
                print(res)

    # 将查询的携程丢到事件循环中运行
    asyncio.get_event_loop().run_until_complete(query_test())

- Query with DictCursor

::

    import aiophoenixdb
    import asyncio
    from aiophoenixdb.cursors import DictCursor

    PHOENIX_CONFIG = {
        'url': 'http://xxxxxxxxxx',
        'user': 'xxx',
        'password': 'xxx',
        'database': 'xxx'
    }

    async def query_test():
        conn = await aiophoenixdb.connect(**PHOENIX_CONFIG)
        async with conn:
            async with conn.cursor(cursor_factory=DictCursor) as ps:
                # need await
                await ps.execute("SELECT * FROM xxx WHERE id = ?",  parameters=("1", ))
                res = await ps.fetchone()
                print(res)

    # 将查询的携程丢到事件循环中运行
    asyncio.get_event_loop().run_until_complete(query_test())