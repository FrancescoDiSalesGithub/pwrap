
import sys
from wrappers import wrapper
from graphics import info
import requests

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("no arguments passed")
        sys.exit(-1)

    if len(sys.argv)>4:
        print("you have insert more than three arguments")
        sys.exit(-1)
    
    if sys.argv[1] == "help":
        graph_class=info()
        graph_class.print_help()
        sys.exit(0)

    try:
        wrapper_class = wrapper(sys.argv[1],sys.argv[2],sys.argv[3])
        filter_elaboration = wrapper_class.check_wrapper()

        with open("output.txt","w") as response:
            response.write(requests.get(str(filter_elaboration)).content)
    
    except Exception as exception:
        print(exception)


    
    




