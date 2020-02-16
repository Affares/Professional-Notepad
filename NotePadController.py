import NotePadModel
class Controller:
    def __init__(self):
        self.notepadModel=NotePadModel.Model()
    def save_file (self,msg,url):
        self.notepadModel.save_file(msg,url)
    def save_as (self,msg1,url):
        self.notepadModel.save_as(msg1,url)
    def read_file(self,url):
        self.msg,self.base=self.notepadModel.read_file(url)
        return self.msg,self.base
    def saySomething(self):
        self.takeAudio = self.notepadModel.takeQuery()
        return self.takeAudio