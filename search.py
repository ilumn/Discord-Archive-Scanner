import fast_json
import time
import threading
import logging
from colorama import *
from operator import contains
import re
with open('archive.json', encoding='utf-8') as json_file:
    data = fast_json.load(json_file)
messages = data["messages"]  
newString = []
from list import strings
for string in strings:
    newString.append(string.lower())
def ThreadFunction(string):
    print(Fore.LIGHTBLUE_EX)
    print(string)
    print(Style.RESET_ALL)
    timesSaid=0
    for x in range(0,len(messages)):
        authorOfMessage = messages[x]["author"]["name"]
        contentOfMessage = messages[x]["content"]
        containsSearch = re.search(string.lower(),contentOfMessage.lower())
        if containsSearch== None:
            continue
        msg = "Message "+str(x)+" from "+authorOfMessage+": "+contentOfMessage+"\n"
        print(Fore.LIGHTGREEN_EX)
        print(msg)
        print(Style.RESET_ALL)
        filename = string+".txt"
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(msg)
        timesSaid+=1
    filename2 = string+"_Count"+".txt"
    with open(filename2, 'w') as f:
        f.write("\n"+"\n"+"The Server has mentioned "+string+" "+str(timesSaid)+" times")
        
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = []
    for string in newString:
        string = str(string)
        print(Fore.YELLOW)
        logging.info("|  Main  |: create and start thread "+string+".")
        print(Style.RESET_ALL)
        x = threading.Thread(target=ThreadFunction, args=(string, ), daemon=True).start()
        threads.append(x)
        
    for string, Thread in enumerate(threads):
        name = str(string)
        print(Fore.YELLOW)
        logging.info("|  Main  |: before joining thread "+string+".")
        Thread.join()
        print(Style.RESET_ALL)
        print(Fore.YELLOW)
        logging.info("|  Main  |: thread for "+string+" done")
        print(Style.RESET_ALL)
