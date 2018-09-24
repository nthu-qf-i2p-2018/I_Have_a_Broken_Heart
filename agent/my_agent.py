# -*- coding: utf-8 -*-
from agent import Agent
from game import Game
from card import Card
from card import _number as NUM_RANK


class MyAgent(Agent):
    def play(self, cards_you_have, cards_played, heart_broken, info):
        # print(cards_you_have)
        legal_cards = Game.get_legal_moves(cards_you_have, cards_played, heart_broken)
        if cards_played:
            lead = cards_played[0].suit
            if legal_cards[0].suit == lead:
                biggest_card = max(card for card in cards_played if card.suit == lead)
                point_sum = sum(card.point for card in cards_played)
                points = {card: point_sum+card.point if card > biggest_card else 0 for card in legal_cards}
                min_point = min(points.values())
                candidate = [card for card in legal_cards if points[card] == min_point]
                if len(cards_played) == 3:
                    return min(candidate, key=self.get_card_rank)
                else:
                    good_candidates = [card for card in candidate if card < biggest_card]
                    if good_candidates:
                        return min(good_candidates, key=self.get_card_rank)
                    else:
                        return max(candidate, key=self.get_card_rank)
            else:
                return min(legal_cards, key=self.get_card_rank)
        else:

            return max(legal_cards, key=self.get_card_rank)

    def pass_cards(self, cards):
        # print(cards)
        cards_to_pass = []

        for i in (1, 13, 12):
            bad_card = Card('♠', i)
            if bad_card in cards:
                cards_to_pass.append(bad_card)

        for i in (1, 13, 12, 11, 10):
            bad_card = Card('♥', i)
            if bad_card in cards:
                cards_to_pass.append(bad_card)

        for num in (1, 13, 12, 11, 10, 9, 8):
            for suit in ('♣', '♦'):
                bad_card = Card(suit, num)
                if bad_card in cards:
                    cards_to_pass.append(bad_card)

        # for card in cards_temp if card]
        if len(cards_to_pass) < 3:
            cards_left = set(cards) - set(cards_to_pass)
            candidates = sorted(cards_left, key=self.get_card_rank)
            cards_to_pass.extend(candidates[:3-len(cards_to_pass)])

        return cards_to_pass[:3]

    def get_card_rank(self, card):
        if card.suit == '♠':
            if card >= Card('♠', 12):
                return -100, -NUM_RANK[card.number]
            else:
                return 100, -NUM_RANK[card.number]
        else:
            return -card.point, -NUM_RANK[card.number]
