'''
Created on Jul 17, 2014
A script to text function of DCI_SCORES_BOT on reddit.com/r/drumcorps
@author: Liam Sargent
'''


from DCI_SCORES_BOT import ListHandler
from DCI_SCORES_BOT import ScoreUtils
from DCI_SCORES_BOT import SiteScraper
import time

print "DCI_SCORES_BOT by u/drum_code"

lh = ListHandler.ListHandler('dciscoreslist.txt')
sp = SiteScraper.SiteScraper(lh)
reddituname = raw_input('Enter reddit username: ')
redditpword = raw_input('Enter reddit password: ')

while True:
    newshows = sp.scrape()
    if len(newshows) > 0:
        print "Found " + str(len(newshows)) + " new shows in most recent query."
        for show in newshows:
            print "Creating post for " + show + "\n"
            sh = ScoreUtils.ScorePuller(show)
            scorepost = ScoreUtils.ScorePoster( reddituname, redditpword, 'drumcorps', sh, lh)
            scorepost.populatepost()
            scorepost.post()
            time.sleep(3)
    time.sleep(60)
    
        