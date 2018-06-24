# coding=utf-8
from aip import AipOcr
import configparser

class BaiDuApi:
    def __init__(self,filePath):
        target=configparser.ConfigParser()
        target.read(filePath)
        app_id=target.get('config','APP_ID')
        api_key=target.get('config','API_KEY')
        secret_key=target.get('config','secret_KEY')
        self.client=AipOcr(app_id,api_key,secret_key)

    def pictureTotext(self,filePath):
        image = BaiDuApi.getFileContent(filePath)
        texts=self.client.basicGeneral(image)
        allTexts=''
        for words in texts['words_result']:
            allTexts = allTexts + ''.join(words.get('words',''))
        
        return allTexts

    @staticmethod
    def getFileContent(filePath):
        with open(filePath,'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    baiduapi = BaiDuApi(r'setup.ini')
    text=baiduapi.pictureTotext(r'imageGrabe.png')
    print text
