import requests
from ids import tokenId, userId

telegramPath = "https://api.telegram.org/bot"
token = tokenId
urlPath = telegramPath + token

def sendMessage(responseMessage):
    sendMessagePath = urlPath + '/sendMessage'
    data = {'chat_id': userId, 'text': responseMessage, "parse_mode":'HTML'}
    request = requests.post(sendMessagePath, data=data)
    return

def deleteMessage(messageId):
    deleteMessagePath = urlPath + '/deleteMessage'
    data = {"chat_id": userId, "message_id":messageId}
    request = requests.post(deleteMessagePath, data)
    return     
