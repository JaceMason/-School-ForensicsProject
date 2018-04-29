import sys
import hashlib

def errMsg(error):
    sys.exit(error)

def calcByBytes(fileName):
    with fileName:
        return fileName.read()

def calcMD5(fileName):
    return hashlib.md5(calcByBytes(fileName)).hexdigest()

def calcSHA1(fileName):
    return hashlib.sha1(calcByBytes(fileName)).hexdigest()
def main():
    try:
        fileName = sys.argv[1]
        image = open(fileName, 'rb')
    except IndexError:
        errMsg("There was no file given")
    except FileNotFoundError:
        errMsg(fileName+ " was invalid or did not exist")

    #DO STUFF    
    md5Checksum = calcMD5(image)
    md5File = open("MD5-" + fileName + ".txt", 'w')
    md5File.write(md5Checksum)

    image = open(fileName, 'rb')
    sha1Checksum = calcSHA1(image)
    shaFile = open("SHA1-" + fileName + ".txt", 'w')
    shaFile.write(sha1Checksum)
    #End Stuff
    
if __name__ == "__main__":
    exit(main())
