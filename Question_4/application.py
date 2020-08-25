import ssl

from flask import Flask,render_template,request
import sys,os
import pyodbc
#import memcache
import time
import redis
import pandas as pd
import random
import hashlib
import pickle

import math

from redis.connection import NONBLOCKING_EXCEPTION_ERROR_NUMBERS, ssl_available

app = Flask(__name__)


hostname=
database = 
username =
password = 
redis_password=
cnxn = pyodbc.connect()
cursor = cnxn.cursor()

r = redis.Redis(host='',
        port=6380, db=0, password='',ssl=True)
print("am printing this value", r)




@app.route('/')
def index():
    return render_template('home.html')

# Pie Chart


@app.route('/assignment4pie', methods=['GET','POST'])
def assignment4pie():
    sql1 = " SELECT count(mag) from quake where mag < 1 ; "
    sql2 = " SELECT count(mag) from quake where mag BETWEEN 1 and 2  ; "
    sql3 = " SELECT count(mag) from quake where mag BETWEEN 2 and 3  ; "
    sql4 = " SELECT count(mag) from quake where mag < 5 ; "
    
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    print("result1 is",result1)

    cursor.execute(sql2)
    result2 = cursor.fetchall()
    print("result2 is",result2)

    cursor.execute(sql3)
    result3 = cursor.fetchall()
    print("result3 is",result3)

    cursor.execute(sql4)
    result4 = cursor.fetchall()
    print("result4 is",result4)

    output= [
          ['condition', 'count(mag)'],
          ['mag< 1',result1[0][0]],
          ['mag 1-2',result2[0][0]],
          ['mag 2-3',result3[0][0]],
          ['mag <5',result4[0][0]]
        
        ]
   

    return render_template("assignment4pie.html", ans = output)


# # Bar Chart

@app.route('/assignment4bar', methods=['GET','POST'])
def assignment4bar():
    sql1 = " SELECT count(mag) from quake where mag < 1 ; "
    sql2 = " SELECT count(mag) from quake where mag BETWEEN 1 and 2  ; "
    sql3 = " SELECT count(mag) from quake where mag BETWEEN 2 and 3  ; "
    sql4 = " SELECT count(mag) from quake where mag < 5 ; "
    
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    print("result1 is",result1)

    cursor.execute(sql2)
    result2 = cursor.fetchall()
    print("result2 is",result2)

    cursor.execute(sql3)
    result3 = cursor.fetchall()
    print("result3 is",result3)

    cursor.execute(sql4)
    result4 = cursor.fetchall()
    print("result4 is",result4)

    output= [
          ['condition', 'count(mag)'],
          ['mag< 1',result1[0][0]],
          ['mag 1-2',result2[0][0]],
          ['mag 2-3',result3[0][0]],
          ['mag <5',result4[0][0]]
        
        ]
   

    return render_template("assignment4bar.html", ans = output)



# # scatter graph

@app.route('/assignment4scatter', methods=['GET','POST'])
def assignment4scatter():
    sql1 = " SELECT count(mag) from quake where mag < 1 ; "
    sql2 = " SELECT count(mag) from quake where mag BETWEEN 1 and 2  ; "
    sql3 = " SELECT count(mag) from quake where mag BETWEEN 2 and 3  ; "
    sql4 = " SELECT count(mag) from quake where mag < 5 ; "
    
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    print("result1 is",result1)

    cursor.execute(sql2)
    result2 = cursor.fetchall()
    print("result2 is",result2)

    cursor.execute(sql3)
    result3 = cursor.fetchall()
    print("result3 is",result3)

    cursor.execute(sql4)
    result4 = cursor.fetchall()
    print("result4 is",result4)

    output= [
          ['condition', 'count(mag)'],
          ['mag< 1',result1[0][0]],
          ['mag 1-2',result2[0][0]],
          ['mag 2-3',result3[0][0]],
          ['mag <5',result4[0][0]]
        
        ]
   

    return render_template("assignment4scatter.html", ans = output)

# Line graph

@app.route('/assignment4line', methods=['GET','POST'])
def assignment4line():
    sql1 = " SELECT count(mag) from quake where mag < 1 ; "
    sql2 = " SELECT count(mag) from quake where mag BETWEEN 1 and 2  ; "
    sql3 = " SELECT count(mag) from quake where mag BETWEEN 2 and 3  ; "
    sql4 = " SELECT count(mag) from quake where mag < 5 ; "
    
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    print("result1 is",result1)

    cursor.execute(sql2)
    result2 = cursor.fetchall()
    print("result2 is",result2)

    cursor.execute(sql3)
    result3 = cursor.fetchall()
    print("result3 is",result3)

    cursor.execute(sql4)
    result4 = cursor.fetchall()
    print("result4 is",result4)

    output= [
          ['condition', 'count(mag)'],
          ['mag< 1',result1[0][0]],
          ['mag 1-2',result2[0][0]],
          ['mag 2-3',result3[0][0]],
          ['mag <5',result4[0][0]]
        
        ]
   

    return render_template("assignment4line.html", ans = output)



port = os.getenv('PORT', '3000')
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=int(port))
