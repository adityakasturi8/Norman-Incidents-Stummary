#!/usr/bin/python3
import urllib.request
import tempfile
import PyPDF2
import sqlite3
import re

def fetch_incidents(url):
    '''
    fetch_incidents(url):
    This function is being used to open the url from norman police department daily incidents summary and read it
    url = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-01_daily_incident_summary.pdf")
   '''
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data 

def extract_incidents(incident_data):
    '''
        In this function we are extracting the data from the pdf file and extracts the incidents. Each incident include data_time, incident number, incident location, nature, and incident ori
    '''
    fp = tempfile.TemporaryFile()
    fp.write(incident_data)
    fp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pagecount =  pdfReader.getNumPages()
    completedata = []
    for pagenum in range(pagecount):
        p = pdfReader.getPage(pagenum).extractText()

        fulldata = p.replace(" \n"," ")
 

        fulldata = re.split(r'\s+(?=\d?\d?\/\d?\d?\/\d{4} \d?\d?:\d?\d?)', fulldata)
       
        for i in range(len(fulldata)):
            fulldata[i] = fulldata[i].split("\n")
            if (len(fulldata[i]) == 5):
                completedata.append(fulldata[i])
    return completedata

def createdb(db = 'normanpd.db'):
    '''
    In this Function we create a database and insert the table with the schema mentioned in the below code 
    '''
    connect = sqlite3.connect(db)
    cur = connect.cursor()
    cur.execute("DROP TABLE IF EXISTS incidents")
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
        incident_time TEXT DEFAULT 'NA',
            incident_number TEXT DEFAULT 'NA',
                incident_location TEXT DEFAULT 'NA',
                    nature TEXT DEFAULT 'NA',
                        incident_ori TEXT DEFAULT 'NA'
                        )''')
    connect.commit()
    connect.close()
    return db

def populatedb(db, incidents):
    '''
    populating the database , Used the following link for reference
    https://stackoverflow.com/questions/37058984/insert-multiple-rows-into-db-with-python-list-of-tuples 
    '''

    connect = sqlite3.connect(db)
    cur = connect.cursor()
    cur.executemany("INSERT into incidents VALUES  (?,?,?,?,?)", incidents)
    connect.commit()
    connect.close()
    return True
def status(db):
    '''
    Status, and fetching all data
    '''

    connect = sqlite3.connect(db)

    cur = connect.cursor()
   # cur.execute("SELECT * FROM incidents")
    cur.execute("SELECT nature , count(*) from incidents group by nature order by nature")
    storage = cur.fetchall()
    for row in storage:
        print(row[0], "|",row[1])
    cur.execute("DROP TABLE IF EXISTS INCIDENTS")
    cur.close()
    return True

