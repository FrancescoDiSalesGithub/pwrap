
import sys
from wrappers import wrapper
from graphics import info
from cookiejar import cookie_jar

import requests
import webbrowser

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("no arguments passed")
        sys.exit(-1)

    if len(sys.argv)>5:
        print("you have insert more than four arguments")
        sys.exit(-1)
    
    if sys.argv[1] == "help":
        graph_class=info()
        graph_class.print_help()
        sys.exit(0)


    wrapper_class = wrapper(sys.argv[1],sys.argv[2],sys.argv[3])
    filter_elaboration = wrapper_class.check_wrapper()

    with open("output.html","w") as response:
        
        session = requests.Session()
        jar = cookie_jar(str(sys.argv[4]))
        cookie = jar.get_data()

        cookie_dictionary = dict(cookie)
        responsePHP = session.get(str(filter_elaboration),cookies=cookie_dictionary)
        response.write(str(responsePHP.content.decode("utf-8")))

    webbrowser.open("output.html")
    



    
    




