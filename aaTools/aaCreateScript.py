"""
Created on 15 Oct 2014

Modules for use with Wonderware Archestra, various things to make the job easier.

USAGE:
    %prog in_file.txt out_file.txt
@author: Roan Fourie
@mail: roanfourie@gmail.com
"""
import sys

def create_script_tagnames(in_file, out_file):
    """
    Created on 15 Oct 2014
    Created for use with Wonderware Archestra to create the if statements used in the scrAssignIO scripts.
    It takes a text file containing a list of Field Attributes and creates a new text file with the if statements.
    
    USAGE:
        %prog in_file.txt out_file.txt
    @author: Roan Fourie
    @mail: roanfourie@gmail.com
    """
    return_data = 0
    str_data = ''
    write_data = ''
    #current_row = 0
    try:
        with open(out_file, 'at') as fo:
            fo.seek(0,2)
            write_data = """'Wait two execution counts to make sure script executes\nIf Me.scrAssignIO.ExecutionCnt > 2 Then\n
'Declare variables\n
\tDIM Datasource AS STRING;
\tDIM AliasDB AS INDIRECT;
"""
            fo.write(write_data)
            #print(write_data)
        fo.close()
        with open(in_file, 'rt') as fi:
            for line in fi:
                #str_data = fi.readline()
                str_data = line
                with open(out_file, 'at') as fo:
                    fo.seek(0,2)
                    write_data = '\tDIM '+ str_data.rstrip('\n') + '_Exist AS INTEGER;\n'
                    fo.write(write_data)
                    #print(write_data)
                fo.close()
                #print(line)
                #print(str_data)
        with open(out_file, 'at') as fo:
            fo.seek(0,2)
            write_data = """\n\n'Datasource is the input/output source you want to allocate to your field attribute
\tDatasource = Me.PLCPath + "." + Me.Tagname;\n
'Create the alias list that is in the Device Integration object using the PLCPath uda to make it more dynamic
\tAliasDB.bindto(Me.PLCPath + ".AliasDataBase");
\t'The exist variables will return an integer value when the string exists in the alias database in the DI object
\t'A string comparison is done between the Alias DB list and the Attribute to see if the attribute exists in the Alias DB
\t'The StringChar function looks at the ASCII value for a quote which seperates the alias tags from each other in the aliasDB\n
"""
            fo.write(write_data)
            #print(write_data)
        with open(in_file, 'rt') as fi:
            for line in fi:
                #str_data = fi.readline()
                str_data = line
                with open(out_file, 'at') as fo:
                    fo.seek(0,2)
                    write_data = '\t' + str_data.rstrip('\n') + '_Exist = StringInString(AliasDB, (StringChar(34) + Me.TagName + ".'+ str_data.rstrip('\n') +'" + StringChar(34)),1,0);\n'
                    fo.write(write_data)
                    #print(write_data)
                fo.close()
                #print(line)
        with open(out_file, 'at') as fo:
            fo.seek(0,2)
            write_data = '\n\n'+"\t'"+ 'The value is then assigned to the DIN Field Attribute input source or unassigned if it is not in the AliasDB\n'
            fo.write(write_data)
            #print(write_data)
        with open(in_file, 'rt') as fi:
            for line in fi:
                #str_data = fi.readline()
                str_data = line
                with open(out_file, 'at') as fo:
                    fo.seek(0,2)
                    write_data = '\tIf %s_Exist > 0 Then\n\t\tMe.%s.Input.InputSource = Datasource + ".%s";\n\tElse\n\t\tMe.%s.Input.InputSource = "---";\n\tEndIf;\n\n' % (str_data.rstrip('\n'), str_data.rstrip('\n'), str_data.rstrip('\n'), str_data.rstrip('\n'))
                    fo.write(write_data)
                    #print(write_data)
                fo.close()
                #print(line)
        with open(out_file, 'at') as fo:
            fo.seek(0,2)
            write_data = """\n'The script is then finished by setting the trigger bit to true and it will stop executing
    Me.AssignIOCmd = True;\n
EndIf;\n
'A Log Message flag is added to see if the script executed in the SMC - This can be excluded and is for troubleshooting
'LogMessage (Me.Tagname + "Finished");\n
"""
            fo.write(write_data)
            #print(write_data)
        fo.close()
    except IOError:
        print("Error in reading/writing file.")
        return_data = 2
    else:
        print('Operation completed successfully.')
        return_data = 1
    finally:
        fi.close()
        #fo.close()
        print("done")
    return return_data

create_script_tagnames(sys.argv[1], sys.argv[2])