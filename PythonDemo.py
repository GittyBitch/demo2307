# ein Python module importieren um json Dateien zu bearbeiten
import json

print ("Willkommen")
Liste = ["Hamburg","Köln",3,4,5]
print ( Liste[1] )

Person = {

        "name": "Karl-Heinz",
        "postleitzahl": "11111",
        "strasse": "weg 8",
        "sexpartner": ["Bernd", "Adolf", "Benny", "der andere Bernd"],
}

dateiname = "Infos.json"
with open(dateiname, "w") as write_file:
    json.dump(Person, write_file, indent=4)

print ( Person["postleitzahl"] ) 
print ( Person["sexpartner"] [0]) 
print ("adios")


