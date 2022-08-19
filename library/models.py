from django.db import models
from django.utils.timezone import now

# import time
# Create your models here.

# curtime = time.ctime(time.time())
    
# timecol = curtime.split(' ')
# timecol2=timecol

# timecol2[0]=timecol[4]
# timecol2.pop()
# timecol=f"{timecol2[0]}-{timecol2[1]}-{timecol2[2]} {timecol2[3]}"

# print("From Models : ",timecol)
# print("From Models : ",curtime)

class Destination ( models.Model):
    name = models.CharField(max_length=100)
    item = models.CharField(max_length=500)
    song= models.FileField(default="null.mp3",max_length=500)
    lastopened = models.DateTimeField(default=now())