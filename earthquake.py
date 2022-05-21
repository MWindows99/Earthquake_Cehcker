import requests
import json

def earthquake():
    request_url = "https://api.p2pquake.net/v2/history?codes=551&limit=1"
    try:
        r = requests.get(request_url, timeout=4.0)
        earth_data = r.json()[0]
    except:
        return False
    e_point = str(earth_data["earthquake"]["hypocenter"]["name"])
    e_tsunami = str(earth_data["earthquake"]["domesticTsunami"])
    e_magnitude = int(earth_data["earthquake"]["hypocenter"]["magnitude"])
    e_scale = int(earth_data["earthquake"]["maxScale"])
    e_time = str(earth_data["earthquake"]["time"])
    if e_point == '':
        e_point = "不明/調査中"
    if e_magnitude == -1:
        e_magnitude = "不明"
    else:
        e_magnitude = str(e_magnitude)
    if e_scale == -1:
        e_scale = "不明"
    else:
        e_scale = str(e_scale / 10)
    if e_tsunami == 'None':
        e_tsunami_mes = "この地震による、津波の心配はありません。"
    elif e_tsunami == "Unknown":
        e_tsunami_mes = "この地震による、津波の情報は不明です。"
    elif e_tsunami == "Checking":
        e_tsunami_mes = "この地震による、津波の情報は現在調査中です。"
    elif e_tsunami == "Watch":
        e_tsunami_mes = "この地震により、津波注意報が発表されています。今後の情報に注意してください。詳しい情報は、気象庁ホームページをご確認ください。"
    elif e_tsunami == "Warning":
        e_tsunami_mes = "この地震により、津波予報が発表されています。落ち着いて速やかに行動してください。詳しい情報は、気象庁ホームページをご確認ください。"
    message = {}
    message["point"] = e_point
    message["time"] = e_time
    message["magnitude"] = e_magnitude
    message["scale"] = e_scale
    message["tsunami"] = e_tsunami_mes
    return message
