The folder "aaTools" contain tools to make developing with Wonderware ArchestrA quicker or easier.
Currently 3 tools in the form of Python scripts exist:
    1. aaCreateScript.py    (Creates a Wonderware ArchestrA script from a file containing field attributes, in this case a script to create relative tag references)
    2. aaCSV.py (Creates a list of values from a csv exported galaxy object by giving the keyword, i.e. if you want to extract all the tagnames or all the PLCPaths or all the ShortDesc's)
    3. aaFA.py (Creates a list of tagnames with Field Attributes appended at the back using an exported CSV dump file.)
    4. aaAppend (Inputs two lists, outputs a list with list2 lines appended to list1 lines, separated by a character or string. Example list1 contains tagnames, list2 contains field attributes, character is a point.)
    
TODO:
    1. Create a user manual on how to use the aaFA and aaAppend tool.