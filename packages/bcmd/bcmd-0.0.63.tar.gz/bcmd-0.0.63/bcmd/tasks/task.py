from pathlib import Path
from typing import Final

import pathspec
import typer
from beni import bcolor, bfile, binput, bpath, btask, btime, bzip
from beni.bfunc import syncCall, toAny, tryRun
from beni.bqiniu import QiniuBucket
from beni.btype import Null

from bcmd.common import password

from . import bin, venv

app: Final = btask.newSubApp('BTask 工具')


_PREFIX = 'template/'


@app.command()
@syncCall
async def template_gen(
    tempalte_name: str = typer.Argument(..., help="模板名称"),
    project_path: Path = typer.Argument(None, help="用于生成模板的文件夹路径"),
):
    '生成模板'
    with bpath.useTempPath() as tempPath:
        project_path = bpath.get(project_path)
        await _copyTemplateFiles(project_path, tempPath)
        bucket = await _getBucket()
        fileList, _ = await bucket.getFileList(f'{_PREFIX}{tempalte_name}/', 200)
        num = len(fileList)
        if num > 100:
            bcolor.printYellow(f'当前模板的版本数量已经超过 {num} 个，建议删除一些不常用的版本')
        elif num > 180:
            btask.abort(f'当前模板的版本数量已经超过 {num} 个，无法继续添加')
        with bpath.useTempFile() as tempFile:
            bzip.zipFolder(tempFile, tempPath)
            nowTime = await btime.networkTime()
            key = f'{_PREFIX}{tempalte_name}/{tempalte_name}_{nowTime.strftime("%Y%m%d_%H%M%S")}.zip'
            with tryRun():
                await bucket.deleteFiles(key)
            await bucket.uploadFile(key, tempFile)
        bcolor.printGreen('OK')


async def _copyTemplateFiles(src: Path, dst: Path):
    spec = pathspec.PathSpec.from_lines(
        toAny(pathspec.patterns).GitWildMatchPattern,
        (await bfile.readText(src / '.gitignore')).splitlines() + ['.git'],
    )
    files = bpath.listFile(src, True)
    files = [x for x in files if not spec.match_file(x.relative_to(src))]
    for file in sorted(files):
        toFile = bpath.changeRelative(file, src, dst)
        bpath.copy(file, toFile)


@app.command()
@syncCall
async def create(
    tempalte_name: str = typer.Argument(..., help="模板名称"),
    project_path: Path = typer.Argument(None, help="项目路径，不填标识在当前目录创建"),
):
    '创建项目'
    if not project_path:
        project_path = Path.cwd()
    project_path = bpath.get(project_path)
    if project_path.exists():
        await binput.confirm(f'项目路径 {project_path} 已存在，是否覆盖？')
    if Path(tempalte_name).is_absolute():
        btask.abort(f'模板名称不能为绝对路径：{tempalte_name}')
    bucket = await _getBucket()
    fileList, _ = await bucket.getFileList(f'{_PREFIX}{tempalte_name}/', 1000)
    if not fileList:
        btask.abort('模板不存在')
    fileList.sort(key=lambda x: x.key)
    with bpath.useTempPath(True) as tempPath:
        key = fileList[-1].key
        bcolor.printGreen(f'正在使用版本 {key}')
        await bucket.downloadPrivateFileUnzip(key, tempPath)
        for item in bpath.listPath(tempPath):
            toItem = project_path / item.name
            bpath.copy(item, toItem)
    init(project_path)


@app.command()
@syncCall
async def init(
    project_path: Path = typer.Argument(None, help="项目路径"),
):
    '初始化 BTask 项目，包括 venv 和 bin 操作'
    if not project_path:
        project_path = Path.cwd()
    fileList = bpath.listFile(project_path, True)
    for file in fileList:
        if file.name == 'venv.list':
            targetPath = file.parent
            venv.venv(
                packages=Null,
                path=targetPath,
                disabled_mirror=False,
                quiet=True,
            )
            binListFile = targetPath / 'bin.list'
            if binListFile.is_file():
                bin.download(
                    names=Null,
                    file=binListFile,
                    output=targetPath / 'bin',
                )


@app.command()
@syncCall
async def tidy(
    tasks_path: Path = typer.Argument(None, help="tasks 路径"),
):
    '整理 tasks 文件'
    initFile = tasks_path / '__init__.py'
    btask.check(initFile.is_file(), '文件不存在', initFile)
    files = bpath.listFile(tasks_path)
    files = [x for x in files if not x.name.startswith('_')]
    contents = [f'from . import {x.stem}' for x in files]
    contents.insert(0, '# type: ignore')
    contents.append('')
    content = '\n'.join(contents)
    await bfile.writeText(
        initFile,
        content,
    )
    print(content)


async def _getBucket():
    ak, sk = await password.getQiniu()
    return QiniuBucket(
        'pytask',
        'http://qiniu-cdn.pytask.com',
        ak,
        sk,
    )
