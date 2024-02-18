import pytest
import requests
from unittest.mock import Mock
from open_meteo_weather_sample_jpcity import get

# モジュールレベルの定数として定義
# TODO: 実装コード側と重複するので集約。定数なので検証対象外であり、コード側を参照したい。
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

# locationとexpected_resultのペアをリストで定義
locations_and_results = [
    ("tokyo", {
        "location": "tokyo",
        "time"          : "dummy_time",
        "temperature_2m": "dummy_temperature"
    }),
    ("nagoya", {
        "location": "nagoya",
        "time"          : "dummy_time",
        "temperature_2m": "dummy_temperature"
    }),
    ("osaka", {
        "location": "osaka",
        "time"          : "dummy_time",
        "temperature_2m": "dummy_temperature"
    })
]

# パラメータ化されたテスト関数を定義
@pytest.mark.parametrize("location, expected_result", locations_and_results)
def test_get(location, expected_result):
    """
    This is the title of the test case.
    """
    
    # モックオブジェクトを作成
    mock_response = Mock()
    mock_response.json.return_value = {"hourly": expected_result}

    # requests.getをモックに置き換え
    requests.get = Mock(return_value=mock_response)

    # 関数をテスト
    result = get(location)
    assert result == expected_result

    # APIが正しいURLで呼び出されたことを確認
    selected_location = LOCATION_DICT[location]
    latitude = selected_location["latitude"]
    longitude= selected_location["longitude"]
    timezone = "Asia%2FTokyo"
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone={timezone}&hourly=temperature_2m"
    requests.get.assert_called_once_with(
        url,
        headers={'user-agent' : 'curl'}
    )
