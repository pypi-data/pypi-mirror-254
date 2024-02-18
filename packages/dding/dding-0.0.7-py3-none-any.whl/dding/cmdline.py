# -*- coding: utf-8 -*-
import argparse
import sys

from dding.notify import notify_dding


def main():
    if len(sys.argv) == 2:
        print(sys.argv[1])
        notify_dding(group='default', content=sys.argv[1], title='',msgtype='text')
    elif len(sys.argv) == 3:
        notify_dding(group=sys.argv[1], content=sys.argv[2], title='',msgtype='text')
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('--group', default='default')
        parser.add_argument('--content', default='')
        parser.add_argument('--title', default='')
        parser.add_argument('--msgtype', default='text')
        args = parser.parse_args()

        params = vars(args)
        # print(params)

        notify_dding(**params)


def usage():
    print("usage: dding group=[custom name] content=hello")
    print("usage: dding --group default --content hello --title hello --msgtype markdown")
    print("usage: dding --content hello --msgtype text")
    print("example: dding helloworld")


def test1():
    content="### 杭州天气 \n> 1111"
    # content="### 杭州天气 \n 1111"

    notify_dding(group='default', title='hello',content=sys.argv[1], msgtype='text')

if __name__ == '__main__':
    main()
    # test1()

