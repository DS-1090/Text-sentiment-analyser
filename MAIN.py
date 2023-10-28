    
import matplotlib.pyplot as mp
from textblob import TextBlob as tb

pos=0
neg=0
neut=0
t=[]
n=int(input("Enter no of Sentences:"))
for i in range(n):
    t.append(input("enter text:"))
for i in range(n):    
    sentiment= tb(t[i]).sentiment.polarity
    if(sentiment>0):
        pos +=1
        print("positive st")
    elif(sentiment<0):
        neg+=1
        print("negative st")

    else:
        neut+=1
        print("neutral st")


total=pos+neg+neut

pos_percent=(pos/total)*100
neg_percent=(neg/total)*100
neut_percent=(neut/total)*100
val={"positive":pos_percent, "negative":neg_percent, "neutral":neut_percent}

xval=list(val.keys())
yval=list(val.values())
fig = mp.figure(figsize = (10, 5))
mp.bar(xval, yval, color ='blue', width = 0.4)
mp.xlabel("Sentiment")
mp.ylabel(" percentage ")
mp.title("Sentiment analysis of Texts")
mp.show()
