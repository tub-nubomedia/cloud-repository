from pymongo import MongoClient
import urllib
import getpass
import argparse
import sys

__author__ = 'lto'


def usage():
    return "python connect_from_remote.py [-u <username>] [-d] [--password] --ip <CLOUDREPO_IP>"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cloud Repository Conncetor', usage=usage)
    parser.add_argument('-u', '--username', help='username for the cloud repository, default is \'nubomedia\'')
    parser.add_argument('-pwd', '--password', help='password for the given username')
    parser.add_argument('-d', '--debug', help='activate debug', action='store_true')
    parser.add_argument('--ip', help='ip of the cloud repository', required=True)

    args = vars(parser.parse_args(sys.argv[1:]))

    password=''

    if args.get("password") is None:
        print "Insert the password for the cloud repository:\t"
        password = urllib.quote_plus(getpass.getpass())
    else:
        password = urllib.quote_plus(args.get("password"))

    # mongo --port 27018 -u "myUserAdmin" -p "abc123" --authenticationDatabase "admin"

    client = MongoClient('mongodb://%s:%s@%s:27018' % (args.get("username"), password, args.get("ip")))

    print "Database are: "
    print client.database_names()