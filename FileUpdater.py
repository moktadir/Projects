###USE WITH CAUTION. THIS PROGRAM IS DESIGNED FOR AUTOMATION, THEREFORE###
###THIS PROGRAM MAY REPLACE(DESTROY) ANY SPECIFIED FILES.###
###USE AT YOUR OWN RISK. YOU HAVE BEEN WARNED.###

#Activate program through command-line or shortcut, it
#Requires two args: 1st file(path), 2nd file(path), forward-slash('/') format


#Walkthrough: To set up a shortcut(Windows):
#1. Create a shortcut to this file.
#2. Open the shortcut file's properties.
#3. Where it says 'Target', add your two filename/path arguments
#   in the format "X:/exampleDir/example.txt" or simply "example.txt" if
#   located in the same directory.
#Note: Target location uses '\' format, whereas your arguments should use '/'


import os.path, time, sys, shutil


def replMonth(name): #Change month label to number format
    return{'Jan': 1,   'Feb': 2,  'Mar': 3,  'Apr': 4,
           'May': 5,   'Jun': 6,  'Jul': 7,  'Aug': 8,
           'Sep': 9,    'Oct': 10,  'Nov': 11,  'Dec': 12
           }[name]


def touchUp(List): #Reformat file modify timestamp
    newList = []
    newList.append(List[3])
    newList.append(str(replMonth(List[0])))
    newList.append(List[1])
    [newList.append(i) for i in List[2].split(':')]
    for i in range(6):
        newList[i] = int(newList[i])
    return newList


def updater(file1,file2): #Portable function: Compare timestamps, replace
    time1 = time.ctime(os.path.getmtime(file1)).split(' ')[1:] #First file
    
    for i in range(len(time1)-1):
        if time1[i] == '':
            time1.pop(i)
    time1 = touchUp(time1)

    try:
        time2 = time.ctime(os.path.getmtime(file2)).split(' ')[1:] #Second file
    except:
        shutil.copy(file1, file2)
        input("Looks like something's wrong with the second file(path). ",
              "We'll just create a copy there, just in case.\n")
        return
    
    for i in range(len(time2)-1):
        if time2[i] == '':
            time2.pop(i)
    time2 = touchUp(time2)
    
    for i in range(6):
        if time1[i] == time2[i]:
            continue
        elif time1[i] > time2[i]:
            shutil.copy(file1, file2)
            print("Replaced second file.\n")
            return
        elif time1[i] < time2[i]:
            shutil.copy(file2, file1)
            print("Replaced first file.\n")
            return
        
    print("Files are identical!\n")
    return


def main(argv): #Call for two comm-line args, 1st file(path), 2nd file(path)
    try:
        local, synced = argv[1], argv[2]
    except:
        print("There was something wrong with your arguments. ", end = "")
        input("Press Enter to exit... ")
        exit()
        
    updater(local, synced)
    return

main(sys.argv)
