import unittest
from unittest.mock import patch
from tic_tac_toe import TicTac


class TestTicTac(unittest.TestCase):
    def setUp(self):
        self.game = TicTac()

    def test_put_invalid(self):
        self.game.put('X', 0, 0)
        with self.assertRaises(ValueError):
            self.game.put('X', 0, 0)

    def test_put_valid(self):
        self.assertIsNone(self.game.put('X', 0, 0))

    def test_validate(self):
        with self.assertRaises(ValueError):
            self.game.validate('X', 0, 10)
        with self.assertRaises(ValueError):
            self.game.validate('X', 10, 0)
        with self.assertRaises(ValueError):
            self.game.validate('10', 0, 0)

    @patch('tic_tac_toe.TicTac.validate', return_value=True)
    def test_check(self, _):
        maps = [
            [
                ('X', 0, 0), ('_', 0, 1), ('_', 0, 2),
                ('_', 1, 0), ('X', 1, 1), ('_', 1, 2),
                ('_', 2, 0), ('_', 2, 1), ('X', 2, 2)
            ],
            [
                ('_', 0, 0), ('_', 0, 1), ('X', 0, 2),
                ('_', 1, 0), ('X', 1, 1), ('_', 1, 2),
                ('X', 2, 0), ('_', 2, 1), ('_', 2, 2)
            ],
            [
                ('X', 0, 0), ('X', 0, 1), ('X', 0, 2),
                ('_', 1, 0), ('_', 1, 1), ('_', 1, 2),
                ('_', 2, 0), ('_', 2, 1), ('_', 2, 2)
            ],
            [
                ('_', 0, 0), ('_', 0, 1), ('_', 0, 2),
                ('X', 1, 0), ('X', 1, 1), ('X', 1, 2),
                ('_', 2, 0), ('_', 2, 1), ('_', 2, 2)
            ],
            [
                ('_', 0, 0), ('_', 0, 1), ('_', 0, 2),
                ('_', 1, 0), ('_', 1, 1), ('_', 1, 2),
                ('X', 2, 0), ('X', 2, 1), ('X', 2, 2)
            ],
            [
                ('X', 0, 0), ('_', 0, 1), ('_', 0, 2),
                ('X', 1, 0), ('_', 1, 1), ('_', 1, 2),
                ('X', 2, 0), ('_', 2, 1), ('_', 2, 2)
            ],
            [
                ('_', 0, 0), ('X', 0, 1), ('_', 0, 2),
                ('_', 1, 0), ('X', 1, 1), ('_', 1, 2),
                ('_', 2, 0), ('X', 2, 1), ('_', 2, 2)
            ],
            [
                ('_', 0, 0), ('_', 0, 1), ('X', 0, 2),
                ('_', 1, 0), ('_', 1, 1), ('X', 1, 2),
                ('_', 2, 0), ('_', 2, 1), ('X', 2, 2)
            ]
        ]

        for map in maps:
            for arguments in map:
                self.game.put(arguments[0], arguments[1], arguments[2])
            self.assertTrue(self.game.check('X'))

    # @patch('tic_tac_toe.TicTac.validate', return_value=True)
    # @patch('tic_tac_toe.TicTac.info', return_value=None)
    # def game_check(self, _,__):
    #     gaming_win_x = [
    #         [
    #             (0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (1, 2), (1, 1), (0, 2), (2, 2)
    #         ],
    #         [
    #             (0, 0), (0, 2), (0, 2), (0, 1), (2, 2), (1, 1), (1, 2)
    #         ],
    #         [
    #             (0, 0), (0, 2), (0, 1), (0, 1), (0, 2)
    #         ]
    #     ]
    #     gaming_win_y = [
    #         [
    #             (0, 0), (1, 1), (1, 0), (2, 0), (0, 1), (2, 1)
    #         ],
    #         [
    #             (2, 2), (1, 2), (2, 1), (1, 1), (0, 0), (1, 0)
    #         ]
    #     ]
        # gaming_rewriting = [
        #     [
        #         (0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (1, 2), (0, 0), (0, 2), (2, 2)
        #     ],
        #     [
        #         (2, 2), (0, 2), (0, 2), (0, 1), (2, 2), (1, 1), (1, 2)
        #     ],
        #     [
        #         (0, 0), (0, 1), (0, 1), (0, 1), (0, 2)
        #     ],
        #     [
        #         (1, 1), (1, 1), (1, 0), (2, 0), (0, 1), (2, 1)
        #     ],
        #     [
        #         (2, 2), (1, 2), (2, 1), (1, 1), (0, 0), (2, 2)
        #     ]
        # ]
        # gaming_out_of_range = [
        #     [
        #         (0, 0), (0, 100), (1, 0), (2, 0), (2, 1), (1, 2), (1, 1), (0, 2), (2, 2)
        #     ],
        #     [
        #         (0, 0), (0, 2), (0, 21), (0, 1), (2, 2), (1, 1), (1, 2)
        #     ],
        #     [
        #         (0, 0), (0, 2), (0, 1), (0, 31), (0, 2)
        #     ],
        #     [
        #         (20, 0), (1, 1), (1, 0), (2, 0), (0, 1), (2, 1)
        #     ],
        #     [
        #         (2, 2), (1, 2), (2, 1), (15, 1), (0, 0), (1, 0)
        #     ]
        # ]

