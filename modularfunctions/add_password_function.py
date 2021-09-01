from botRequests import deleteMessage, sendMessage

def addPasswordFunction(message):
    messageContent = message.text
    messageId = message.message_id
    password = messageContent.split()[1]
    sendMessage("Password saved.\nTo update this password change it running <pre>/password newPassword</pre>\nRemember this password is temporal so needs to be input each time the computer is on.")
    deleteMessage(messageId)
    return password