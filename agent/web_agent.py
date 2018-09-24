# -*- coding: utf-8 -*-
from agent import Agent
import requests


class WebAgent(Agent):
    def play(self, cards_you_have, cards_played, heart_broken, info):
        data = {
            'cards_you_have': cards_you_have,
            'cards_played': cards_played,
            'heart_broken': heart_broken
        }
        result = requests.post(, data)
        return ...

    def pass_cards(self, cards):
        return ...
