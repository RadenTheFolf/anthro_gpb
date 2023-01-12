import logging
import threading
import time
import git


def check_for_updates():
    logging.info("Checking for updates before launch...")
    g = git.cmd.Git('.')
    result = g.pull()
    print(result.flags)
    logging.info("Applying updates...")


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Preparing to launch  AnthroGPB...")
    check_for_updates()