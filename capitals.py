capitals = {"England": "London",
             "China": "Beijing",
             "Somalia": "Mogadishu"
             }
## print(capitals.get("Somalia", N/A))
## capitals.update({"Scotland" : "Edinburgh"})
## print(capitals)
## capitals.pop("China")
## print(capitals)
## capitals.popitem() pops latest item 
## capital.clear() clears everything
## keys = capitals.keys()
''' for key in capitals.keys():
 print(key) ## iterates over every key
'''
## value = capitals.values()
''' for value in capitals.values():
 print(value)
'''

''' for x, y in capitals.items():
 print(f"{x} : {y}")
'''
## del capitals["England"]
## print("England" in capitals) -> prints True
''' new_capitals = {"Spain" : "Madrid",
                "France" : "Paris",
                "Italy" : "Rome",
                }
capitals.update(new_capitals)
print(capitals)
'''
new = {country: capital for country, capital in capitals.items()}
print(new)
