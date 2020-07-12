import requests
import json
import time
import socket
from nonebot import on_command, CommandSession

socket.setdefaulttimeout(20)


@on_command('bus_wuhan', aliases='武汉公交', only_to_me=False)
async def bus_wuhan(session: CommandSession):
    route = session.get('route', prompt='输入线路番号')
    bus_info = await get_bus(route)
    await session.send(bus_info)


@bus_wuhan.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['route'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


def direction0(route):
    direction = '0'
    url = f'http://bus.wuhancloud.cn:9087/website/web/420100/line/027-{route}-{direction}.do?Type=LineDetail'
    header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 '
                          '(KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN'}
    session = requests.session()
    res = session.get(url=url, headers=header)
    res.close()
    result = json.loads(res.text)
    data = result['data']
    stop = data['stops']
    bus0 = str(result['data']['buses'])
    num0 = bus0.count('|')
    num = int(num0 / 5)
    s1 = data['lineName'] + '路' + ' 上行方向 ' + data['startStopName'] + ' 开往 ' + data['endStopName'] + '\n'

    bus1 = dict()
    bus_num0 = dict()
    bus_num = dict()
    bus2 = dict()
    stop0 = dict()
    stop1 = dict()
    stop10 = dict()
    s3 = str()
    stop2 = dict()
    time0 = dict()
    time1 = dict()
    timer = str()
    for i in range(num):
        bus1[i] = bus0.split(" ")[i].replace('[', '').replace(']', '').replace("'", "").replace(',', '')
        bus_num0[i] = bus1[i][0:5].replace('|', '')
        bus_num[i] = str(bus_num0[i])
        bus2[i] = bus1[i][5:]
        if bus_num[i].count('') == 6:
            stop0[i] = bus2[i][4:6]
        elif bus_num[i].count('')  == 5:
            stop0[i] = bus2[i][3:5]
        stop1[i] = str(stop0[i].split('|', 1)[0]).replace('|', '')
        stop10[i] = str(stop1[i])
        if bus_num[i].count('') == 5:
            if stop10[i].count('') == 2:
                time0[i] = bus2[i][5:6]
            elif stop10[i].count('') == 3:
                time0[i] = bus2[i][6:7]
        elif bus_num[i].count('') == 6:
            if stop10[i].count('') == 2:
                time0[i] = bus2[i][6:7]
            elif stop10[i].count('') == 3:
                time0[i] = bus2[i][7:8]
        stop2[i] = int(stop1[i])
        time1[i] = int(time0[i])
        if time1[i] == 0:
            timer = '   即将到达  '
        elif time1[i] == 1:
            timer = '    已到达    '
        s2 = bus_num0[i] + '号车' + timer + stop[stop2[i] - 1]['stopName'] + '\n'
        s3 += s2

    s4 = s1 + '\n' + s3
    return s4


def direction1(route):
    direction = '1'
    url = f'http://bus.wuhancloud.cn:9087/website/web/420100/line/027-{route}-{direction}.do?Type=LineDetail'
    header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 '
                          '(KHTML, like Gecko) Mobile/14F89 MicroMessenger/6.5.10 NetType/WIFI Language/zh_CN'}
    session = requests.session()
    res = session.get(url=url, headers=header)
    res.close()
    result = json.loads(res.text)
    data = result['data']
    stop = data['stops']
    bus0 = str(result['data']['buses'])
    num0 = bus0.count('|')
    num = int(num0 / 5)
    s1 = data['lineName'] + '路' + ' 下行方向 ' + data['startStopName'] + ' 开往 ' + data['endStopName'] + '\n'

    bus1 = dict()
    bus_num0 = dict()
    bus_num = dict()
    bus2 = dict()
    stop0 = dict()
    stop1 = dict()
    stop10 = dict()
    s3 = str()
    stop2 = dict()
    time0 = dict()
    time1 = dict()
    timer = str()
    for i in range(num):
        bus1[i] = bus0.split(" ")[i].replace('[', '').replace(']', '').replace("'", "").replace(',', '')
        bus_num0[i] = bus1[i][0:5].replace('|', '')
        bus_num[i] = str(bus_num0[i])
        bus2[i] = bus1[i][5:]
        if bus_num[i].count('') == 6:
            stop0[i] = bus2[i][4:6]
        elif bus_num[i].count('')  == 5:
            stop0[i] = bus2[i][3:5]
        stop1[i] = str(stop0[i].split('|', 1)[0]).replace('|', '')
        stop10[i] = str(stop1[i])
        if bus_num[i].count('') == 5:
            if stop10[i].count('') == 2:
                time0[i] = bus2[i][5:6]
            elif stop10[i].count('') == 3:
                time0[i] = bus2[i][6:7]
        elif bus_num[i].count('') == 6:
            if stop10[i].count('') == 2:
                time0[i] = bus2[i][6:7]
            elif stop10[i].count('') == 3:
                time0[i] = bus2[i][7:8]
        stop2[i] = int(stop1[i])
        time1[i] = int(time0[i])
        if time1[i] == 0:
            timer = '   即将到达  '
        elif time1[i] == 1:
            timer = '    已到达    '
        s2 = bus_num0[i] + '号车' + timer + stop[stop2[i] - 1]['stopName'] + '\n'
        s3 += s2

    s4 = s1 + '\n' + s3
    return s4


async def get_bus(route: str) -> str:
    if 'N' in route:
        ss1 = direction0(route)
        ss = ss1
    elif 'W' in route:
        ss1 = direction0(route)
        ss = ss1
    else:
        ss1 = direction0(route)
        time.sleep(2)
        ss2 = direction1(route)
        ss = ss1 + '\n\n' + ss2
    return ss
