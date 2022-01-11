import sys
import re
import random
from random import randint
import datetime
import csv
import pandas as pd
import time
import sqlite3


database_path = "../sqlite_database/rank.db"
con = sqlite3.connect(database_path)
cursor = con.cursor()

url = sys.argv[1]
keyword = "some text"
date = "06-01-2022"
position = "10"

insert = "INSERT INTO rank (url, keyword, date, rank) values ('" + \
    url + "', '" + keyword + "', '" + date + "', " + position + ")"
print(insert)

cursor.execute(insert)
cursor.execute("COMMIT")
