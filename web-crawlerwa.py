import sys,urllib2,time,re
timeout=0
now=0
links=[]
visited_links=[]
max_pages=0
style_tag=re.compile(r'<style[\s\S]+?/style>')
script_tag=re.compile(r'<script[\s\S]+?/script>')
TAG_RE = re.compile(r'<[^>]+>')
def addlinks(html,url):
    global links
    global visited_links
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
    for i in range(len(urls)):
        if ".css" in urls[i] or ".js" in urls[i]:
            continue
        if "http://" in urls[i] or "https://" in urls[i]:
            link=urls[i]
        elif urls[i][0]=="/":
            link=url+urls[i]
        if link not in visited_links:
            links.append(link)
    return
def striptags(html):
    html=script_tag.sub('',html)
    return TAG_RE.sub('',html)
def crawler(url):
    global links
    global visited_links
    content=urllib2.urlopen(url)
    soup=content.read()
    n=url.split("/")
    a=""
    name=a.join(n).split(":")[1]+".txt"
    f=open(name,'w')
    f.write(striptags((str)(soup)))
    f.close()
    addlinks(soup,url)
    visited_links.append(url)
    next_link=links[0]
    links=links[1:]
    if round(time.time()-now)>=timeout:
        print("timeout")
        sys.exit("done")
    if len(visited_links)>=max_pages:
        print ("done")
        sys.exit("done")
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
