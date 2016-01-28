from pymongo import MongoClient
import urllib
import getpass
import argparse
import sys

__author__ = 'lto'


def usage():
    return "python connect_from_remote.py [-u <username>] [-d] [--password] --ip <CLOUDREPO_IP>\n\nBasically performing \'mongo --host $IP --port $PORT -u $USERNAME -p $PASSWORD --authenticationDatabase \"admin\""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cloud Repository Conncetor', usage=usage())
    parser.add_argument('-u', '--username', help='username for the cloud repository')
    parser.add_argument('-pwd', '--password', help='password for the given username')
    parser.add_argument('-i', '--ip', help='ip of the cloud repository')
    parser.add_argument('-p', '--port', help='port of the cloud repository')

    args = vars(parser.parse_args(sys.argv[1:]))

    ip=''
    if args.get("ip") is None:
        ip='localhost'
    else:
        ip=args.get("ip")
    port=''
    if args.get("port") is None:
        port='27018'
    else:
        port=args.get("port")

    password=''
    if args.get("username") is not None:
        if args.get("password") is None:
            print "Insert the password for the cloud repository:\t"
            password = urllib.quote_plus(getpass.getpass())
        else:
            password = urllib.quote_plus(args.get("password"))

	    client = MongoClient('mongodb://%s:%s@%s:%s' % (args.get("username"), password, ip, port))
    else:
	    client = MongoClient(ip, int(port))

    print 'Connected to %s' % client 

    print "Database are: "
    print client.database_names()
