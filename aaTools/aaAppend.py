'''
Created on 24 Oct 2014

Modules for use with Wonderware Archestra, various things to make the job easier.

USAGE:
    %prog in1_file.txt %character in2_file.txt
@author: Roan Fourie
@mail: roanfourie@gmail.com
'''
import sys

def append_files(in_file1, character, in_file2, out_file):
    """
    Created on 24 Oct 2014
    Created for use with Wonderware Archestra.
    Takes a file1 and appends file2 contents joined by a character, line for line.
    
    USAGE:
        %prog in_file1.csv %character in_file2.txt
    @author: Roan Fourie
    @mail: roanfourie@gmail.com
    """
    return_data = 0

    write_data = ''

    i = 0
    try:
        with open(in_file1, 'rt') as fi1:
            lines1 = fi1.readlines() # Read all the lines in fi1 as a tuple
        
        with open(in_file2, 'rt') as fi2:
            lines2 = fi2.readlines() # Read all the lines in fi2 as a tuple
                
        with open(out_file, 'at') as fo:
            fo.seek(0,2)
            while i < len(lines1):
                lines1[i] = lines1[i].rstrip('\n')
                #lines1[i] = lines1[i].rstrip('\r')
                fo.write(lines1[i] + character + lines2[i])
                i = i + 1
        print(write_data)
    except IOError:
        print("Error in reading/writing file.")
        return_data = 2
    else:
        print('Operation completed successfully.')
        return_data = 1
    finally:
        fi2.close()
        fi1.close()
        fo.close()
        print("done")
    return return_data

append_files(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])