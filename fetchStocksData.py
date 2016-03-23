# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:49:20 2016

@author: shakuler
"""
import urllib2, csv, cookielib

sitePT = 'http://xueqiu.com/S/{SYMBOL}/historical.csv'
#site = "http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol=JPASSOCIAT&amp;fromDate=1-JAN-2012&amp;toDate=1-AUG-2012&amp;datePeriod=unselected&amp;hiddDwnld=true"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#req = urllib2.Request(site, headers=hdr)
symbolTest = 'APPL'
Exchange = 'NASDAQ'

try:
    with open(Exchange + '.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print u'读取', row['Symbol'], row['Name‘], u‘数据.’
            symbol = row['Symbol'].strip()
            
            if '^' not in symbol:
                site = sitePT.format("")
            
            