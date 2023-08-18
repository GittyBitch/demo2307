# ein Python module importieren um json Dateien zu bearbeiten
import json

print ("Willkommen")
Liste = ["Hamburg","Köln",3,4,5]
print ( Liste[1] )

dateiname = "Infos.json"
with open(dateiname, "r") as read_file:
    Person=json.load(read_file)

print ( Person["postleitzahl"] ) 
print ( Person["sexpartner"] [0]) 
print ("adios")


