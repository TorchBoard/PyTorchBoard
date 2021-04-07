""" TorchBoard API Tests """

import unittest as ut

import torchboard as tb


class TorchBoardTests(ut.TestCase):
    def test_init_shouldHaveEmptyMetrics(self):
        board = tb.api.TorchBoard()
        self.assertFalse(board.metrics)
