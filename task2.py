import sys

def errMsg(error):
    sys.exit(error)

def main():
    try:
        fileName = sys.argv[1]
        image = open(fileName, 'r')
    except IndexError:
        errMsg("There was no file given")
    except FileNotFoundError:
        errMsg(fileName+ " was invalid or did not exist")
        
    print(fileName)
if __name__ == "__main__":
    exit(main())
