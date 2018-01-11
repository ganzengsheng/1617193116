import urllib
import urllib2
import re
import thread
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'
pageStories = []
url = 'http://www.51jrjob.com/jobseeker/stage/findjob.html?kv=&cv=&acv=&fl=&it=&le=&page=2'
headers = {'User-Agent':user_agent}
result = urllib2.Request( url, headers=headers )
response = urllib2.urlopen( result )
pageCode = response.read().decode('utf-8')
pattern = re.compile(r'<a class="pos-detail".*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<span class="spansalary">(.*?)</span>',re.S )
items = re.findall( pattern, pageCode )
for i in items:
    for g in i:
        print g
