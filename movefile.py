import glob
import shutil
import os
from configparser import ConfigParser

class File():
    def __init__(self, dest):
        self.dest = dest
        self.name = self.dest.split("\\")[-1]
        self.category = {}
        if '.' in self.name:
            self.exten = self.name.split('.')[-1]
        else:
            self.exten = "folder"

    def addCategory(self,name,extentions):
        self.category[name] = extentions

    def categorize(self):
        if self.exten != "folder":
            for i in self.category:
                if self.exten in self.category[i]:
                    self.cat = i
                    break
                else:
                    self.cat = "other"
        else:
            self.cat = "folder"
    def move(self):
        if self.exten != "folder":
            self.path = "{0}{1}\{2}".format(
                "\\".join(self.dest.split("\\")[:-1]) + "\\",
                self.cat,
                self.name
            )
            if os.path.isdir("\\".join(self.path.split("\\")[:-1])):
                try:
                    shutil.move(self.dest, self.path)
                except Exception as e:
                    print("uh oh you fucked up -> {}".format(e))
            else:
                os.mkdir("\\".join(self.path.split("\\")[:-1]))
                try:
                    shutil.move(self.dest, self.path)
                except Exception as e:
                    print("uh oh you fucked up -> {}".format(e))

if __name__ == "__main__":
    configname = "weirdconfignamesoidontoverwritesomethingimportant.ini"
    folder = '{0}'.format("\\".join(__file__.split("\\")[:-1]) + "\\")
    category = {}
    config = ConfigParser()
    print("the file is " + __file__)
    while True:
        print("What to do:")
        print("[1]Create Config")
        print("[2]Move Files")
        print("[3]Exit")
        print()
        answer = int(input())
        if answer == 1:
            with open(configname, 'w') as f:
                pass
            config.read(configname)
            config.add_section("Folders")
            config.set("Folders", "video", "mp4,mkv,mov,wmv,avi,flv,f4v,swf")
            config.set("Folders", "audio", "mp3,aac,flac,alac,wav,aiff,dsd,pcm")
            config.set("Folders", "documents", "pdf,docx")
            config.set("Folders", "installers", "exe,msi")
            config.set("Folders", "Picture", "png,jpeg,gif,tiff,psd,raw")
            config.set("Folders", "zip", "zip,rar,7z")
            with open(configname, 'w') as configfile:    # save
                config.write(configfile)       
        elif answer == 2:
            if os.path.isfile(configname):
                config.read(configname)
                for i in config["Folders"]:
                    extentions  = config["Folders"][i].split(',')
                    category[i] = extentions
                
                for item in glob.glob("{0}\*".format(folder)):
                    i = File(item)
                    if i.dest != __file__ and i.name != configname:
                        i.category = category
                        i.categorize()
                        i.move()
                    else:
                        pass 
            else:
                print("Config doesn't exist, make one")
        elif answer == 3:
            break
            
    # for item in glob.glob("{0}\*".format(folder)):
    #     i = File(item)
    #     i.category = category
    #     i.categorize()
    #     i.move()
        
