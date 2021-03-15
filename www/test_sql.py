import orm
import asyncio
from models import User, Blog, Comment
# ref https://aodabo.tech/blog/001546713871394a2814d2c180b4e6f8d30c62a3eaf218a000


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='yzw123', db='awesome')
    u = User(name='Test', email='test@qq.com', passwd='123456', image='about:blank')
    await u.save()
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()