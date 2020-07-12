import requests
import random
from nonebot import on_command, CommandSession
from aiocqhttp import MessageSegment


@on_command('melody', aliases='发车', only_to_me=False)
async def sh71(session: CommandSession):
    msg1 = await get_msg_1()
    sound = await get_sound()
    msg2 = await get_msg_2()
    await session.send(msg1)
    await session.send(sound)
    await session.send(msg2)


async def get_msg_1():
    message = "加开列车！"
    return message


async def get_sound():
    i = str(random.randint(1, 130))
    record = MessageSegment.record("melody/" + i + ".mp3")
    return record


async def get_msg_2():
    message = "ドアが閉まります、ご注意ください！"
    return message
