import _json
import json
import os

wrote=False

files = os.listdir("/Users/Srujan/Music")
with open("data.json","w") as f :
    f.write("[\n")  
    pk=1
    for file in files :
        p1 = file[0:29] + "..."
        item_us = file
        item_us = item_us.replace(" ","_")
        item_us = item_us.replace("(","")
        item_us = item_us.replace(")","")
        obj = { "pk" :  str(pk) ,"model" : "library.Destination" , "fields" :  { "name" : p1,"item" : file,"song" : item_us}}
        pk+=1
        if wrote :
            f.write(",") 
        json.dump(obj,f)   
        wrote=True
        f.write("\n")    
    f.write("]")  
    print("dumped")



