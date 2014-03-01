__author__ = 'anandh'

print "Helo world"

from alchemyapi import AlchemyAPI

from bs4 import BeautifulSoup

import urllib2


#ProductPage=urllib2.urlopen('http://www.flipkart.com/moto-g/p/itmdsmbxcrm9wy8r?pid=MOBDSGU2QFWMHGRR&otracker=ts_mg_8gb')
ProductPage=urllib2.urlopen('http://www.flipkart.com/moto-g/p/itmdsmbxcrm9wy8r?pid=MOBDSGU2ZMDYENQA')
ProductData=BeautifulSoup(ProductPage.read())

ReviewCount=ProductData.find("span",{'itemprop':'reviewCount'}).get_text()
print ReviewCount

RatingUserCount=ProductData.find("span",{'itemprop':'ratingCount'}).get_text()
print RatingUserCount

Rating=ProductData.find("div",{'class':'pp-big-star'}).get_text()
print Rating


'''
pageNum=0
while int(pageNum) < int(ReviewCount)/10:
    ReviewPage=urllib2.urlopen('http://www.flipkart.com/google-nexus-5/product-reviews/ITMDQ9VXQ6NSWAFG?pid=MOBDQ9VXZMHXZGBP&start='+str(pageNum))
    #ReviewPage=urllib2.urlopen('http://www.flipkart.com/moto-g/product-reviews/ITMDSMBXCRM9WY8R?pid=MOBDSGU2ZMDYENQA&start='+pageNum)
    ReviewData= BeautifulSoup(ReviewPage.read())


    for review in ReviewData.findAll("p",{'class':'line bmargin10'}):
        print review.get_text()
        print "--------------------------------------------------------------------"

    for reviewHead in ReviewData.findAll("div",{'class':'line fk-font-normal bmargin5 dark-gray'}):
        print reviewHead.get_text()
        print "--------------------------------------------------------------------"
    pageNum=pageNum+10



alch=AlchemyAPI()

resp=alch.category("text","Nexus 5")

print resp


#print "Sentiment: ", resp["docSentiment"]["type"]
'''


url=raw_input()

