from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

openai_api_key = settings.APIKEY

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hihihihihihih'
        return JsonResponse ({'message': message, 'response':response})
    return render(request, 'chatbot.html')