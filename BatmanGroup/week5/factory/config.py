import json


class Config:
    DB = {}


class DevConfig(Config):
    DB = {
            "Player1": {"Full_name": "Full name Player1", "Age": "20", "Club": "Club1"},
            "Player2": {"Full_name": "Full name Player2", "Age": "20", "Club": "Club2"},
            "Player3": {"Full_name": "Full name Player3", "Age": "20", "Club": "Club3"},
     }


class TestConfig(Config):
    DB = {
            "Rooney": {"Full_name": "Wayne Mark Rooney", "Age": "32", "Club": "DC"},
            "Ibrahimovic": {"Full_name": "Zlatan Ibrahimovic", "Age": "37", "Club": "LA Galaxy"},
            "Messi": {"Full_name": "Lionel Messi", "Age": "31", "Club": "Barcelona"},
     }


def runtime_config():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        if settings['env'] == "DEV":
            return DevConfig
        if settings['env'] == "TEST":
            return TestConfig
        else:
            return Config
