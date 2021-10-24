import unittest
from list_class import CustomList


class TestCustomList(unittest.TestCase):
    def test_add_custom_custom(self):
        sums = [
            [
                [1, 2, 3], [3, 2, 1], [4, 4, 4]
            ],
            [
                [1], [3, 2, 1], [4, 2, 1]
            ],
            [
                [1, 2, 3], [1], [2, 2, 3]
            ],
            [
                [], [3, 2, 1], [3, 2, 1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in sums:
            self.assertEqual(CustomList(param[0]) + CustomList(param[1]), CustomList(param[2]))

    def test_add_custom_list(self):
        sums = [
            [
                [1, 2, 3], [3, 2, 1], [4, 4, 4]
            ],
            [
                [1], [3, 2, 1], [4, 2, 1]
            ],
            [
                [1, 2, 3], [1], [2, 2, 3]
            ],
            [
                [], [3, 2, 1], [3, 2, 1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in sums:
            self.assertEqual(CustomList(param[0]) + param[1], CustomList(param[2]))

    def test_radd_list_custom(self):
        sums = [
            [
                [1, 2, 3], [3, 2, 1], [4, 4, 4]
            ],
            [
                [1], [3, 2, 1], [4, 2, 1]
            ],
            [
                [1, 2, 3], [1], [2, 2, 3]
            ],
            [
                [], [3, 2, 1], [3, 2, 1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in sums:
            self.assertEqual(param[0] + CustomList(param[1]), CustomList(param[2]))

    def test_sub_custom_custom(self):
        subs = [
            [
                [1, 2, 3], [3, 2, 1], [-2, 0, 2]
            ],
            [
                [1], [3, 2, 1], [-2, -2, -1]
            ],
            [
                [1, 2, 3], [1], [0, 2, 3]
            ],
            [
                [], [3, 2, 1], [-3, -2, -1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in subs:
            self.assertEqual(CustomList(param[0]) - CustomList(param[1]), CustomList(param[2]))

    def test_sub_custom_list(self):
        subs = [
            [
                [1, 2, 3], [3, 2, 1], [-2, 0, 2]
            ],
            [
                [1], [3, 2, 1], [-2, -2, -1]
            ],
            [
                [1, 2, 3], [1], [0, 2, 3]
            ],
            [
                [], [3, 2, 1], [-3, -2, -1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in subs:
            self.assertEqual(CustomList(param[0]) - param[1], CustomList(param[2]))

    def test_rsub_list_custom(self):
        subs = [
            [
                [1, 2, 3], [3, 2, 1], [-2, 0, 2]
            ],
            [
                [1], [3, 2, 1], [-2, -2, -1]
            ],
            [
                [1, 2, 3], [1], [0, 2, 3]
            ],
            [
                [], [3, 2, 1], [-3, -2, -1]
            ],
            [
                [3, 2, 1], [], [3, 2, 1]
            ],
            [
                [0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
            ],
            [
                [], [], []
            ]
        ]
        for param in subs:
            self.assertEqual(param[0] - CustomList(param[1]), CustomList(param[2]))

    def test_equals_custom_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) == CustomList(param[1]), param[2])

    def test_equals_custom_list(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) == param[1], param[2])

    def test_equals_list_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] == CustomList(param[1]), param[2])

    def test_ne_custom_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) != CustomList(param[1]), not param[2])

    def test_ne_custom_list(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) != param[1], not param[2])

    def test_ne_list_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] != CustomList(param[1]), not param[2])

    def test_lt_custom_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) < CustomList(param[1]), param[2])

    def test_lt_custom_list(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) < param[1], param[2])

    def test_lt_list_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] < CustomList(param[1]), param[2])

    def test_gt_custom_custom(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) > CustomList(param[1]), param[2])

    def test_gt_custom_list(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) > param[1], param[2])

    def test_gt_list_custom(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [10, -4], False
            ],
            [
                [6], [3, 1, 2], False
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], False
            ],
            [
                [], [], False
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] > CustomList(param[1]), param[2])

    def test_le_custom_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) <= CustomList(param[1]), param[2])

    def test_le_custom_list(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) <= param[1], param[2])

    def test_le_list_custom(self):
        equals = [
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [1], False
            ],
            [
                [], [3, 2, 1], True
            ],
            [
                [3, 2, 1], [], False
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] <= CustomList(param[1]), param[2])

    def test_ge_custom_custom(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) >= CustomList(param[1]), param[2])

    def test_ge_custom_list(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(CustomList(param[0]) >= param[1], param[2])

    def test_ge_list_custom(self):
        equals = [
            [
                [10, 2, 3], [3, 2, 1], True
            ],
            [
                [10, 2, 3], [30, 2, 1], False
            ],
            [
                [1, 2, 3], [3, 2, 1], True
            ],
            [
                [1, 2, 3], [10, -4], True
            ],
            [
                [6], [3, 1, 2], True
            ],
            [
                [1], [3, 2, 1], False
            ],
            [
                [1, 2, 3], [1], True
            ],
            [
                [], [3, 2, 1], False
            ],
            [
                [3, 2, 1], [], True
            ],
            [
                [0, 0], [0, 0, 0, 0], True
            ],
            [
                [], [], True
            ]
        ]
        for param in equals:
            self.assertEqual(param[0] >= CustomList(param[1]), param[2])