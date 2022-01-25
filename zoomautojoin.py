import logging
from sys import platform
from tabnanny import verbose

Windows = False
if platform == "win32" or platform == "cygwin":
    Windows = True

logging.basicConfig(filename="log.txt", level=logging.INFO,format="%(asctime)s %(message)s")
def Print(toPrint):
    logging.info("{}".format(toPrint))
    print(toPrint)
from time import sleep, strftime
import os,sys

if Windows:
    try:
        import subprocess
    except:
        Print("Subprocess module cannot be imported. Did you install the dependancy ??")
        quit(0)

timeIndex = []
linkIndex = []
descIndex = []


def parseFile():
    timeIndex.clear()
    linkIndex.clear()
    source = open("meetings.txt",'r')
    meetingLines = source.readlines()
    indexcounter = 0
    for line in meetingLines:
        a = line.split(" ",2)
        timeIndex.append("placeholder")
        linkIndex.append("placeholder")
        descIndex.append("placeholder") 
        timeIndex[indexcounter] = a[0]
        linkIndex[indexcounter] = a[1]
        if (len(a) ==3):
            if a[2].strip() == "" or a[2].strip() == " ":
                descIndex[indexcounter] = "No description provided"
            else:
                descIndex[indexcounter] = a[2]
        else:
            print(len(a))
            descIndex[indexcounter] = "No description provided"
        indexcounter+= 1
    source.close()
verboseFlag = False
def main():
    print("Rest easy... this will open zoom when the time comes UwU")
    try:
        if sys.argv[1] == "-verbose" or sys.argv[1] == "--v":
            print("Verbose argument found")
            verboseFlag = True  
    except:
        print("No launch args")
        verboseFlag = False
    while True:
        currenttime = strftime("%H:%M")
        for time in timeIndex:
            if verboseFlag == True:
                print("Currenttime = {} and comparing to {}".format(currenttime,time))
            if currenttime == time:
                index = timeIndex.index(time)
                # using zoombie logic to open zoom without browser thanks to https://github.com/DaBigBlob/zoombie
                link = linkIndex[index]
                domain = link.split('/')[3]
                mID = link.split('/')[-1].split('?')[0]
                pswd = link.split('/')[-1].split('=')[1]

                os.system(f'start zoommtg://{domain}/join?action=join"&"confno={mID}"&"pwd={pswd} /HIGH >NUL  2>NUL')    
                Print(f"JOINING MEETING: {linkIndex[index]} - DESC: {descIndex[index]}")
                Print("Sleeping for 60 seconds to avoid accidental meeting join")
                sleep(60)
                parseFile()
        sleep(5)
        parseFile()
parseFile()
main()
