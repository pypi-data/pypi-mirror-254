from pathlib import Path
from typing import Final

import typer
from beni import bcolor, bpath, btask
from beni.bfunc import syncCall
from beni.bqiniu import QiniuBucket

from bcmd.common import password

app: Final = btask.newSubApp('temp 工具')


@app.command()
@syncCall
async def upload_qiniu(
    local_path: Path = typer.Argument(..., help="本地路径"),
    bucket_name: str = typer.Argument(None,  help="七牛云空间名称"),
):
    ak, sk = await password.getQiniu()
    bucket = QiniuBucket(
        'pytask-doc',
        '',
        ak,
        sk,
    )
    for file in bpath.listFile(local_path, True):
        key = file.relative_to(local_path).as_posix()
        await bucket.uploadFile(key, file)
        print(key)
    bcolor.printGreen('OK')