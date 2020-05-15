# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 22:23
# 文件名称：aiohttp_spider.py
# 开发工具：PyCharm

# aiohttp实现高并发爬虫
# asyncio+aiohttp(实现异步请求)爬虫
# 去重（在爬取的过程中有些url已经爬取了，就不需要再爬取），
# 入库（使用异步的方式，pymysql已经不适用了，aiomysql）

import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery


start_url = "https://cuiqingcai.com/"
waitting_urls = []
seen_urls = set()
stopping = False

sem = asyncio.Semaphore(3)  # 使用信号量来控制并发量

async def fetch(url, session):
    # 获取html的内容
    # async with aiohttp.ClientSession() as session:  # 这里是每抓取一个url就创建一个session
    async with sem:
        # await asyncio.sleep(1)
        try:
            async with session.get(url) as resp:  # get方法
                print("url status: {}".format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()  # html内容
                    return data
        except Exception as e:
            print(e)

# 解析url-->由cpu来完成，不是io操作
# 从html中获取url
# PyQuery解析出所有的url，解析是通过cpu完成的，不会耗费io的
def extract_urls(html):
    # urls = []
    doc = PyQuery(html)
    for link in doc.items("a"):  # 获取a标签
        url = link.attr("href")  # a标签中的href属性
        if url and url.startswith("https") and url not in seen_urls:
            # urls.append(url)   # 如果详情页还有url(初始页时有)，可以将url加入到urls中，然后迭代爬取
            waitting_urls.append(url)  # 待爬取的url加到waitting队列中
    # return urls


# 获取请求的start_url中的所有url，网络请求比较费io
async def init_urls(url, session):
    html = await fetch(url, session)  # 获取初始url的html内容
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    # 获取文章详情并解析入库
    html = await fetch(url, session)  # 获取html的内容
    seen_urls.add(url)  # 加入到集合中

    # extract_urls提取出页面中所有的url，解析是通过cpu完成的，不会耗费io的
    extract_urls(html)  # 获取该详情页中的url

    doc = PyQuery(html)
    title = doc("title").text()

    async with pool.acquire() as conn:  # pool.acquire()获取连接
        async with conn.cursor() as cur:
            # await cur.execute("SELECT 42;")

            insert_sql = "insert into article_test(title) values('{}')".format(title)
            await cur.execute(insert_sql)

    # pool.close()
    # await pool.wait_closed()


# 从waitting_urls中取出url，并过滤和爬取
async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:  # 如果waitting_urls用的是队列Queue，则不需要，因为队列是阻塞的
                await asyncio.sleep(0.5)
                continue  # 退出此次循环

            url = waitting_urls.pop()
            print("start get url: {}".format(url))
            if re.match("https://cuiqingcai.com/\d+.html", url):  # 详情页url模式 --> 提取文章内容
                if url not in seen_urls:  # 还没抓取过
                    asyncio.ensure_future(article_handler(url, session, pool))  # 注册爬取事件
                    await asyncio.sleep(1)
            # else:                                            # 非详情页url--> 提取详情页url
            #     if url not in seen_urls:
            #         asyncio.ensure_future(init_urls(url, session))


async def main(loop):
    # 等待mysql链接建立好
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='root',
                                      db='my_aiomysql', loop=loop,
                                      charset="utf8", autocommit=True)

    # 两种创建Task实例的方式，asyncio.ensure_future和loop.create_task(python3.7以后的版本支持asyncio.create_task)。
    # 方式一：asyncio.ensure_future --> 调用了task = loop.create_task(coro_or_future)
    # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))

    async with aiohttp.ClientSession() as session:  # main执行完后，session会close掉
        html = await fetch(start_url, session)  # 初始化url爬取,获取初始url的html内容
        seen_urls.add(start_url)
        extract_urls(html)                      # 解析url内容，获取子链接

    asyncio.ensure_future(consumer(pool))  # # 将consumer注册到事件循环中


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()

