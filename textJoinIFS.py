#Simple script to change a list of values to a string seperated by ";" to be used for IFS search. 

import pyperclip

text = pyperclip.paste()
#print(text)

lines = text.split('\r\n')
#print(lines)
text = ';'.join(lines)

print(text)
pyperclip.copy(text)
#input("Done, press any key to exit")