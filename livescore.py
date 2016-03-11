#! /bin/python
import urllib,urllib2
url="http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
page=urllib2.urlopen(url)
data=page.read()
match=data.split('<match')
batstart=match[2].split('<btTm')
batinn=batstart[1].split('</btTm>')
inn=batinn[0].split("/>")
sname=inn[0].split("sName=\"")[1]
sname=sname.split("\"")[0]
    #print(sname)
desc=inn[0].split("desc=\"")[1]
desc=desc.split("\"")[0]
#print(desc)
r=inn[0].split("r=\"")[1]
r=r.split("\"")[0]
    #print(r)
ovrs=inn[0].split("ovrs=\"")[1]
ovrs=ovrs.split("\"")[0]
    #print(ovrs)
wkts=inn[0].split("wkts=\"")[1]
wkts=wkts.split("\"")[0]
    #print(wkts)
write="Team:"+sname+"\n"+"Score:"+r+"/"+wkts+"\tOvers:"+ovrs
    #print(write)
print(write)
