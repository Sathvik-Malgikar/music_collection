from urllib.request import Request
from django.shortcuts import render,redirect
from django.utils.timezone import now
from .models import Destination
from django.contrib import messages
import os
import random
from django.http import HttpResponse


# Create your views here.

def getmedia(req):
    item = req.GET["it"]
    obj = Destination.objects.filter(item=item)
    obj.update(lastopened=now())
    return redirect('/media/'+item)


def library ( req ) :
    
    
    files = Destination.objects.all() 
    print(files)
    files = sorted(files,key=lambda file : file.lastopened , reverse=True)
    recommended =   random.choice(files)
    recommended={"name" : recommended.name,"item": recommended.item}
    items = Destination.objects.values_list("item")
    items = list(items)
    return render ( req , 'library.html',{"mega_list" : files ,"items" : items , "recommended":recommended})

def listen(req):
    audio_link=req.GET["song"]
    return HttpResponse("Your song will start playing. Enjoy !!\n ( headphones recommended )"+audio_link)

def search(req) :
    
    substring = req.POST['searchField']
    if(substring==''):
        messages.info(req,"Please enter the name of the song you want to search")
        return redirect('/library')
    substring = substring.lower()
    print("Recieved : ",substring,"\n  length : ",len(substring),"\n")
    
    # items  = list ( Destination.objects.values_list("item"))
    items  = Destination.objects.values_list("item")
    print("number of items : ",len(items),"\n")
    for (item,) in items:
        iteml=item.lower()
        print("item : ",iteml,"\n")
        if (substring in iteml):
            print("Match found :) " ,item,"\n")
            o1 = Destination.objects.filter(item=item)
            time  = now()
            # print(time)
            o1.update(lastopened=time)
            return redirect('/media/'+item)
    messages.info(req,"Song not :( found please type the name correctly or try another song")
    print("no match found :(")
    return redirect('/library')
    