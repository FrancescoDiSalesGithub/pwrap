class info:
    def __init__(self) -> None:
        pass

    def print_help(self):
        print("------ help ----------")
        print("")
        print("usage: python3 pwrap.py [URL] [File inclusion entrypoint] [wrapper] [filename-where-there-are-cookies-info.yaml]")
        print("")
        print("possible wrappers: ")
        print("file - puts the file wrapper in the entrypoint")
        print("filter - applies filter wrapper in the entrypoint")
        print("data - puts the data wrapper in the entrypoint")
        print("zip - puts the zip wrapper in the entrypoint")
        print("expect - puts the expect wrapper in the entry point")
        print("input - puts the input wrapper in the entry point")
        
        print("")
        print("example usage: ")
        print("python3 pwrap.py http://vulnerablesite.com/ page file cookie.yaml")
        print("python3 pwrap.py http://vulnerablesite.com/ directory all cookie.yaml")
        print("python3 pwrap.py http://vulnerablesite.com/ module expect cookie.yaml")

        print("---------------------------------------------------")
        print("correct yaml compilation")
        print("---------------------------------------------------")
        print(" ")
        print('write each cookie information as "key":"value"')
        print("example of correct yaml file: ")
        print("---")
        print('"PHPSESSID": "abc123456"')
        print('"token":"secret information"')
        
