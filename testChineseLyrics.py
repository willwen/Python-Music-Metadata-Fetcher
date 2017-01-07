import requests
songname = "see you again"
url = u'https://www.googleapis.com/customsearch/v1?key=AIzaSyBxuLKu0t1hdq9mCXHfWWPgrVWYG2IwXQY&cx=012738320297236110223:4rg8w0cdgnq&q=' + songname
#data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'


#response = requests.get(url)


#print(response.json())


#link = response.json()["items"][0]["link"]

link = "https://mojim.com/jpy105708x1x10.htm"
webpage = requests.get(link)
print(webpage.text);


from bs4 import BeautifulSoup

##parsed_html = BeautifulSoup(webpage.text)
##temp = parsed_html.body.find_all(id='fsZx3')
###print temp.replace("<br/>","\n")
##for wrapper in temp:
##   print wrapper.replace("<br/>","\n")
##   print "\n"



#<dt id='fsZx2' class='fsZx2' > See You Again</dt><dd id='fsZx3' class='fsZx3'>
