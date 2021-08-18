
import sys
from wrappers import wrapper
from graphics import info



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

    wrapper_class = wrapper(sys.argv[2],sys.argv[3],sys.argv[4])




