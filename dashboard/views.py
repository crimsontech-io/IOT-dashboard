from django.shortcuts import render
import sqlite3
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import json

def index(request):
    import sqlite3
    import os.path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "codes.db")
    
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    label=[]
    date=[]
    dateL=[]
    countD=[]
    counting=cur.execute('''SELECT
    date,
    COUNT(date) date_count
FROM
    qrcodes
GROUP BY
    date;''')

   
    for a,b in counting:
        # print(a)
        # dat=datetime.strptime(str(a), '%Y-%m-%d').date()
        dateL.append(a)
        countD.append(b)

    
    all=cur.execute('''SELECT * FROM qrcodes;''')
    for x,y in all:

       
        label.append(x) 
        daty=datetime.strptime(str(y), '%Y-%m-%d').date()

        date.append(str(daty))

    dates=json.dumps(date)
    dateL=json.dumps(dateL)
    context={
        'label':label,
        'date':dates,
        'dateL':dateL,
        'countD':countD,
        'totalCount':len(label),
        'last':countD[-1],
        'lastQr':label[-1],
        'lastDate':date[-1],
    }
    print()
    return render(request,'index.html',context)