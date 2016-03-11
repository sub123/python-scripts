#use http://thetvdb.com/api/GetSeries.php?seriesname=doctor%20who to get series id
import urllib2,datetime
import MySQLdb as mdb
id_with_show={'78901':'Supernatural','274431':'Gotham','290853':'Fear the Walking Dead','78901':'Supernatural','153021':'The Walking Dead','78650':'The Flash','76107':'Doctor Who'}
show_id={'78901','274431','290853','153021','78650','76107','78901'}
def schedule():
    for i in range(0,10):
        date=(str)(datetime.date.today() + datetime.timedelta(days=i))
        print date
        i=i+1
        for shid in show_id:
            url="http://www.thetvdb.com/api/GetEpisodeByAirDate.php?apikey=7C745E1A562DDA57&seriesid="+shid+"&airdate="+date
            a=urllib2.urlopen(url)
            content=a.read()
            if '<Error>' in content:
                continue
            data=id_with_show[shid]+":"
            season=content.split('<Combined_season>')[1]
            season=season.split('</Combined_season>')[0]
            data=data+" Season-"+season
            episode=content.split('<EpisodeNumber>')[1]
            episode=episode.split('</EpisodeNumber>')[0]
            data=data+" Episode-"+episode
            episode_name=content.split('<EpisodeName>')[1]
            episode_name=episode_name.split('</EpisodeName>')[0]
            data=data+":"+episode_name
            #print data
            date=(str)(datetime.date.today() + datetime.timedelta(days=i))
            sql="INSERT INTO dchub_tvschedule VALUES ('"+data+"','"+date+"')"
            #print sql
            cur.execute(sql)
            db.commit()
try:
    db=mdb.connect(host="localhost", user="root", passwd="icui4cu", db="verlihub")
    cur=db.cursor()
    cur.execute("TRUNCATE table dchub_tvschedule")
    schedule()
except:
    print("Could not connect to db or check url")
