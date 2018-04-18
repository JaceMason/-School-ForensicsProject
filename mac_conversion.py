import argparse

#Place holder functions will be finished soon.
def convertToDate(value):
    print(value + " convert to date")

def convertToTime(value):
    print(value + " convert to time")

def main():
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
    fileHexOption.add_argument('-f', nargs='?', dest = 'value',
                               help = "values stored in files")
    fileHexOption.add_argument('-h', nargs='?', dest = 'value',
                               help = "values stored in files")

    #Parse the args and put the structure into "args"
    #"args" should have two values, "convertType" and "value"
    #which we created in the "add_argument" functions
    args = parser.parse_args()

    #Run the function stored in the first argument (stored in args.convertType)
    #
    args.convertType(args.value)

if __name__ == "__main__":
    exit(main())
