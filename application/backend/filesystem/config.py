import configparser

class Config:

    file_mod = {
        "create": "w+",
        "read": "r",
        "write": "w"
    }

    file_path_creation = "./config.ini"
    file_path = "./config.ini"

    def __init__(self):
        self.config = configparser.ConfigParser()


    def write_config(config, mod):
        '''writes the config object to the config.ini file'''
        path = Config.file_path_creation if mod == "create" else Config.file_path
        try:
            with open(path, Config.file_mod[mod]) as file:
                config.write(file)
        except KeyError:
            pass

    def setup(self):
        '''creates config.ini file if not already present
           restores config.ini file if already present'''
        self.config["PATH"] = { "DefaultPath": "/" }
        self.config["DEFAULTS"] = {
            "DefaultFormat": "mp4",
            "DefaultResolution": "720p"
            }
        Config.write_config(self.config, "create")

    def set_default(self, section, key, value):
        '''sets defaultpath config to have defaultpath as value'''
        self.config.read(self.file_path)
        sections = self.config.sections()
        if section in sections:
            self.config[section][key] = value
            Config.write_config(self.config, "write")

    def get_default(self, section, key):
        '''retrieves defaultpath value'''
        self.config.read(self.file_path)
        sections = self.config.sections()
        if section in sections:
            return self.config[section][key]

if __name__ == "__main__":
    configurer = Config()
    configurer.setup()