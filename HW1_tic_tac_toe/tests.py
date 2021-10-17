import unittest
from unittest.mock import Mock, patch
from tic_tac_toe import TicTac


class TestTicTac(unittest.TestCase):
    def setUp(self):
        self.game = TicTac()

    @patch('tic_tac_toe.TicTac.__init__', new=[['_' for _ in range(3)] for _ in range(3)])
    def test_put_valid(self):
        # self.game.put('X', 0, 0)
        with self.assertRaises(ValueError):
            self.game.put('X', 0, 0)
