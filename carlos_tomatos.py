import argparse
from typing import List

import gevent
import grequests
from pytoml import load


class Color:
    pass


class Song:
    pass


class Music:
    song: Song


class LightConfig:
    color: Color
    intensity: float


class WaterConfig:
    day_limit: float


class RaidenConfig:
    server: str


class TomatosConfig:
    monitor_sleep: float
    light: LightConfig
    water: WaterConfig


class Config:
    raiden_config: RaidenConfig
    tomatos_config: TomatosConfig


class Watering:
    water: int


class Lightining:
    time: int


class DiscJockey:
    pass


class schedule:
    water_schedule: List[Watering]
    light_schedule: List[Lightining]
    song_schedule: List[DiscJockey]


class CarlosTomatos:
    def __init__(self, config):
        self.config = config

    def _schedule_actions(self):
        pass

    def monitor(self):
        config = self.config
        while True:
            gevent.sleep(config.monitor_sleep)
            self._schedule_actions()


def load_config(config_path: str):
    with open(config_path) as file_handler:
        config = load(file_handler)

        raiden_service_config = RaidenConfig(
            config['raiden']['serve'],
        )
        tomatos_config = TomatosConfig()

        config = Config(
            raiden_service_config,
            tomatos_config,
        )
        return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file')
    args = parser.parse_args()

    config = load_config(args.config_file)

    tomatos = CarlosTomatos(config)
    tomatos.monitor()
