import unittest 
from unittest.mock import MagicMock

from Poker.card import Card 

from Poker.hand import Hand
from Poker.player import Player 

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "Boris", hand = hand)
        self.assertEqual(player.name,"Boris")
        self.assertEqual(player.hand,hand)

    def test_figures_out_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"

    

        player = Player(name = "Boris", hand = mock_hand)

        self.assertEqual(player.best_hand(),"Straight Flush")
        
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assets_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_the_game(self):
        player = Player(name = "Sharon", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )