#!/usr/bin/python
import re
import subprocess
import datetime
import time
import os
import gzip

fop=open("output.html",'a')
fop.write("<!DOCTYPE html><html><head><style>table {  font-family: arial, sans-serif; border-collapse: collapse; width: 100%; }  td, th {  border: 1px solid #dddddd;   text-align: left;   padding: 8px; }  tr:nth-child(even) {   background-color: #dddddd; } </style> </head> <body> <h2>DAILY::ZXTM CCP MONITORING </h2>")

fop.write("<table>")
fop.write("<tr><th>DATE</th><th>GET REQUEST</th><th>POST REQUEST</th><th>200</th><th>201</th><th>202</th><th>404</th><th>500</th><th>ABORT REQUEST</th></tr>")
year=datetime.datetime.now().year
month=datetime.datetime.now().month
day=datetime.datetime.now().day


grep_list=["GET","POST",r'\b200\b',r'\b201\b',r'\b202\b',r'\b404\b',r'\b500\b',r'\b503\b',"favicon.ico"]

date=datetime.date(year,month,day)

os.chdir("/stm/var/archive")
print(os.getcwd())

for i in range(-1,-7):
    dt=datetime.timedelta(i)
    dformat=dt+date
    string1=str(dformat.strftime("%Y%m%d"))
    file_name="fileanme.log-"+string1+".gz"
    print("--------------------------------------------------",file_name,"-----------------------------------------------")
    fo=gzip.open(file_name,'r')
    data=fo.read()
    kcimGetRequest=str(len(re.findall(grep_list[0],data)))
    kcimPostRequest=str(len(re.findall(grep_list[1],data)))
    total_200_req=str(len(re.findall(grep_list[2],data)))
    total_201_req=str(len(re.findall(grep_list[3],data)))
    total_202_req=str(len(re.findall(grep_list[4],data)))
    total_404_req=str(len(re.findall(grep_list[5],data)))
    total_500_req=str(len(re.findall(grep_list[6],data)))
    total_503_req=str(len(re.findall(grep_list[7],data)))
    total_Abort_req=str(len(re.findall(grep_list[8],data)))
    list=[string1,kcimGetRequest,kcimPostRequest,total_200_req,total_201_req,total_202_req,total_404_req,total_500_req,total_Abort_req]
   #print(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],[8])
    fop.write("<tr><td>"+list[0]+"</td><td>"+list[1]+"</td><td>"+list[2]+"</td><td>"+list[3]+"</td><td>"+list[4]+"</td><td>"+list[5]+"</td><td>"+list[6]+"</td><td>"+list[7]+"</td><td>"+list[8]+"</td></tr>")


fop.write("</table></body></html>")
os.chdir("/dir/path")
subprocess.call(['sh','sendmail.sh'])
time.sleep(3)
fop.truncate(0)
