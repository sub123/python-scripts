import sys,urllib,urllib2,time,re,os
timeout=0
now=0
links=[]
visited_links=[]
max_pages=0
path=""
def crawler(url):
    global links
    global visited_links
    global path
    if round(time.time()-now)>=timeout:
        print("timeout")
        sys.exit("done")
    content=urllib.urlopen(url)
    if content.getcode()==200:
        left=round((now+timeout)-(time.time()))
        content=urllib2.urlopen(url,timeout=left)
        soup=content.read()
        n=url.split("/")
        a=""
        name=path+"/"+a.join(n).split(":")[1]+".txt"
        f=open(name,'a')
        html=soup
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        link=""
        for i in range(len(urls)):
            if ".css" in urls[i] or ".js" in urls[i]:
                continue
            if "#" in urls[i] or "javascript(void)" in urls[i]:
                continue
            if "http://" in urls[i] or "https://" in urls[i]:
                link=urls[i]
            else:
                link=url+urls[i]
            if link not in visited_links:
                links.append(link)
                f.write(link+"\n")
        visited_links.append(url)
    next_link=links[0]
    links=links[1:]
    if round(time.time()-now)>=timeout:
        print("timeout")
        sys.exit("done")
    if len(visited_links)>=(max_pages+1):
        print ("done")
        sys.exit("done")
    else:
        print "crawling:"+next_link
        crawler(next_link)
def main():
    global now
    global max_pages
    global timeout
    global path
    url=raw_input("Enter Url to be crawled:")
    max_pages=input("Enter max number of pages to be crawled:")
    timeout=input("Enter timeout period:")
    now=time.time()
    n=url.split("/")
    a=""
    path=a.join(n).split(":")[1]
    if not os.path.exists(path):
        os.makedirs(path)
    crawler(url)
main()
