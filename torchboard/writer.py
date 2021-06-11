""" TorchBoard API """

import os
from datetime import datetime

from tinydb import TinyDB

from .constants import METRICS_TABLE_NAME, TB_DIR_NAME


class Writer:

    """ Initialization """

    def __init__(self, log_dir=None):
        # create db
        self._db = self._make_db(log_dir)

        # TODO: start the server & display the url

    """ Public Methods """

    def track(self, **metrics):
        """ Track Metrics """

        # Insert parameters as dict into the db
        self._db.insert(metrics)

    """ Private Methods """

    def _make_db(self, log_dir):
        """ Make Tiny Database """

        # create db path if necessary
        db_path = os.getcwd() if log_dir is None else log_dir
        db_path = os.path.join(db_path, TB_DIR_NAME)
        os.makedirs(db_path) if not os.path.isdir(db_path) else None

        # create db filename using today's date and time
        dt_now = datetime.now().strftime("%b_%d_%Y_%H:%M:%S.%f")
        db_filename = f"logs_{dt_now}.json"

        # join db path components
        db_path = os.path.join(db_path, db_filename)

        # create db
        return TinyDB(db_path).table(METRICS_TABLE_NAME)
