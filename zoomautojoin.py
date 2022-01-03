import webbrowser
from time import gmtime, sleep, strftime
import os,sys
timeIndex = []
linkIndex = []
def parseFile():
    timeIndex.clear()
    linkIndex.clear()
    source = open("meetings.txt",'r')
    meetingLines = source.readlines()
    indexcounter = 0
    for line in meetingLines:
        a= line.split(" ")
        length = len(a)
        timeIndex.append("totally optimized code")
        linkIndex.append("python omegacringe... ")
        timeIndex[indexcounter] = a[0]
        linkIndex[indexcounter] = a[1]
        # timeIndex.append(first_half[0])
        # meetingLines.append(second_half[0])
        indexcounter+= 1
      
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
                print("currenttime = {} and comparing to {}".format(currenttime,time))
            if currenttime == time:
                index = timeIndex.index(time)
                # webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(linkIndex[index],new=0) 
                # webbrowser.open(linkIndex[index],new=0) subsitute this if u dont have chrome
                # using zoombie logic to open zoom without browser thanks to https://github.com/DaBigBlob/zoombie
                link = linkIndex[index]
                domain = link.split('/')[3]
                mID = link.split('/')[-1].split('?')[0]
                pswd = link.split('/')[-1].split('=')[1]
                os.system(f'start zoommtg://{domain}/join?action=join"&"confno={mID}"&"pwd={pswd} /HIGH')
                
                print("JOINING MEETING")
                print("sleeping for 1 minute to avoid ACCIDENTAL meeting join")
                sleep(60)
                parseFile()
        sleep(5)
        parseFile()
parseFile()
main()
