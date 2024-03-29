#v 5


from SecApp.IOClass import AppIO

'''
====================================================================================
Loading index page:
'''
def checkexist():
	from SecApp.IntegrityClass import Integrity
	checkInt = Integrity()
	output = str(checkInt.checkExists())
	AppIO(output)

'''
====================================================================================
Password page:
'''
def checkdatabasepassword(passkey):
	from SecApp.DBBaseClass import DBIndexSystem
	output = str(DBIndexSystem(passkey).sanitycheck)
	AppIO(output)
'''
====================================================================================
Wizard page:
'''

def createnewdatabase(passkey,dbname):

	from SecApp.DBBaseClass import DBSubsystem
	initdb = DBSubsystem(passkey,dbname).createDB()

	pre_note = {'note':{'active':'True','typ':'note','range':'0-100','aggregate':'False', 'multipoint':'False'}}
	from SecApp.DBQuestionClass import SecuQ
	initQ = SecuQ(passkey)
	initQ.questionInsert(str(pre_note),descriptor='inclusive')

'''
====================================================================================
Answers page:
'''


def loadresponsequestions(passkey): # output

	from SecApp.DBQuestionClass import SecuQ
	initQ = SecuQ(passkey)
	output = initQ.valid
	AppIO(output)
	return True
	
def loadtodayresponses(passkey):
	from SecApp.DBOutputClass import SecuFrame
	initDO = SecuFrame(passkey,'today')
	output = initDO.iffo().dayresponse().responseFrame
	AppIO(output)



def saveresponsedata(passkey,data): # input

	from SecApp.DBInputClass import SecuIn
	initDI = SecuIn(passkey)
	output = initDI.questionDataIN(str(data))
	AppIO(str(output)) #output is boolean
	return True




'''
====================================================================================
Questions page:
'''





def loadquestions(passkey):

	from SecApp.DBQuestionClass import SecuQ
	initQ = SecuQ(passkey)
	output = initQ.all
	AppIO(output)
	return True

def savequestions(passkey,json):

	from SecApp.DBQuestionClass import SecuQ
	initQ = SecuQ(passkey)
	output = initQ.questionInsert(json,descriptor='exclusive')
	AppIO(output)
	return True

'''
====================================================================================
Graph page:
'''
def graphall(passkey):
	from SecApp.DBOutputClass import SecuFrame
	initDO = SecuFrame(passkey)
	output = initDO.iffo().igraph().graphFrame
	AppIO(output)
def getreferencequestions(passkey):
	from SecApp.DBQuestionClass import SecuQ
	initQ = SecuQ(passkey)
	output = initQ.valid
	AppIO(output)
	return True

def graphanalysis(passkey):

	from SecNeural.NeuroNetAnalysis import NeuroBasicAlgo
	algoConfig ={"algo_id" : "hx0" , "algoName":"Basic", "algoMode":"Basic", "independantVars":["a","d","c"]  , "dependantVars":["b"]}
	initNeuro = NeuroBasicAlgo(passkey,algoConfig)
	output = initNeuro.GraphOutput
	AppIO(output)

'''
====================================================================================
Cloud page:
'''

# index: check location
def checkcloudlocation():
	print " ------------------------------ 1111111 got cloud selection"
	from SecApp.SyncClass import Sync
	initsync = Sync()
	print " ------------------------------ 22222222 got cloud selection"
	initsync.getcloudselection()
	print " ------------------------------ 3333333 got cloud selection"
	output = initsync.backup # variable that holds backup location
	print " ------------------------------ 4444444 got cloud selection " + str(output)
	AppIO(str(output))


def authenticate(jsonconfig):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	status = initsync.parseconfigjson(str(jsonconfig))
	AppIO(str(status))

def authorize(jsonconfig):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	status = initsync.parseconfigjson(str(jsonconfig))
	AppIO(str(status))


# Get cloud credentials if they exist
def getcloudcreds(page):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	output = initsync.getconfig(page) #returns json of available credentials ofr given page location
	AppIO(str(output))

def sync(jsonconfig):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	status = initsync.parseconfigjson(str(jsonconfig))
	AppIO(status)


def savecreds(jsonconfig):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	status = initsync.parseconfigjson(str(jsonconfig)) #automatically detects from config
	AppIO(status)


def syncimportdb(jsonconfig):
	from SecApp.SyncClass import Sync
	initsync = Sync()
	status = initsync.parseconfigjson(str(jsonconfig)) #automatically detects from config
	AppIO(status)