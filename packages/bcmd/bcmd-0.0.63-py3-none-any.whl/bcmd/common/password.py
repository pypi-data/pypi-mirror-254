import getpass
from typing import Any

from beni import bcache, bjwt


@bcache.cache
async def getPypi() -> tuple[str, str]:
    content = 'pypi.org eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Il9fdG9rZW5fXyIsInBhc3N3b3JkIjoicHlwaS1BZ0VJY0hsd2FTNXZjbWNDSkRrM05qWTFOMk5tTFRsaU9URXROR0ZsT1MwNVlUQTBMVFE0WVQ2NlTzlIbkx4RG9Ca3ciLCIzMGE0YTM1Ni0zNmYwLTQ4NTktODk3Zi0xZDFmZDRkMmVhMWQiOjE3MDA4NDU1ODQuNDg5MTY2fQ.YjsYWtUxfsDbHJRQiFSzfuNKDnccC3gxGbAk_bW-LBARCak5EUmlOR1ppWVFBQ0tsc3pMQ0ppT0RBMU16QmhaUzFrTURZekxUUTBZbVF0T0dJMU1pMHdNMlZqWVRSaFlUYzJZV1lpWFFBQUJpQWNvaWxLNlA2TVNZSklETnlvXzcwTXkybzVPWWR3'
    data = _getData(content)
    return data['username'], data['password']


@bcache.cache
async def getQiniu() -> tuple[str, str]:
    content = '七牛云 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhayI6Ik8td1lkdzA1Q05fLThoLUFKYmZDWTRqN2VoRkJTcEdiQTlyNlhOUk4iLCJzayI6InQxZWI5ZDI4YzNhZWMiOjE2OTY5MjI0MjAuNTgzMzkzNn0.4pn5edULuUmgo_pTpcoPE1Cxwxq5W81CjSeTCmnaEyEyNjAtck5ZUlJNZ29tSUcwZ0Rtakp2T2o1VmNjdTFWMzJHZHFFY2UiLCIyMzE4NmNlMy01MTI0LTRjMWItYjIzZC0'
    data = _getData(content)
    return data['ak'], data['sk']


def _getData(content: str) -> dict[str, Any]:
    index = content.find(' ')
    if index > -1:
        tips = f'请输入密码（{content[:index]}）：'
    else:
        tips = '请输入密码：'
    while True:
        try:
            pwd = getpass.getpass(tips)
            return bjwt.decodeJson(content, pwd)
        except KeyboardInterrupt:
            raise Exception('操作取消')
        except BaseException:
            pass
