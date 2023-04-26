import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep
import  random
class Network:
    def __init__(self,collection = "AM_FAC2"):
        cred = credentials.Certificate('serviceKey.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection(collection)
        self.docParameter = self.collection.document('command')
        self.docStatus = self.collection.document('status')
        self.docMonitor = self.collection.document('monitor')
        self.docEmitted = self.collection.document('emitted')

    def changeChamber(self,chamber):
        self.collection = self.db.collection(chamber)
        self.docParameter = self.collection.document('command')
        self.docStatus = self.collection.document('status')
        self.docMonitor = self.collection.document('monitor')
        self.docEmitted = self.collection.document('emitted')
        self.docError = self.collection.document('Error')

    def sendCommand(self,dic):
        dic["random"] = random.randint(0, 999999)
        self.docParameter.set(dic)

    def checkEmittingSignal(self,aDict=None):
        for i in range(30):
            sleep(2)
            try:
                s = self.docStatus.get().to_dict()['status']
                dic_emitted = self.docEmitted.get().to_dict()
                if not aDict:
                    aDict = self.docParameter.get().to_dict()
                if s == "Sent:" and (dic_emitted == aDict):
                    self.docStatus.set({'status': 'Recived'})
                    self.docError.set({'Information': 'No ERROR'})
                    print("DUT Start Emittion")
                    return True
            except:
                print("Wait")
        self.writeError("DUT Not Reply")
        return False

    def writeError(self,infor):
        self.docError.set({'Information': infor})

    def markComplete(self):
        self.docMonitor.set({'auto': 'Complete'})

    def markIncomplete(self):
        self.docMonitor.set({'auto': 'In Progress'})