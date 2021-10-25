import os

userdir = os.path.expanduser("~")          #get to the user path on mac
picturesDir = userdir +"/Pictures"          #get to Pictures directory, I could add this in the userdir step but I think it is easier to follow this way

##### add in foldername here #####
rootFolder = "/linkedin_headshots/"         #this is the folder where the pictures are stored
directory = picturesDir + rootFolder        #directory used for creating a list of folders
folders = os.listdir(directory)             #list of folders
try:
    folders.remove('.DS_Store')         #remove this hidden folder
except:
    pass
folders.remove('good_photos')           #remove good_photos folder, I could leave this in and I don't think anything would change with the program

fileNumbers = os.listdir(directory + "good_photos")         #get file numbers from good_photos folder and remove the extension and save as newFileNumbers

newFileNumbers = []
for file in fileNumbers:
    newFile = file[:len(file)-4]
    newFileNumbers.append(newFile)
print(fileNumbers)
print(newFileNumbers)

def run():
    for folder in folders:
        files = os.listdir(directory + "/" + folder)
        for file in files:
            match = False           # set match to false, this is used to determine if any numbers in newFileNumbers array is in the file name
            for num in newFileNumbers:
                path = directory + folder + "/" + file          #used to remove file if no match
                if num in file:
                    match = True
            if match == False:          # if no numbers in in newFileNumbers array match file name then the file is deleted
                print(path + ' will be deleted')
                if os.path.exists(path):            #not sure if this is needed but I added it to be safe
                        os.remove(path)

run()



