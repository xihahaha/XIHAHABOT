from datetime import datetime
from aiocqhttp import MessageSegment
import nonebot
import pytz
import random
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='23', minute='00')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=874418596,
                                 message=f'现在{now.hour}点啦！赶快给我滚去睡觉！！！')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='10', minute='38')
async def _():
    bot = nonebot.get_bot()
    record = MessageSegment.record("ATOS/ATOS.mp3")
    try:
        await bot.send_group_msg(group_id=874418596,
                                 message=record)
        await bot.send_group_msg(group_id=874418596,
                                 message=f'G114514次列车即将进站，请工作人员做好接车准备')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='10', minute='40')
async def _():
    bot = nonebot.get_bot()
    i = str(random.randint(1, 130))
    record = MessageSegment.record("melody/" + i + ".mp3")
    try:
        await bot.send_group_msg(group_id=874418596,
                                 message=f'G114514次列车即将发车')
        await bot.send_group_msg(group_id=874418596,
                                 message=record)
        await bot.send_group_msg(group_id=874418596,
                                 message=f'车门即将关闭，请注意安全！')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='22', minute='38')
async def _():
    bot = nonebot.get_bot()
    record = MessageSegment.record("ATOS/AOTS.mp3")
    try:
        await bot.send_group_msg(group_id=874418596,
                                 message=record)
        await bot.send_group_msg(group_id=874418596,
                                 message=f'G114514次列车即将进站，请工作人员做好接车准备')
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', hour='22', minute='40')
async def _():
    bot = nonebot.get_bot()
    i = str(random.randint(1, 130))
    record = MessageSegment.record("melody/" + i + ".mp3")
    try:
        await bot.send_group_msg(group_id=874418596,
                                 message=f'G114514次列车即将发车')
        await bot.send_group_msg(group_id=874418596,
                                 message=record)
        await bot.send_group_msg(group_id=874418596,
                                 message=f'车门即将关闭，请注意安全！')
    except CQHttpError:
        pass
