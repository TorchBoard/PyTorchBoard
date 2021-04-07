""" Unit Tests Runner """

import os
import sys
import unittest


if __name__ == "__main__":
    # allow module import
    sys.path.append(os.getcwd())

    # setup loader, runner and suite
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    suite = loader.discover("./tests")

    # run tests and store result
    result = runner.run(suite)

    # exit with result code
    ret_code = not result.wasSuccessful()
    sys.exit(ret_code)
