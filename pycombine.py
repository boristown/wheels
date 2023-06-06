import sys

if __name__ == '__main__':
    #call as:
    #python pycombine.py <input python file path> <output python file path>
    #output name of input path and output path
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    print("input path: " + input_path)
    print("output path: " + output_path)
    #解析输入文件中的代码，将其中引用的文件提取出来，合并成一个文件，输出到output_path
    #parse the code in input file, extract the files referenced in it, combine them into one file, and output to output_path

    #打开输入文件，读取其中的代码
    #open the input file and read the code in it
    input_file = open(input_path, 'r')
    input_code = input_file.read()
    input_file.close()

    #解析代码，提取其中引用的文件
    #parse the code and extract the files referenced in it

    #打开输出文件，写入代码
    #open the output file and write the code in it
    output_file = open(output_path, 'w')
    output_file.write(input_code)

    #关闭输出文件
    #close the output file
    output_file.close()