import getpass
import json
import uuid
from typing import Final

import jwt
import pyperclip
from beni import bcolor, btask
from beni.bfunc import magicSequence, syncCall
from rich.console import Console

app: Final = btask.newSubApp('密钥')


_KEY_SALT = '_salt_@#%@#xafDGAz.nq'
_KEY_TEXT = '_text_A!@$,FJ@#adsfkl'


@app.command()
@syncCall
async def encode_json():
    '生成JSON密文（使用剪贴板内容）'
    content = pyperclip.paste()
    try:
        data = json.loads(content)
    except:
        return btask.abort('错误：剪贴板内容必须是JSON格式', content)
    Console().print_json(data=data, indent=4, ensure_ascii=False, sort_keys=True)
    password = ''
    while not password:
        password = getpass.getpass('输入密码：')
    while password != getpass.getpass('再次密码：'):
        pass
    data[_KEY_SALT] = str(uuid.uuid4())
    result = jwt.encode(data, password, algorithm='HS256')
    result = magicSequence(result)
    pyperclip.copy(result)
    print('密文已复制到剪贴板')
    bcolor.printYellow(result)
    bcolor.printGreen('OK')
    # {"uuu": "xxx", "ppp": "xxx"}


@app.command()
@syncCall
async def decode_json():
    '还原JSON密文内容（使用剪贴板内容）'
    content = pyperclip.paste()
    bcolor.printYellow(content)
    content = magicSequence(content)
    password = ''
    while not password:
        password = getpass.getpass('输入密码：')
    try:
        data = jwt.decode(content, password, algorithms=['HS256'])
        if _KEY_SALT in data:
            del data[_KEY_SALT]
        Console().print_json(data=data, indent=4, ensure_ascii=False, sort_keys=True)
    except:
        return btask.abort('无法解析密文')


@app.command()
@syncCall
async def encode_text():
    '生成文本密文（使用剪贴板内容）'
    content = pyperclip.paste()
    bcolor.printYellow(content)
    data = {
        _KEY_TEXT: content,
        _KEY_SALT: str(uuid.uuid4()),
    }
    password = ''
    while not password:
        password = getpass.getpass('输入密码：')
    while password != getpass.getpass('再次密码：'):
        pass
    result = jwt.encode(data, password, algorithm='HS256')
    result = magicSequence(result)
    pyperclip.copy(result)
    print('密文已复制到剪贴板')
    bcolor.printYellow(result)
    bcolor.printGreen('OK')


@app.command()
@syncCall
async def decode_text():
    '还原文本密文内容（使用剪贴板内容）'
    content = pyperclip.paste()
    bcolor.printYellow(content)
    content = magicSequence(content)
    password = ''
    while not password:
        password = getpass.getpass('输入密码：')
    try:
        data = jwt.decode(content, password, algorithms=['HS256'])
        content = data[_KEY_TEXT]
        bcolor.printYellow(content)
    except:
        return btask.abort('无法解析密文')
