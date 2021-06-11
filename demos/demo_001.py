"""
Demo 001: Create a logger
"""

import os
import shutil

import torchboard as tb


LOG_DIR = os.path.join(os.getcwd(), "temp")


def demo_001():
    """ Create a tb logger in the `temp` path """

    # Create logger
    logger = tb.Writer(log_dir=LOG_DIR)

    # Insert a couple of metrics
    logger.track(loss=0.972, acc=0.456)
    logger.track(loss=0.968, acc=0.702)
    logger.track(loss=0.853, acc=0.653)
    logger.track(loss=0.846, acc=0.795)
    logger.track(loss=0.646, acc=0.795)
    logger.track(loss=0.502, acc=0.883)
    logger.track(loss=0.383, acc=0.901)


if __name__ == "__main__":
    # Remove tmp folder JIC
    shutil.rmtree(LOG_DIR)

    # Run demo
    demo_001()
