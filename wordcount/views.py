from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    sr= sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
            
    return render(request, 'count.html',{'fulltext':fulltext, 'length': len(wordlist), 'sortedlist1': sr })


def about(request):
    return render(request,'aboutus.html')
