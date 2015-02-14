#visoscript
# -*- coding: utf-8 -*-
import mechanize
from mechanize._opener import urlopen
from mechanize._form import ParseResponse
from bs4 import BeautifulSoup
import time
import sched

#VIRKAR
def logIn(brow,name):
	#visoscript

	''' Connect to the website and login to the form
	'''
	brow = mechanize.Browser()
	brow.open('https://www.nord.is/innskra/')
	brow.select_form(nr = 0)

	brow.form['username'] = name[0]
	brow.form['password'] = name[1]

	brow.submit()

	#RETURN the open browser that is loggedin
	return brow

#VIRKAR
def getTheVisos():


	''' Scrape the next visos that is about to happen today
	'''
	browser = mechanize.Browser()
	browser.open('https://www.nord.is/atburdir/')

	html = browser.response()
	parsed_html = BeautifulSoup(html)

	'''
	search for everything that is with some class
	passed events is the events that are over

	TODO:check what the class of the not-passed events are
	TODO:only return the visos that are happening today
	'''

	templist = [] #Fylkið sem heldur utan um alla viðburði sem eiga eftir að gerast
	for link in parsed_html.find_all('div','upcoming-event'):
		print((link.a.get('href').encode('utf-8')))
		#print(link.div.string.encode('utf-8')) skoða hvort þurfi að adda bæði dagsetningu inn í fylkið
		templist.append((link.a.get('href').encode('utf-8')))

	#return the vísós that are gonna happen
	return templist

#VIRKAR EKKI
#ÞETTA FER Í  GANG KLUKKAN 13:10
def getTheFuckersToViso(sc):

	#CALL THE FUNCTION NEXT AFTER 24  HOURS
	sc.enter(24*60*60, 1, getTheFuckersToViso, (sc,))

	#TODO FIX THIS FOR ADDING OTHER PEOPLE
	gummi = ['username', 'password']
	]

	#Assign it to none
	brow1 = mechanize.Browser()


	#Get the visos that are happening later today
	visos = getTheVisos()

	#TODO PUT A VARIABLE HERE IF THE DUDES DONT WANT TO GO TO VISO

	brow1 = logIn(brow1,gummi)


	#check if there is a viso today
	if(visos[0] != 0):
		#biddu núna þangað til að klukkan er orðin  þú veist 2 min í skráningu
		#og byrjaðu að spamma
		bla = True
		bla2= True
		counter = 0
		while(bla):
			time.sleep(10)  # Delay for 10 minute (60*10 seconds)
			bla = False

		for viso in visos:
			visoName ='https://www.nord.is'+ viso +'skraning'
			brow1.open(visoName)

			print("ja")

		



#KÖLLUM Á GETTHEFUCKERSTOVISO þegar klukkan er orðin eitthvað víst 13:10 á hverjum þriðjudegi r sum
#NOTA ÞETTA EÐA CRONJOB
s = sched.scheduler(time.time, time.sleep)
s.enter(24*60*60, 1,getTheFuckersToViso, (s,))
s.run()
