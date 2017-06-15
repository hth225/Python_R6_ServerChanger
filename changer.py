def mainmenu(location):
    fileloc = open(location, 'r')
    addre = fileloc
    fileloc.close()

    servloc = open(addre, 'r')

    if location is None:
        save_file_location()
    else:
        print("Your server is "+servloc.find("DataCenterHint="))

def save_file_location():
    location = input("Enter GameSettings.ini file locaion :")
    wr = open("locaion.txt", "w")
    wr.write(location)
    wr.close()
    return location