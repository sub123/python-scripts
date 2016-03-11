import sys,urllib2,time,BeautifulSoup,re
timeout=0
now=0
links=[]
visited_links=[]
max_pages=0
script_tag=re.compile(r'<script[\s\S]+?/script>')
TAG_RE = re.compile(r'<[^>]+>')
def striptags(html):
    html=script_tag.sub('',html)
    return TAG_RE.sub('',html)
def crawler(url):
    global links
    global visited_links
    content=urllib2.urlopen(url)
    print "url open"
    soup=BeautifulSoup.BeautifulSoup(content)
    n=url.split("/")
    a=""
    name=a.join(n).split(":")[1]
    f=open(name,'w')
    f.write(striptags((str)(soup)))
    f.close()
    print "parsed"
    atags=[tag.attrs for tag in soup.findAll('a')]
    for tag in atags:
        for i in range(len(tag)):
            if tag[i][0]=="href":
                if "#" in tag[i][1]:
                    continue
                if "https://" in tag[i][1] or "http://" in tag[i][1]:
                    link=tag[i][1]
                else:
                    link=url+tag[i][1]
                if link in visited_links:
                    continue
                links.append(link)
    visited_links.append(url)
    next_link=links[0]
    links=links[1:]
    if round(time.time()-now)>=timeout:
        sys.exit("exit")
    if len(visited_links)>=max_pages:
        sys.exit("exit")
    else:
        crawler(next_link)
def main():
    global now
    global max_pages
    global timeout
    url=raw_input("Enter Url to be crawled:")
    max_pages=input("Enter max number of pages to be crawled:")
    timeout=input("Enter timeout preiod:")
    now=time.time()
    crawler(url)
main()
