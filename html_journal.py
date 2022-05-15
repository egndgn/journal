from html.parser import HTMLParser
import urllib.request

csv_yaz = open("journal_csv.csv", "w", encoding='utf-8')

url = urllib.request.urlopen("https://dblp.org/db/journals/publ/el.html")
html = url.read().decode()
url.close()

class Parse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           for name,link in attrs:
               if name == "href" and link.startswith("https://dblp.org/db/journals/"):
                   print (link)
                   journal_name = link[29:-11]
                   print(journal_name)
                   csv_yaz.write(link+", "+journal_name+"\n")

p = Parse()
p.feed(html)

print()

url = urllib.request.urlopen("https://dblp.org/db/journals/publ/sp.html")
html = url.read().decode()
url.close()

class Parse(HTMLParser):
    def __init__(self):
        super().__init__()
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           for name,link in attrs:
               if name == "href" and link.startswith("https://dblp.org/db/journals/"):
                   print (link)
                   journal_name = link[29:-11]
                   print(journal_name)
                   csv_yaz.write(link+", "+journal_name+"\n")

p = Parse()
p.feed(html)

url = urllib.request.urlopen("https://dblp.org/db/journals/publ/wi.html")
html = url.read().decode()
url.close()

class Parse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           for name,link in attrs:
               if name == "href" and link.startswith("https://dblp.org/db/journals/"):
                   print (link)
                   journal_name = link[29:-11]
                   print(journal_name)
                   csv_yaz.write(link+", "+journal_name+"\n")

p = Parse()
p.feed(html)

url = urllib.request.urlopen("https://dblp.org/db/journals/publ/ieee.html")
html = url.read().decode()
url.close()

class Parse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
    def handle_starttag(self, tag, attrs):
        if tag == "a":
           for name,link in attrs:
               if name == "href" and link.startswith("https://dblp.org/db/journals/"):
                   print (link)
                   journal_name = link[29:-11]
                   print(journal_name)
                   csv_yaz.write(link+", "+journal_name+"\n")

p = Parse()
p.feed(html)