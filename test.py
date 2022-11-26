import matplotlib.pyplot as plt
import pymongo
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as pyt
import datetime
import numpy as np
import time

cli=pymongo.MongoClient("mongodb://localhost:27017")
mydba=cli["accounts"]
myt=mydba['Oct']
total=0
average=0
l=[]
d=[]
dat={"Amount":[],"Date":[]}

data=myt.find()
for i in data:
   l.append(int(i["Amount"]))

   d.append(i["date"])

l.sort()
d.sort()
fig = plt.figure(figsize = (10, 5))
pyt.bar(d,l,color="Pink",width=0.4)
pyt.title("Oct")
pyt.show()
