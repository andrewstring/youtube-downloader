import os
from backend.filesystem.config import Config
from backend.yt import execute_yt

clear = lambda: os.system("clear")

class Prompt():

    format = {
        "1": "mp4",
        "2": "mp3"
    }
    
    resolution = {
        "1": "720p",
        "2": "480p",
        "3": "360p"
    }

    def __init__(self):
        self.config = Config()
        self.url = ""
        self.format = ""
        self.resolution = ""
        self.path = ""
        self.file_name = ""

    def input_url(self):
        clear()
        url = input("Please enter video url: ")
        if "youtube.com" not in url:
            return self.input_url()
        self.url = url
        return self.url

    def input_format(self):
        clear()
        format = input('''Press enter to use default format or select format:
1. Video (mp4)
2. Audio (mp3)
3. Set Default
Select and press enter: ''')
        if format not in [ "", "1", "2", "3" ]:
            return self.input_format()
        elif format == "":
            self.format = self.config.get_default("DEFAULTS", "defaultformat")
        elif format == "3":
            self.format = self.input_default_format()
        else:
            self.format = Prompt.format[format]
        return self.format


    def input_default_format(self):
        clear()
        default_format =  input('''Select default format
1. Video (mp4)
2. Audio (mp3)
Select and press enter: ''')
        if default_format not in [ "1", "2" ]:
            return self.input_default_format()
        self.format = Prompt.format[default_format]
        self.config.set_default("DEFAULTS", "defaultformat", self.format)
        return self.format


    def input_resolution(self):
        clear()
        resolution = input('''Press enter to use default format or select resolution
1. 720p
2. 480p
3. 360p
4. Set Default
Select and press enter: ''')
        if resolution not in [ "", "1", "2", "3", "4" ]:
            return self.input_resolution()
        elif resolution == "":
            self.resolution = self.config.get_default("DEFAULTS", "defaultresolution")
        elif resolution == "4":
            self.resolution = self.input_default_resolution()
        else:
            self.resolution = Prompt.resolution[resolution]
        return self.resolution
        

    def input_default_resolution(self):
        clear()
        default_resolution = input('''Select default resolution
1. 720p
2. 480p
3. 360p
Select and press enter: ''')
        if default_resolution not in [ "1", "2", "3"]:
            return self.input_default_resolution()
        self.resolution = Prompt.resolution[default_resolution]
        self.config.set_default("DEFAULTS", "defaultresolution", self.resolution)
        return self.resolution

    def input_path(self):
        clear()
        path = input('''Press enter to use default path or enter path to set new default path.
Path: ''')
        if not path:
            self.path = self.config.get_default("PATH", "defaultpath")
            return self.path
        self.path = path
        self.config.set_default("PATH", "defaultpath", self.path)
        return self.path

    def input_file_name(self):
        clear()
        file_name = input('''Please enter name of file: ''')
        if not file_name:
            return self.input_file_name()
        self.file_name = file_name
        return self.file_name

    def runtime(self, url=None):
        if not url:
            self.input_url()
        self.input_format()
        if self.format == "mp4":
            self.input_resolution()
        self.input_path()
        self.input_file_name()

        clear()
        print("Url: ", self.url)
        print("Format: ", self.format)
        print("Resolution: ", self.resolution)
        print("Path: ", self.path)
        print("File Name: ", self.file_name)
        execute_yt(self.url,
            self.format,
            self.path,
            self.file_name,
            self.resolution)



    

if __name__ == "__main__":
    prompt = Prompt()
    prompt.runtime()