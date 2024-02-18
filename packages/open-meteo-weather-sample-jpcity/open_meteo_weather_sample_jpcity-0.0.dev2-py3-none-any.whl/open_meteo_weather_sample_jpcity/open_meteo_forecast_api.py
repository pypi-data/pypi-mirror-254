import requests

# モジュールレベルの定数として定義
LOCATION_DICT: dict = {
    "tokyo" : {
        "latitude" : "35.6785",
        "longitude": "139.6823",
    },
    "nagoya" : {
        "latitude" : "35.1814",
        "longitude": "136.9063",
    },
    "osaka" : {
        "latitude" : "34.6937",
        "longitude": "135.5021",
    },
}


def list_locations() -> list:
    cityname_list = list(LOCATION_DICT.keys())
    return cityname_list


def get(location: str) -> dict:
    # 関数の外側に定義された定数を参照
    selected_location = LOCATION_DICT[location]
    latitude = selected_location["latitude"]
    longitude= selected_location["longitude"]
    timezone = "Asia%2FTokyo"
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone={timezone}&hourly=temperature_2m"
    # https://paiza.hatenablog.com/entry/2021/11/04/130000
    #
    # f文字列（f-strings、フォーマット文字列、フォーマット済み文字列リテラル
    # https://note.nkmk.me/python-f-strings/

    response = requests.get(url, headers={'user-agent' : 'curl'})
    hourly = response.json()["hourly"]
    return {
        "location": location,
        "time"          : hourly["time"],
        "temperature_2m": hourly["temperature_2m"]
    }
    # return response.text




