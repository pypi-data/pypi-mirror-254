import getpass

import jwt
from beni import bcache
from beni.bfunc import magicSequence, tryRun


@bcache.cache
async def getPypi() -> tuple[str, str]:
    while True:
        with tryRun():
            data = _getData(
                '输入密码（pypi）',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Il9fdG9rZW5fXyIsInBhc3N3b3JkIjoicHlwaS1BZ0VJY0hsd2FTNXZjbWNDSkRrM05qWTFOMk5tTFRsaU9URXROR0ZsT1MwNVlUQTBMVFE0WVQ2NlTzlIbkx4RG9Ca3ciLCIzMGE0YTM1Ni0zNmYwLTQ4NTktODk3Zi0xZDFmZDRkMmVhMWQiOjE3MDA4NDU1ODQuNDg5MTY2fQ.YjsYWtUxfsDbHJRQiFSzfuNKDnccC3gxGbAk_bW-LBARCak5EUmlOR1ppWVFBQ0tsc3pMQ0ppT0RBMU16QmhaUzFrTURZekxUUTBZbVF0T0dJMU1pMHdNMlZqWVRSaFlUYzJZV1lpWFFBQUJpQWNvaWxLNlA2TVNZSklETnlvXzcwTXkybzVPWWR3'
            )
            return data['username'], data['password']


@bcache.cache
async def getQiniu() -> tuple[str, str]:
    while True:
        with tryRun():
            data = _getData(
                '输入密码（七牛云）',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhayI6Ik8td1lkdzA1Q05fLThoLUFKYmZDWTRqN2VoRkJTcEdiQTlyNlhOUk4iLCJzayI6InQxZWI5ZDI4YzNhZWMiOjE2OTY5MjI0MjAuNTgzMzkzNn0.4pn5edULuUmgo_pTpcoPE1Cxwxq5W81CjSeTCmnaEyEyNjAtck5ZUlJNZ29tSUcwZ0Rtakp2T2o1VmNjdTFWMzJHZHFFY2UiLCIyMzE4NmNlMy01MTI0LTRjMWItYjIzZC0'
            )
            return data['ak'], data['sk']


def _getData(tips: str, content: str):
    content = magicSequence(content)
    while True:
        with tryRun():
            pwd = getpass.getpass(f'{tips}：')
            return jwt.decode(content, pwd, algorithms=['HS256'])
