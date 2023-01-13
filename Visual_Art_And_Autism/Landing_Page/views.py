from django.http import HttpResponse
from .models import FirstPage
from django.shortcuts import render
from gtts import gTTS
import playsound
def title(request):
    first_page_object = FirstPage.objects.all()[0]
    print(first_page_object.heading)
    #return HttpResponse(first_page_object.heading)
    context = {"First_Page_Data": first_page_object}
    readaloud(first_page_object.description)
    return render (request, 'Landing_Page/firstpage.html', context)
# Create your views here.
def readaloud(text):
    audio = gTTS(text)
    print("Testing..Testing..123")
    audio.save("audio.mp3")
    # playsound.playsound("audio.mp3")