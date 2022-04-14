import glob
import shutil

# downloadFolder = "D:\Download\\"

downloadFolder = "D:\\archive\Downloads jan 17 2022\\"
audio = "D:\\archive\Downloads jan 17 2022\\audio\\"
installers = "D:\\archive\Downloads jan 17 2022\installers\\"
zipp = "D:\\archive\Downloads jan 17 2022\zip\\"
jar = "D:\\archive\Downloads jan 17 2022\jar\\"
images = "D:\\archive\Downloads jan 17 2022\images\\"
videos = "D:\\archive\Downloads jan 17 2022\\videos\\"
other = "D:\\archive\Downloads jan 17 2022\other\\"


class File():
    def __init__(self, dest) -> None:
        self.dest = dest
        self.name = self.dest.split("\\")[-1]
        if '.' in self.name:
            self.exten = self.name.split('.')[-1]
        else:
            self.exten = "folder"
    def __call__(self):
        return(self.name)


def sort(File):
    exten = File.exten
    if exten == "folder":
        pass
    elif exten == "mp3":
        path = audio + File.name
        
    elif exten == "exe" or exten == "msi":
        path = installers + File.name
        print(path)    
    elif exten == "zip" or exten == "7z" or exten == "rar":
        path = zipp + File.name
    elif exten == "jar":
        path = jar + File.name
    elif exten == "png" or exten == "jpg" or exten == "jpeg" or exten == "gif":
        path = images + File.name
    elif exten == "mp4" or exten == "wav":
        path = videos + File.name
    else:
        path = other + File.name

    try:
        shutil.move(File.dest, path)
    except:
        print("no path?")


for item in glob.glob("{0}*".format(downloadFolder)):
    i = File(item)
    sort(i)