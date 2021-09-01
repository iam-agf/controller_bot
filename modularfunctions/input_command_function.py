from botRequests import deleteMessage, sendMessage
from commandRunner import runTerminal

def inputCommandFunction(message, password):
    messageContent = message.text
    messageId = message.message_id

    command = messageContent.split()
    returnOutput = runTerminal(command, password)
    print(returnOutput)
    if returnOutput:
        deleteMessage(messageId)
    return
