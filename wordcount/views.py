from django.shortcuts import render
from django.http import HttpResponse
import operator
def homepage(request):

	return render(request,'home.html')

def contact(request):
	return HttpResponse("<h2>contact us at</h2> <br><i>support@gmail.com</i>")

def count(request):
	data= request.GET['fulltextarea']
	word_list=data.split()
	list_length=len(word_list)


	word_dictionary={}
	for word in word_list:
		if word in word_dictionary:
			word_dictionary[word]+=1

		else:
		    word_dictionary[word]=1

	sorted_list = sorted(word_dictionary.items(), key= operator.itemgetter(1),reverse =True)	    	

	return render(request,'count.html',{'fulltext':data,'words':list_length,'worddict':word_dictionary.items()})