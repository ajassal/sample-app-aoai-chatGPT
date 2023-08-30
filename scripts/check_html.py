import sys
import os
import logging

logging.basicConfig(level=logging.INFO)

from data_utils import HTMLParser

ip_path = sys.argv[1]

def check(fpath):
    logging.info("Checking: %s", fpath)
    hp = HTMLParser()
    with open(fpath) as f:
        content = f.read()
    document = hp.parse(content, os.path.basename(fpath))

def main():
    if os.path.isdir(ip_path):
        for fname in os.listdir(ip_path):
            ip_fpath = os.path.join(ip_path, fname)
            if os.path.splitext(ip_fpath)[-1].lower() == ".html":
                try:
                    check(ip_fpath)
                except Exception as e:
                    logging.exception(e)
    else:
        check(ip_path)

main()
