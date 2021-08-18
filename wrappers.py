


class wrapper:

    __possible_wrappers={
        "file":"file://",
        "zip":"zip://"}

    def __init__(self,url,entry,wrapper):
        self.__url=url
        self.__entry=entry
        self.__wrapper=wrapper
        pass

    def check_wrapper(self):
        for value in self.__possible_wrappers:
            if value == self.__possible_wrappers[value]:
                print("ok")
    
    def elaborate(self):
        pass

    def set_url(self,url):
        self.__url = url

    def get_url(self) -> str:
        return self.__url

    def set_entry(self,entry):
        self.__entry=entry

    def get_entry(self) -> str:
        return self.__entry

    def set_wrapper(self,wrapper):
        self.__wrapper = wrapper

    def get_wrapper(self):
        return self.__wrapper

