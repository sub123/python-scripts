import urllib,urllib2
url="http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
try :
        page=urllib2.urlopen(url)
        data=page.read()
        # print(data)
        matches=data.split("</match>")
        serial=1
        length=len(matches)
        print("<================Cricket=================>\n")
        i=0
        while serial<length:
                series=""
                mdesc=""
                mnum=""
                vcity=""
                vcountry=""
                grnd=""
                # type of match
                t1=matches[i].split("type=\"")
                typ=t1[1].split("\"")[0]
                #print(typ)
                # series
                if('srs' in matches[i]):
                    s1=matches[i].split("srs=\"")
                    series=s1[1].split("\"")[0]
                    #print(series)
                    # match desc
                if('mchDesc' in matches[i]):
                    m1=matches[i].split("mchDesc=\"")
                    mdesc=m1[1].split("\"")[0]
                    #print(mdesc)
                    # match number
                if('mnum' in matches[i]):
                    m1=matches[i].split("mnum=\"")
                    mnum=m1[1].split("\"")[0]
                   #print(mnum)
                if('vcity' in matches[i]):
                    v1=matches[i].split("vcity=\"")
                    vcity=v1[1].split("\"")[0]
                         #print(vcity)
                if('vcountry' in matches[i]):
                    v1=matches[i].split("vcountry=\"")
                    vcountry=v1[1].split("\"")[0]
                        #print(vcountry)
                if('grnd' in matches[i]):
                    g1=matches[i].split("grnd=\"")
                    grnd=g1[1].split("\"")[0]
                        #print(grnd)
                    #date
                if('Tme Dt' in matches[i]):
                    m1=matches[i].split("Tme Dt=\"")
                    dt=m1[1].split("\"")[0]
                line1=(str)(serial)+" "+dt+"\n"
                line2=series+"\n"
                line3=mdesc+" "+mnum+"\n"
                line4=grnd+"\n"
                line5=vcity+" "+vcountry+"\n"
                i=i+1
                serial=serial+1
                print(line1)
                print(line2)
                print(lin3)
                print(line4)
                print(line5)
                print("<==========================================>\n")
except:
        print("Lost Network Connection")
