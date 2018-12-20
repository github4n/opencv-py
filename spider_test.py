import requests
import json
import pandas as pd

#接口列表
url = {
    'leaguequerylist': 'https://apic.itou.com/api/match/leaguequerylist', #获取联赛列表
    'finishcount': 'https://apic.itou.com/api/match/finishcount', #历史完场数量
    'selectlist': 'https://apic.itou.com/api/match/selectlist', #当前比赛列表
    'proxymp': 'https://apic.itou.com/api/mdata/proxymp', #近10场战绩
    'proxya': 'https://apic.itou.com/api/mdata/proxya', #该场比赛情况
    'proxya_1': 'https://apic.itou.com/api/mdata/proxya', #最近比赛详情
    'proxymp_1': 'https://apic.itou.com/api/mdata/proxymp', #近10场主客战绩
    'proxymp_2': 'https://apic.itou.com/api/mdata/proxymp', #赔率变化情况
    'proxya_2': 'https://apic.itou.com/api/mdata/proxya', #原型比率变化列表
    'proxya_3': 'https://apic.itou.com/api/mdata/proxya', #原型比率详情
    'proxymp_3': 'https://apic.itou.com/api/mdata/proxymp', #亚原型变化
    'proxya_4': 'https://apic.itou.com/api/mdata/proxya', #亚原型比率变化列表
    'proxya_5': 'https://apic.itou.com/api/mdata/proxya', #交易盈亏详情
    'proxya_6': 'https://apic.itou.com/api/mdata/proxya', #近期比赛统计数据详情
    'proxymp_4': 'https://apic.itou.com/api/mdata/proxymp', #往期赛季表现
    'proxya_7': 'https://apic.itou.com/api/mdata/proxya', #用户表现倾向
    'proxymp_5': 'https://apic.itou.com/api/mdata/proxymp', #比赛双方球员情况
    'proxya_8': 'https://apic.itou.com/api/mdata/proxya', #当前比赛信息
    'proxya_9': 'https://apic.itou.com/api/mdata/proxya', #队员名称列表
    'proxya_10': 'https://apic.itou.com/api/mdata/proxya', #比赛详情
    'prizelist': 'https://apic.itou.com/api/match/prizelist', #往期比赛列表
    'prizeleaguequerylist': 'https://apic.itou.com/api/match/prizeleaguequerylist', #往期比赛列表
}
#参数列表
param = {
    'leaguequerylist': {'platform': 'koudai_mobile', '_prt': 'https', 'ver': '20180101000000'},
    'finishcount': {'platform': 'koudai_mobile', '_prt': 'https', 'ver': '20180101000000'},
    'selectlist': {'platform': 'koudai_mobile', '_prt': 'https', 'ver': '20180101000000', 'hide_more': '1'},
    'proxymp': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/history/digest',
        'dc': '1539239293',
        'sport_id': '1',
        'type': '',
        'match_id': '1042699',
        'channelid': '9',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'user_id': '',
        'device_id': '',
        'app_id': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.score.history.getMatchheadInfo',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_1': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.score.history.gethistory',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxymp_1': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/history/digest',
        'dc': '1539239293',
        'sport_id': '1',
        'type': 'site',
        'match_id': '1042699',
        'channelid': '9',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'user_id': '',
        'device_id': '',
        'app_id': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'channel': 'app.cps.31120.20.a.okooo.com ',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxymp_2': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/odds/oddsdata',
        '_dc': '1539239293',
        'sport_id': '1',
        'MatchID': '1042699',
        'betting_type_id': '1',
        'channelid': '9',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'user_id': '',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_2': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.odds.getOdds',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'betting_type_id': '1',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018  ',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_3': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.stat.getstat',
        '_dc': '1534311823305',
        'SportId': '1',
        'MatchID': '1042699',
        'LId': '24',
        'bettingTypeId': '1',
        'boundary': '1.00',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
        't': '944857',
        '_': '1534311823307',
    },
    'proxymp_3': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/ah/digest',
        '_dc': '1539239293',
        'sport_id': '1',
        'type': 'site',
        'match_id': '1042699',
        'channelid': '4',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'user_id': '',
        'device_id': 'fadf8886e277aaf2842c7e43cf3b0e7c',
        'app_id': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'channel': 'app.tap.myapp.com',
        'VersionNum': '2.4.9',
        'CodeVer': '20161010-001',
    },
    'proxya_4': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.ah.getAh',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'betting_type_id': '2',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_5': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.exchanges.getexchanges',
        '_dc': '1539239293',
        'sportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_6': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.schedule.getExtra',
        '_dc': '1539239293',
        'sportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxymp_4': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/match/feature',
        '_dc': '1539239293',
        'sport_id': '1',
        'match_id': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'app_id': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'channel': 'app.cps.31120.20.a.okooo.com ',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_7': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.note.getlist',
        '_dc': '1539239293',
        'sportId': '1',
        'nodeType': 'all',
        'page': '1',
        'access_token': '',
        'matchId': '1042699',
        'userId': '',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxymp_5': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'soccer/match/playerinfo',
        '_dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'channelid': '9',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'user_id': '',
        'device_id': '',
        'app_id': '5A9089C9-B92A-888B-D563-3BE95247D7C9',
        'channel': 'app.cps.31120.20.a.okooo.com ',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_8': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.score.history.getMatchheadInfo',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_9': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.match.getlineup',
        'dc': '1539239293',
        'SportId': '1',
        'MatchID': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'proxya_10': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'interface': 'mc.data.match.livestatus',
        'dc': '1539239293',
        'sportid': '1',
        'matchid': '1042699',
        'itoukey': '155352b9a7cd26dadd714f41cab3e52f',
        'app_key': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'device_id': '',
        'app_id': 'C14F562F-C6E0-45E3-A2C4-E807BA99B018',
        'channel': 'app.cps.31120.20.a.okooo.com',
        'VersionNum': '1.0.0.1',
        'CodeVer': '20161010-001',
    },
    'prizelist': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'date_list[]': '2018-08-11',
        't': '566924',
        '_': '1534312936616',
    },
    'prizeleaguequerylist': {
        'platform': 'koudai_mobile',
        '_prt': 'https',
        'ver': '20180101000000',
        'date_list[]': '2018-08-11',
        't': '801066',
        '_': '1534312936747',
    },
}

r=requests.get(url['prizelist'], params=param['prizelist'])
print(r.text)
print(json.loads(r.text))