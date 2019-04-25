from aip import AipSpeech
APP_ID = '15902738'
API_KEY = 'BDxCS2Buf2KDPjtesZWI7Gfe'
SECRET_KEY = 'Ic4MgB53o9DqMjDreObCt5XdPD9IbOPo'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
lan="猪，别碰我"
result = client.synthesis(lan,'zh',1,{'vol':15,'per':4,'spd':5,'aue':6})
if not isinstance(result,dict):
    with open('C:/Users/kunkun/Desktop/oop.wav','wb') as f:
        f.write(result)
