from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import requests

evt_on = 'lighton'
evt_off = 'lightoff'
evt_bright = 'lightbrightness'
key = 'dV7RowWzCO9Te38TaE7T5b'


@on_command('lighton', aliases='开灯')
async def turn_light_on(session: CommandSession):
    event = await light_on()
    await session.send(event)


@on_natural_language(keywords={'开灯'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'lighton')


async def light_on():
    url = (f'https://maker.ifttt.com/trigger/{evt_on}' +
           f'/with/key/{key}')
    requests.post(url)
    res = requests.get(url)
    res = res.text
    print(res)
    if 'Congratulations!' in res:
        result = '已开灯'
    else:
        result = '通讯错误'
    return result


@on_command('lightoff', aliases='关灯')
async def turn_light_off(session: CommandSession):
    event = await light_off()
    await session.send(event)


@on_natural_language(keywords={'关灯'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'lightoff')


async def light_off():
    url = (f'https://maker.ifttt.com/trigger/{evt_off}' +
           f'/with/key/{key}')
    requests.post(url)
    res = requests.get(url)
    res = res.text
    print(res)
    if 'Congratulations!' in res:
        result = '已关灯'
    else:
        result = '通讯错误'
    return result


@on_command('lightbrightness', aliases=('设置亮度', '亮', '暗'))
async def light_brightness(session: CommandSession):
    bright = session.get('bright', prompt='请输入亮度（1-100）')
    event = await light_bright(bright)
    await session.send(event)


@on_natural_language(keywords={'亮','暗','光'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'lightbrightness')


async def light_bright(bright):
    url = (f'https://maker.ifttt.com/trigger/{evt_bright}' +
           f'/with/key/{key}?value1={bright}')
    requests.post(url)
    res = requests.get(url)
    res = res.text
    print(res)
    if 'Congratulations!' in res:
        result = '已设置亮度为' + bright + '%'
    else:
        result = '通讯错误'
    return result
