from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Text

from summarizer.summary import * 

# says that this function can do handle POST requests
@api_view(["POST", "GET"])
def summarize_view(request):
	
	# handle data inputs
	if request.method == "POST":
		
		# get the data and provide No value if not given
		text = request.data.get("text", None)
		
		# add it to the database and save
		new_addition = Text(text=text)
		new_addition.save()

		# pull the text and summarize it
		summary = summarize(new_addition.text)
		
		# return answer & status 200 (meaning everything worked!) 
		return Response(summary, status=200)
    if request.method == "GET":
        # get all the text in the database
        texts = (
            " ".join([text.text for text in Text.objects.all()])
            if Text.objects.all()
            else "No text found."
        )

        # return all the text
        return Response(texts, status=200)
		
