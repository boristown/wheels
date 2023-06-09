import sys
import glob

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
    boristown_path = "boristown"
    #获取boristown文件夹下所有的.py文件的路径
    #get the paths of all .py files in boristown folder
    boristown_files = glob.glob(boristown_path + "/*.py")
    #提取文件名
    boristown_libs = [file.split("\\")[-1].split(".")[0] for file in boristown_files]
    #打开输入文件，读取其中的代码
    #open the input file and read the code in it
    input_file = open(input_path, 'r')
    input_code = input_file.read()
    input_file.close()

    #检查input_code中是否有代码：from boristown.[lib] import ...
    #如果有，则注释该行代码，然后把boristown文件夹下对应的lib文件中的代码复制到input_code中
    #其中[lib]是boristown_libs中的一个元素
    #check if there is code in input_code: from boristown.[lib] import ...
    #if there is, comment out that line of code, and then copy the code in the corresponding lib file in boristown folder to input_code
    #where [lib] is an element in boristown_libs
    while True:
        find = False
        for lib in boristown_libs:
            #检查input_code中是否有代码：from boristown.[lib] import ...
            #check if there is code in input_code: from boristown.[lib] import ...
            patten = "\nfrom boristown." + lib + " import"
            print("patten: " + patten)
            index = input_code.find(patten)
            if index != -1:
                find = True
                print('found code: ' + patten)
                #找到该行代码的位置
                #find the position of that line of code
                #index = input_code.find("from boristown." + lib + " import")
                #找到该行代码的结尾位置
                #find the end position of that line of code
                end_index = input_code.find("\n", index+1)
                #注释该行代码
                #comment out that line of code
                input_code = input_code.replace("from boristown." + lib + " import", "#from boristown." + lib + " import")
                #打开boristown文件夹下对应的lib文件，读取其中的代码
                #open the corresponding lib file in boristown folder and read the code in it
                lib_file = open(boristown_path + "/" + lib + ".py", 'r')
                lib_code = lib_file.read()
                lib_file.close()
                end_index+=1
                #把lib_code中的代码复制到input_code中，被注释的代码之后
                #copy the code in lib_code to input_code, after the commented out code
                input_code = input_code[:end_index] + "\n" + lib_code + "\n" +  input_code[end_index:]
        if not find:
            break

    #解析代码，提取其中引用的文件
    #parse the code and extract the files referenced in it

    #打开输出文件，写入代码
    #open the output file and write the code in it
    output_file = open(output_path, 'w')
    output_file.write(input_code)

    #关闭输出文件
    #close the output file
    output_file.close()