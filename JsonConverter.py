import json
import sys


def main():
    inputFileName="input.txt"
    outputFileName="output.json"
    if len(sys.argv) >1:
        inputFileName=sys.argv[1]
    if len(sys.argv) >2:
        outputFileName=sys.argv[2]

    read=open(inputFileName, 'r')
    result={}
    result["mdBlogText"]=read.read()
    var=json.dumps(result)
    read.close()
    print var
    write=open(outputFileName, "w+")
    write.write(var)
    write.close()


if __name__ == '__main__':
    main()


# Run python JsonConverter in terminal and script will look for a file named "input.txt" and will dump the output in a file with name output.json
# To provide different file name Run python JsonConverter <InputFileName> <OutputFileName>
