from sys import stdout
from botRequests import sendMessage
import subprocess
import os
from modularfunctions.cd_evaluator_function import cdEvaluator

def runTerminal(command, password):
    if password is None:
        sendMessage("To run any command first input a sudo password with\n<pre>/password YourPassword</pre>")
        return
    bashCommand = ' '.join(command) + "\n"
    if command[0] == 'sudo':
        if command[1] == 'cd':
            if len(command) == 2:
                cdCommand = cdEvaluator("/home")
            else:
                cdCommand = cdEvaluator(command[2])
            if cdCommand is not True:
                sendMessage(cdCommand)
            runTerminal(['ls'], password)
            return True
        else:
            sudoBashCommand = f"echo {password} |" + bashCommand
            process = subprocess.Popen(sudoBashCommand,     
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE, 
                                        shell = True)
    else:
        if command[0] == 'cd':
            if len(command) == 1:
                cdCommand = cdEvaluator("/home")
            else:
                cdCommand = cdEvaluator(command[1])
            if cdCommand is not True:
                sendMessage(cdCommand)
            runTerminal(['ls'], password)
            return True
        else:
            process = subprocess.Popen(bashCommand, 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE,
                                    shell = True)
    (output, error) = process.communicate()
    responseMessage = output if output else error
    responseMessage = responseMessage.decode()
    inputtedCommand = f"$ {bashCommand}"
    print(type(responseMessage))
    responseMessage = inputtedCommand + codifyText(responseMessage) if responseMessage is not None else responseMessage

    sendMessage(responseMessage)
    return False if len(error) else True

def codifyText(message):
    formattedMessage = "<code>" + message + "</code>"
    return formattedMessage