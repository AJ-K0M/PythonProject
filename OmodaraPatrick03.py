# module for regular expressions.
import re;
# module for program arguments.
import sys;

'''
To get practice in using Python file objects, program arguments, and regular expressions.
Create a python script that will read in a text file of possible credit card numbers
and attempt to categorize them to major credit card networks: American Express (Amex), Visa, Mastercard

Author: Patrick Omodara
'''
# Exit and Usage messages displays if the correct program arguments are not inputed.
exitMessage = "Error: Expecting 2 program arguments, found " + str(len(sys.argv)) + "instead.\n";
exitMessage += "Usage: python OmodaraPatrick03.py cc_numbers_python.txt \n";

# Ensure there is a file in the program argument.
if (len(sys.argv) != 2):
    exit(exitMessage);
# Regex for the various credit Cards.
amexInput = re.compile('^3[47]\d{13}$');
masterInput1 = re.compile('^5[1-6]\d{14}$');
masterInput2 = re.compile('^222[1-9]\d{12}$');
masterInput3 = re.compile('^2720\d{12}$');
visaInput1 = re.compile('^4\d{12}$');
visaInput2 = re.compile('^4\d{16}$');

# Pulls the file from the program argument.
inputFile = sys.argv[1];

# In case the wrong file name is entered.
try:
    # File Object to open file in "read" mode.
    inFH = open(inputFile, 'r');
    # Displays when the wrong file is entered.
except FileNotFoundError:
    exit("Error: Cannot find file: " + inputFile);
    # Displays when the file has no read permission.
except PermissionError:
    exit("Error: No read permission: " + inputFile);

# FOR loop to find the search for the card numbers line by line.
for line in inFH:
    # Searches for the Amex credit card in the file and displays it.
    if (amexInput.search(line)):
        print('AMEX' + line.rstrip());
    # Searches for the Master credit card in the file and displays it.
    elif (masterInput1.search(line)):
        print('Mastercard'+ line.rstrip());
    # Searches for the Master credit card in the file and displays it.
    elif (masterInput2.search(line)):
        print('Mastercard'+ line.rstrip());
    # Searches for the Master credit card in the file and displays it.
    elif (masterInput3.search(line)):
        print('Mastercard'+ line.rstrip());
    # Searches for the Visa credit card in the file and displays it.
    elif (visaInput1.search(line)):
        print('VISA'+ line.rstrip());
    # Searches for the Visa credit card in the file and displays it.
    elif (visaInput2.search(line)):
        print('VISA'+ line.rstrip());

# Close file object.
inFH.close();
# display when code has ran.
print('Program done.')
