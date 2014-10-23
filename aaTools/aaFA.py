"""
Created on 23 Oct 2014

Modules for use with Archestra, various things to make the job easier.

USAGE:
    %prog in_file.csv out_file.txt
@author: Roan Fourie
@mail: roanfourie@gmail.com
"""
import sys

def get_fa(in_file, out_file):
    """
    Created on 21 Oct 2014
    Created for use with Archestra, using the exported csv file from an object.
    Lets say you exported a composite object to a csv file and you want all the Field Attributes but with the relevant Tag name appended infront with a ".", this function will get it for you.
    *note that input file encoding have to be UTF-16-LE.
    *note all Field Attributes must start with FA_* 
    
    USAGE:
        %prog in_file.csv out_file.txt
    @author: Roan Fourie
    @mail: roanfourie@gmail.com
    """
    return_data = 0
    str_data = ' '
    at_data = ''
    write_data = ''
    tagname = ''
    attributes = ''
    kw_position = -1
    pp_position = -1
    lc_position = -1
    c_position = -1
    next_row = 0
    occurences = 0
    try:
        with open(in_file, 'rt', encoding='utf-16-le') as fi:
            for line in fi: # For each line do the following
                str_data = line
                
                if next_row == 1:
                    c_position = str_data.find(',')
                    tagname = str_data[0:c_position]
                    for attribute in attributes:
                        write_data = tagname + '.' + attribute + '\n' #Build the data string with a new line appended to it
                        with open(out_file, 'at') as fo: #Write the data string to a file
                            fo.seek(0,2)
                            fo.write(write_data)
                        fo.close()
                        print(write_data)
                    next_row = 0
                
                kw_position = str_data.find('UserAttrData') # Check the keyword position in the line, -1 if not found
                
                if kw_position > -1: # If the keyword is found in the line
                    next_row = 1 # set the next row to be processed for the tagname
                    kw_position = kw_position + 13
                    pp_position = str_data.find('.',kw_position, len(str_data)) # Check for the first '.' character in the Field Attributes
                    occurences = str_data.count(',', kw_position, pp_position) # Check how many comma's it is up to the last Field Attribute
                    if occurences == 0:
                        next_row = 0
                    lc_position = str_data.rfind(',', 0, pp_position)
                    at_data = str_data[kw_position:lc_position]
                    attributes = at_data.split(",")
    except IOError:
        print("Error in reading/writing file.")
        return_data = 2
    else:
        print('Operation completed successfully.')
        return_data = 1
    finally:
        print("done")
    return return_data

get_fa(sys.argv[1], sys.argv[2])