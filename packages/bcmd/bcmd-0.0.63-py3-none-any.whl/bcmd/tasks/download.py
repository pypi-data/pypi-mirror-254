import asyncio
import os
from pathlib import Path
from typing import Final

import pyperclip
import typer
from beni import bcolor, bhttp, binput, bpath, btask
from beni.bfunc import syncCall

app: Final = btask.newSubApp('下载')


@app.command()
@syncCall
async def urls(
    path: Path = typer.Option(None, '--path', '-p', help='指定路径，默认当前目录'),
):
    '下载文件'
    path = path or Path(os.getcwd())
    content = pyperclip.paste()
    urlSet = set([x.strip() for x in content.strip().split('\n') if x.strip()])

    for i, url in enumerate(urlSet):
        print(f'{i + 1}. {url}')
    print(f'输出目录：{path}')
    await binput.confirm('是否确认？')

    async def download(url: str):
        file = bpath.get(path, '/'.join([x for x in url.replace('://', '/').split('/') if x]))
        try:
            bcolor.printGreen(url)
            await bhttp.download(url, file)
        except:
            bcolor.printRed(url)

    await asyncio.gather(*[download(x) for x in urlSet])

    bcolor.printYellow('Done')
