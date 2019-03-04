def main():
    f1 = input("Enter a source file:").strip()
    f2 = input("Enter a source file:").strip()

    # open file
    infile = open(f1, "r")
    outfile = open(f2, "w")

    # copy file
    countLines = 0
    countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and", countChars, "chars copied")

    # close file
    infile.close()
    outfile.close()
main()