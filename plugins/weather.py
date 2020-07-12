from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import requests


@on_command('weather', aliases=('天气', '天气预报', '查天气'), only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='想查询哪个城市的天气？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'weather')


async def get_weather_of_city(city: str) -> str:
    url = 'https://yiketianqi.com/api?version=v61&appid=47935297&appsecret=1kH3oCAf&city=' + city
    res = requests.get(url)
    result = '今日' + city + '的天气是' + res.json()['wea'] + '，实时温度' + res.json()['tem'] + '℃，' + res.json()['win'] + \
             res.json()['win_speed'] + '，空气指数：' + res.json()['air']
    return result
