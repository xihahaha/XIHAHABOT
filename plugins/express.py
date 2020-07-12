import json
import urllib
import urllib.request
import hashlib
import base64
import urllib.parse
from nonebot import on_command, CommandSession


@on_command('kuaidi', aliases='快递', only_to_me=False)
async def kuaidi(session: CommandSession):
    code = session.get('code', prompt='输入单号')
    code_info = await recognise(code)
    await session.send(code_info)


@kuaidi.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['code'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


def encrypt(origin_data, appkey):
    m = hashlib.md5()
    m.update((origin_data+appkey).encode("utf8"))
    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
    return base64_text


def sendpost(url, datas):
    """发送post请求"""
    postdata = urllib.parse.urlencode(datas).encode('utf-8')
    header = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }
    req = urllib.request.Request(url, postdata, header)
    get_data = (urllib.request.urlopen(req).read().decode('utf-8'))
    return get_data


def get_company(logistic_code, appid, appkey, url):
    data1 = {'LogisticCode': logistic_code}
    d1 = json.dumps(data1, sort_keys=True)
    requestdata = encrypt(d1, appkey)
    post_data = {
        'RequestData': d1,
        'EBusinessID': appid,
        'RequestType': '2002',
        'DataType': '2',
        'DataSign': requestdata.decode()}
    json_data = sendpost(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data


def get_traces(logistic_code, shipper_code, appid, appkey, url):
    data1 = {'LogisticCode': logistic_code, 'ShipperCode': shipper_code}
    d1 = json.dumps(data1, sort_keys=True)
    requestdata = encrypt(d1, appkey)
    post_data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '1002', 'DataType': '2',
                 'DataSign': requestdata.decode()}
    json_data = sendpost(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data


async def recognise(code: str) -> str:
    url = 'http://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx'
    APP_id = "在此输入你的ID"
    APP_key = "在此输入你的KEY"
    data = get_company(code, APP_id, APP_key, url)
    s4 = str()
    if not any(data['Shippers']):
        s1 = "未查到该快递信息,请检查快递单号是否有误！"
    else:
        s1 = "已查到" + str(data['Shippers'][0]['ShipperName']) + "（" + str(data['Shippers'][0]['ShipperCode']) + "）" + code + '\n'
        trace_data = get_traces(code, data['Shippers'][0]['ShipperCode'], APP_id, APP_key, url)
        if trace_data['Success'] == "false" or not any(trace_data['Traces']):
            s2 = "未查询到该快递物流轨迹！" + '\n'
        else:
            str_state = "问题件"
            if trace_data['State'] == '2':
                str_state = "在途中"
            if trace_data['State'] == '3':
                str_state = "已签收"
            s2 = "目前状态： " + str_state + '\n'
            trace_data = trace_data['Traces']
            item_no = 1
            for item in trace_data:
                s3 = str(item_no) + "： " + item['AcceptTime'] + ' ' + item['AcceptStation'] + '\n'
                s4 += s3
                item_no += 1
    s = s1 + s2 + s4
    return s
