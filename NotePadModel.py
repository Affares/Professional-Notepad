from os import path
import speech_recognition as s
class Model:
    def __init__(self):
        self.key="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.offset=5

    def encrypt(self,plaintext):
        result=""
        for i in plaintext:
            try:
                ind=self.key.index(i)
                ind+=self.offset
                ind=(ind%(len(self.key)))
                result+=self.key[ind]
            except ValueError:
                result+=i
        return result

    def decrypt(self,ciphertext):
        result=""
        for i in ciphertext:
            try:
                ind=self.key.index(i)
                ind-=self.offset
                ind=(ind%len(self.key))
                result+=self.key[ind]
            except ValueError:
                result+=i
        return result

    def save_file(self,msg,url):
        string=""
        if type(url) is not str:
            string=url.name
        else:
            string=url
        fileloc,fileext=path.splitext(string)
        if fileext in ".ntxt":
            msg = self.encrypt(msg)
        with open(string,'w',encoding="utf-8") as obj:
            obj.write(msg)

    def save_as(self,msg,url):
        if type(url) is not str:
            string = url.name
        else:
            string = url
        with open(string, 'w', encoding="utf-8") as obj:
            obj.write(self.encrypt(msg))

    def read_file(self,file):
        fname=path.basename(file)
        filep,fileext=path.splitext(file)
        with open(file, 'r') as fw:
            result = fw.read()
            if fileext in ".ntxt":
                result=self.decrypt(result)
        return result,fname

    def takeQuery(self):
        sr=s.Recognizer() #this will give object of class recognizer
        sr.pause_threshold = 1
        with s.Microphone() as m: #open microphone of the current pc
            #sr.adjust_for_ambient_noise (m)    this function is used to cancel Surrounding Noise(if available)
            audio= sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            return query
