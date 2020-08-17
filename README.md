# ArchestrA Tools  

The folder __aaTools__ contain my own set of tools (mostly Python scripts) that were used to make developing Wonderware ArchestrA Projects quicker or easier. To use it you will have to download or clone this project to a local computer. The scripts is mostly executed from command prompt and usually either require some variables to be edited or some input files.  

## Overview and Contents  

1. ```aaCreateScript.py```    (Creates a Wonderware ArchestrA script from a file containing field attributes, in this case a script to create relative tag references)
2. ```aaCSV.py``` (Creates a list of values from a csv exported galaxy object by giving the keyword, i.e. if you want to extract all the tagnames or all the PLCPaths or all the ShortDesc's)
3. ```aaFA.py``` (Creates a list of tagnames with Field Attributes appended at the back using an exported CSV dump file.)
4. ```aaAppend``` (Inputs two lists, outputs a list with list2 lines appended to list1 lines, separated by a character or string. Example list1 contains tagnames, list2 contains field attributes, character is a point.)  
5. [ww-history-daily-max.py](#ww-historian-daily-max) Query a Historian database for the maximum daily values for each day between two dates and filtered for certain times of day only.  

- [ToDo, License and Contribute](#TODO)  

## ww-historian-daily-max  

The script connects to the SQL Historian, then for each tag in a list (configured in the script), it will retrieve the maximum value for each day between two dates. The daily data is filtered between two time slots as well (i.e. between 2 AM and 5:30 AM).  

### Requirements  

1. Windows based computer with network access and Windows authentication to the Historian.  
2. Python 3.8 or later installed.  
3. Pandas Python package installed. ```pip install pandas```  
4. Numpy Python package installed. ```pip install numpy```  
5. Pyodbc Python package installed. ```pip install pyodbc```  
6. The script: ```ww-historian-daily-max.py```  

### Execute  

1. Edit the script for Historian Server Name, tagnames, dates and times.  
2. Run script from the command prompt from the directory on a PC which can access the Historian by means of Windows Authentication. ```>py .\ww-historian-daily-max.py```  
3. The script will create a csv file for each tagname with the date and the value for the day.  

## TODO  

1. Update the scripts and add the new ones.  
2. Create a Walkthrough on how to use the aaFA and aaAppend scripts.  
3. Refactor the code.  

## License  

MIT License.  
License can be viewed [here.](LICENSE)  

## Contribute  

Feel free to contribute to this work by sending me a [message](mailto:roanfourie@gmail.com) or by submitting an [issue](https://github.com/RoanFourie/ArchestrA-Tools/issues).  
