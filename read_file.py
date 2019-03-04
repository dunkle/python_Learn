def main():
    fileName = input("enter file name:\n")
    infile = open(fileName, 'r')
    line = infile.readline()
    print(line)
main()