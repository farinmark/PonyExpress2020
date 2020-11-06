import Pathes

def Print(string):
    if Pathes.mode:
        print(string)
        output = open(Pathes.output_file_name,'a')
        output.write(string+'\n')
        output.close()
        return
    else:
        print(string)
        return