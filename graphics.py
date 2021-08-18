class info:
    def __init__(self) -> None:
        pass

    def print_help(self):
        print("------ help ----------")
        print("")
        print("usage: python3 pwrap.py [URL] [File inclusion entrypoint] [wrapper]")
        print("")
        print("possible wrappers: ")
        print("file - puts the file wrapper in the entrypoint")
        print("data - puts the data wrapper in the entrypoint")
        print("zip - puts the zip wrapper in the entrypoint")
        print("expect - puts the expect wrapper in the entry point")
        print("input - puts the input wrapper in the entry point")
        print("all - prints all the possible wrappers")
        print("")
        print("example usage: ")
        print("python3 pwrap.py http://vulnerablesite.com page file")
        print("python3 pwrap.py http://vulnerablesite.com directory all")
        print("python3 pwrap.py http://vulnerablesite.com module expect")
        