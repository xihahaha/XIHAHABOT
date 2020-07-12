import requests
import json
import random
from nonebot import on_command, CommandSession


@on_command('laji', aliases=('我是什么垃圾'), only_to_me=False)
async def laji(session: CommandSession):
    laji_info = await laji_fenlei()
    await session.send(laji_info)


async def laji_fenlei():
    r = random.randint(0, 19)
    l = ({'name': '干垃圾（我乱说的'}, {'name': '湿垃圾（我乱说的'}, {'name': '可回收物（我乱说的'}, {'name': '有害垃圾（我乱说的'},
         {'name': '干垃圾（我乱说的'}, {'name': '湿垃圾（我乱说的'}, {'name': '可回收物（我乱说的'}, {'name': '有害垃圾（我乱说的'},
         {'name': '干垃圾（我乱说的'}, {'name': '湿垃圾（我乱说的'}, {'name': '可回收物（我乱说的'}, {'name': '有害垃圾（我乱说的'},
         {'name': '干垃圾（我乱说的'}, {'name': '湿垃圾（我乱说的'}, {'name': '可回收物（我乱说的'}, {'name': '有害垃圾（我乱说的'},
         {'name': '女装大佬'}, {'name': 'KIG大佬'}, {'name': 'FURRY大佬'}, {'name': '胶衣大佬'},)
    s4 = '你是' + l[r]['name']
    return s4
