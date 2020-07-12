import requests
import random
from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment


@on_command('sh71', aliases='71路', only_to_me=False)
async def sh71(session: CommandSession):
    msg = await get_msg()
    pic = await get_pic()
    sound = await get_sound()
    await session.send(msg)
    await session.send(pic)
    await session.send(sound)


async def get_msg():
    message = "71路进站啦！"
    return message


async def get_pic():
    picture = MessageSegment.image("sh71/71.jpg")
    return picture


async def get_sound():
    i = str(random.randint(1, 47))
    record = MessageSegment.record("sh71/" + i + ".mp3")
    return record
