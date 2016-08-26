import sqlite3
import sys, getopt

from init_news_db import init_news_db
from search_news import search_news

# Always use console encoding
enc = sys.stdout.encoding

# Function for reading command line arguments
def processArguments(argv):
    # Get optcodes and input from cammand line arguments
    opts, args = getopt.getopt(argv,"i:o:t:",["indb=","outdb=","type="])
    in_db = ""
    out_db = ""
    games_db = ""
    stype = ""
    for opt, arg in opts:
        if opt in ("-i", "--indb"):
            in_db = arg
        elif opt in ("-o", "--outdb"):
            out_db = arg
        elif opt in ("-t", "--type"):
            stype = arg
    if out_db == "":#stype == "" or  or in_db == "":
        # <type> - type of search (games, images, etc)
        # <inputdb> - name of the input db file
        # <outputdb> - name of the output db file
        print ("Please use: python process.py -t <type> -i <inputdb> -o <outputdb>")
    else:
        return (stype, (out_db, in_db))

# Finds articles that are about the same event
def aggregate(out_db, in_db=""):
    out_db = sqlite3.connect(out_db)
    init_news_db(out_db)
    search_news(out_db)

if __name__ == "__main__":
    args = processArguments(sys.argv[1:])
    if args != None:
        stype, args = args
        if stype == "":
            aggregate(*args)