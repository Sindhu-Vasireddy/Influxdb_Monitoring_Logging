#!/usr/bin/python
import sys
from subprocess import Popen,PIPE
from influxdb import InfluxDBClient
import time

host='localhost'
user='ats'
password='atslabb00'
DBNAME='A3'
port=8086


client = InfluxDBClient(host, port, user, password, DBNAME) 
client.create_database(DBNAME)

del sys.argv[0]
#sys.argv.insert(0,'python')
sys.argv.insert(0,'/tmp/A2/prober')
print (sys.argv)
series=[]


proc=Popen(sys.argv,stdout=PIPE)
for line in iter(proc.stdout.readline,''):
#    print line
    l=line.rstrip()
    rate_list=l.split("|")
#    print "rate_list:{}".format(rate_list)
    for string in sys.argv[4:]:
        series=[]
        i=sys.argv.index(string)
        pointValues = {"measurement":"rate","tags":{'oid':string,},"fields":{'value':rate_list[i-4],'timevalue':float(rate_list[0]),}}
        series.append(pointValues)
        client.write_points(series)
     