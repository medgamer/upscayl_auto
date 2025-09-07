# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
from html.parser import HTMLParser

def find_tags(html):
    pattern = r"<([^>]*)>"
    matches = re.findall(pattern, html)

    tags = []
    for t in matches:
        tags.append("<"+t+">")

    return tags

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0],">",attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_data(self, data):
        pass
        # print("-> data  :", data)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0],">",attr[1])


n = int(input())

parser = MyHTMLParser()

for i in range(n):
    parser.feed(input())
    """
    tags = find_tags(input())
    for t in tags:
        parser.feed(t)
    """
