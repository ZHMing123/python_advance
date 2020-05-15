# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 22:45
# 文件名称：aiomysql_operation.py
# 开发工具：PyCharm

# aiomysql使用

import aiomysql
import asyncio


async def test_example(loop):
    # 等待mysql链接建立好
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop,
                                      charset="utf8", autocommit=True)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 42
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))