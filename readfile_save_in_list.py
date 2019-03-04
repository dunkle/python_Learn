def main():
    # save as list every line
    result = []
    file = open("average_number", "r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    print(result[0][0])
    file.close()


main()