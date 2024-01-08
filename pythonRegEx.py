#Expréssion régulière

import re
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

#Fonction findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Fonction search
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Fonction sub
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)




