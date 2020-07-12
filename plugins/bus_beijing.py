import requests
import re
from nonebot import on_command, CommandSession


@on_command('bus_beijing', aliases='北京公交', only_to_me=False)
async def bus_beijing(session: CommandSession):
    route = session.get('route', prompt='输入线路番号')
    bus_info = await get_bus(route)
    await session.send(bus_info)


@bus_beijing.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['route'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


def getLineDir(bus):
    # 构建请求链接
    selbline = requests.utils.quote(bus)
    url = 'http://www.bjbus.com/home/ajax_rtbus_data.php?act=getLineDir&selBLine={}'.format(selbline)
    r = requests.Session().get(url)
    r.encoding = r.apparent_encoding  # 处理编码
    rt = r.text
    # 匹配信息
    uuid_list = re.findall('(?<=data-uuid=")\d+', rt)
    l = len(uuid_list)
    uuid_0 = uuid_list[0]
    uuid_1 = ''
    if l == 2:
        uuid_1 = uuid_list[1]
    busdir_list = re.findall('\((.*?)\)', rt)
    busdir_0 = busdir_list[0]
    busdir_1 = ''
    if l == 2:
        busdir_1 = busdir_list[1]
    return uuid_0, uuid_1, busdir_0, busdir_1


def getbus(uuid):
    url = 'http://www.bjbus.com/home/ajax_rtbus_data.php?act=busTime&selBLine=1&selBDir={}&selBStop=1'.format(uuid)
    r = requests.Session().get(url)
    html = eval(r.text)['html']
    busc = re.findall('(?<=id=")\d+(?=m"><i  class="busc")', html)
    busc = [int(i) for i in busc]
    buss = re.findall('(?<=id=")\d+(?="><i class="buss")', html)
    buss = [int(i) for i in buss]
    bus_list = re.findall('(?<=title=").+?(?=")', html)
    return busc, buss, bus_list


def print_res(busc, buss, bus_list):
    s2 = str()
    for i in range(0, len(bus_list)):
        if i in busc:
            s1 = "即将到达：" + bus_list[i] + "\n"
            s2 += s1
        elif i in buss:
            s1 = "已到达：" + bus_list[i] + "\n"
            s2 += s1
            continue
    return s2


async def get_bus(route: str) -> str:
    # 输入车次信息，获取班车的特征码uuid以及始末站
    uuid_0, uuid_1, busdir_0, busdir_1 = getLineDir(route)
    if uuid_1 != '':
        bus_0 = route + '路 ' + ' 上行方向  ' + busdir_0 + '\n'
        busc, buss, bus_list = getbus(uuid_0)
        s_0 = print_res(busc, buss, bus_list)
        bus_1 = route + '路 ' + ' 下行方向  ' + busdir_1 + '\n'
        busc, buss, bus_list = getbus(uuid_1)
        s_1 = print_res(busc, buss, bus_list)
    elif uuid_1 == '':
        bus_0 = route + '路 ' + ' 单行线  ' + busdir_0 + '\n'
        busc, buss, bus_list = getbus(uuid_0)
        s_0 = print_res(busc, buss, bus_list)
        bus_1 = ''
        s_1 = ''
    s = bus_0 + s_0 + '\n' + bus_1 + s_1
    return s
