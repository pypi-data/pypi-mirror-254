import getpass
import json
from typing import Final

import pyperclip
from beni import bcolor, bjwt, btask
from beni.bfunc import syncCall
from rich.console import Console

app: Final = btask.newSubApp('JWT密文')


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
    secret, tips = _genSecret()
    result = bjwt.encodeJson(data, secret, tips)
    pyperclip.copy(result)
    print('密文已复制到剪贴板')
    bcolor.printYellow(result)


@app.command()
@syncCall
async def encode_text():
    '生成文本密文（使用剪贴板内容）'
    content = pyperclip.paste()
    assert content, '剪贴板内容不能为空'
    bcolor.printGreen(content)
    secret, tips = _genSecret()
    result = bjwt.encodeText(content, secret, tips)
    pyperclip.copy(result)
    print('密文已复制到剪贴板')
    bcolor.printYellow(result)


@app.command()
@syncCall
async def decode_json():
    '还原JSON密文内容（使用剪贴板内容）'
    content = pyperclip.paste().strip()
    bcolor.printYellow(content)
    while True:
        try:
            password = getpass.getpass('输入密码：')
            data = bjwt.decodeJson(content, password)
            Console().print_json(data=data, indent=4, ensure_ascii=False, sort_keys=True)
            return
        except KeyboardInterrupt:
            break
        except BaseException:
            pass


@app.command()
@syncCall
async def decode_text():
    '还原文本密文内容（使用剪贴板内容）'
    content = pyperclip.paste().strip()
    bcolor.printYellow(content)
    while True:
        try:
            password = getpass.getpass('输入密码：')
            data = bjwt.decodeText(content, password)
            bcolor.printGreen(data)
            return
        except KeyboardInterrupt:
            break
        except BaseException:
            pass


def _genSecret():
    secret = ''
    while not secret:
        secret = getpass.getpass('输入密码：')
    while secret != getpass.getpass('再次密码：'):
        pass
    tips = input('密码提示（可选）：')
    return secret, tips
