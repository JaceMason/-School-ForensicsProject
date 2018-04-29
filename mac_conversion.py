import sys
import argparse

#Place holder functions will be finished soon.
def convertToBinary(value, fileOption):
    if fileOption:
        try:
            valueFile = open(value, 'r')
        except:
            print("Sorry, " + value + " does not exist. Make sure it is correct")
            sys.exit()
        value = valueFile.read()
        value = value[:-1]

    if (value[0] + value[1]) == '0x':
        value = value[2:]
    else:
        print("The value '" + value + "' is not hex (does it start with '0x'?")
        sys.exit()

    if(len(value) != 4):
        print("The value '" + value + "' is not of length 4")
        sys.exit()
    value = bin(int(value, 16))
    value = str(value)[2:]
    if len(value) != 16:
        value = value.zfill(16)
   
    return(str(value)) 
        

def convertToDate(value):
    months =['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 

    year = int(value[:7], base=2)
    month = int(value[7:11], base=2)
    day = int(value[11:], base=2)

    year = year + 1980
    month = months[month]
    
    print("Date: " + month + ' ' + str(day) + ', ' + str(year))
    
def convertToTime(value):
    hour = int(value[:5], base=2)
    minute = int(value[5:11], base=2)
    second = int(value[11:], base=2)
    
    ampm = ''
    if hour > 11:
        ampm = 'PM'
    else:
        ampm = 'AM'

    hour = hour % 12
    if hour == 0:
        hour = 12
    print("Time: " + str(hour) + ':' + str(minute) + ':' + str(second) + ampm)
    
    
def main():
    fileValue = ''
    hexValue = ''
    #Create the parser.
    #Because I needed to use the -h options I had to add "add_help=false"
    #I recommend removing this option if you can.
    parser = argparse.ArgumentParser(description="Converts to a date/time",
                                     add_help=False)

    #Handle first option (mutually exclusive options [cannot use -D with -T])
    #Determines the function to call.
    timeDateOption = parser.add_mutually_exclusive_group(required = True)
    timeDateOption.add_argument('-D', dest = 'convertType', const=convertToDate,
                                action = 'store_const',
                                help = "converting to a date")
    timeDateOption.add_argument('-T', dest = 'convertType', const=convertToTime,
                                action = 'store_const',
                                help = "converting to a time")

    #Handle second option (also mutually exlclusive)
    #Determines the value that goes into the function.
    #Doesn't check if it is a file or a hex value, but needs to eventually
    fileHexOption = parser.add_mutually_exclusive_group(required = True)
    fileHexOption.add_argument('-f', nargs='?', dest = 'fileValue',
                               help = "values stored in files")
    fileHexOption.add_argument('-h', nargs='?', dest = 'hexValue',
                               help = "values stored in files")

    #Parse the args and put the structure into "args"
    #"args" should have two values, "convertType" and "value"
    #which we created in the "add_argument" functions
    args = parser.parse_args()

    #Run the function stored in the first argument (stored in args.convertType)
    value = ''

    if args.fileValue != None:
        value = convertToBinary(args.fileValue, True)
    else:
        value = convertToBinary(args.hexValue, False)
        
    args.convertType(value)

if __name__ == "__main__":
    exit(main())
