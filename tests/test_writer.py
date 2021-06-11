""" TorchBoard API Tests """

import os
import shutil
import unittest as ut

from tinydb import where

import torchboard as tb


class WriterTests(ut.TestCase):

    """ SetUp & TearDown """

    def setUp(self):
        # Check log dir
        self.log_dir = os.path.join(os.getcwd(), tb.constants.TB_DIR_NAME)

    def tearDown(self):
        # Remove created log dir
        if os.path.isdir(self.log_dir):
            shutil.rmtree(self.log_dir)

    """ Tests """

    def test_init_withDefaultLogDir_shouldCreateEmptyDB(self):
        board = tb.Writer()
        self.assertTrue(os.path.isdir(self.log_dir))

    def test_init_withCustomLogDir_shouldCreateEmptyDB(self):
        custom_log_dir = os.path.join(os.getcwd(), "custom_log_dir")
        os.mkdir(custom_log_dir)
        board = tb.Writer(log_dir=custom_log_dir)

        log_dir = os.path.join(custom_log_dir, tb.constants.TB_DIR_NAME)

        self.assertTrue(os.path.isdir(log_dir))
        shutil.rmtree(custom_log_dir)

    def test_track_shouldWriteLogs(self):
        board = tb.Writer()
        db = board._db
        board.track(loss="some_stuff")

        tracked_losses = db.search(where("loss") == "some_stuff")
        self.assertEqual(len(tracked_losses), 1)
