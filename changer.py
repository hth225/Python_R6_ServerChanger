def mainmenu():
    # fileloc = open("location.txt", 'r')
    # # for i in fileloc.readline():

    # fileloc.close()

    servloc = open("C:\\Users\\LAD\\Documents\\My Games\\Rainbow Six - Siege\\88b82571-82f9-49bd-a0df-7576dd6f39b2\\GameSettings.ini", 'r+')
    for i, info in enumerate(servloc):
        if "DataCenterHint=" in enumerate(servloc):
            print(info)

    servloc.close()

def save_file_location():
    location = input("Enter GameSettings.ini file locaion :")
    wr = open("location.txt", "w")
    wr.write(location)
    wr.close()
    return location

if __name__ == '__main__':
    # save_file_location()
    file = open("location.txt", 'r')
    content = file.read()
    if content == None:
        save_file_location()
    else:
        mainmenu()

    file.close()