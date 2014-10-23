"""
Created on 21 Oct 2014

Modules for use with Wonderware Archestra, various things to make the job easier.

USAGE:
    %prog in_file.txt out_file.txt %keyword
@author: Roan Fourie
@mail: roanfourie@gmail.com
"""
import sys

def get_values(in_file, out_file, keyword1):
    """
    Created on 21 Oct 2014
    Created for use with Wonderware Archestra, using the exported csv file from an object.
    Lets say you exported a composite object to a csv file and you want all the short descriptions or all the tagnames, this function will get it for you.
    *note that input file encoding have to be UTF-16-LE. 
    
    USAGE:
        %prog in_file.csv out_file.txt %keyword
    @author: Roan Fourie
    @mail: roanfourie@gmail.com
    """
    return_data = 0
    str_data = ' '
    write_data = ''
    kw_position = -1
    next_row = 0
    occurences = 0
    start_position = 0
    count1 = 0
    count2 = 0
    i = 0
    try:
        with open(in_file, 'rt', encoding='utf-16-le') as fi:
            for line in fi: #For each line do the following
                str_data = line
                if next_row == 1: #Means that a valid keyword was found in the previous row
                    i = 0
                    count1 = 0
                    count2 = 0
                    while i < len(str_data): #Iterate until the amount of commas is reached, we know the amount of commas from the previous row
                        i = i+1
                        if str_data[i-1] == ",": #Looks for the commas and count them with their positions in the string
                            count1 = count1 + 1
                            count2 = count2 + 1
                            if count1 == occurences: #The keyword begin position is reached, get the position in the string
                                start_position = i-1
                            if count2 == (occurences + 1): #The keyword end position is reached, get the position in the string
                                end_position = i-1
                                i = len(str_data)
                    start_position = start_position + 1 #Else the first comma is also copied for output
                    if kw_position <= 2: #this part for when the keyword is at the beginning without a comma in front of it
                        start_position = start_position - 1
                    print('Value = ', str_data[start_position:end_position])
                    write_data = str_data[start_position:end_position] + '\n' #Build the data string with a new line appended to it
                    with open(out_file, 'at') as fo: #Write the data string to a file
                        fo.seek(0,2)
                        fo.write(write_data)
                    fo.close()
                    next_row = 0
                kw_position = str_data.find(keyword1) #Check the keyword position in the line, -1 if not found
                if kw_position > -1: #If the keyword is found in the line
                    next_row = 1 #set the next row to be processed for the keyword
                    occurences = str_data.count(',', 0, kw_position) #Check how many comma's it is up to the keyword
    except IOError:
        print("Error in reading/writing file.")
        return_data = 2
    else:
        print('Operation completed successfully.')
        return_data = 1
    finally:
        print("done")
    return return_data

get_values(sys.argv[1], sys.argv[2], sys.argv[3])