from . import open_meteo_forecast_api as forecast 

def get(location: str = "tokyo") -> dict:
    return forecast.get(location)

def list_locations() -> list:
    return forecast.list_locations()

def main() -> None:
    result_dict = get()
    print(result_dict["location"])
    print(result_dict["time"])
    print(result_dict["temperature_2m"])

