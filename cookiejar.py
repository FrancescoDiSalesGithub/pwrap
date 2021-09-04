import yaml

class cookie_jar:

    def __init__(self,filename) -> None:
        
        with open(filename,"r") as stream:
            try:
                self.__data = yaml.safe_load(stream)
            except Exception as exception:
                print(exception)

    def get_data(self):
        temp_list_cookie_jar = []
        
        for value in self.__data:
            key = self.__data[value]
            temp_cookie_entry = (value,key)
            temp_list_cookie_jar.append(temp_cookie_entry)
        
        return temp_list_cookie_jar

