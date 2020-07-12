import requests
import random
from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment


@on_command('ana', aliases='ANA', only_to_me=False)
async def sh71(session: CommandSession):
    pic = await get_pic()
    sound = await get_sound()
    await session.send(pic)
    await session.send(sound)

async def get_pic():
    picture = MessageSegment.image("ana/ana.png")
    return picture

async def get_sound():
    record = MessageSegment.record("ana/ana.mp3")
    return  record