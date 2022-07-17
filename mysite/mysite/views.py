from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def analyze(request):
    djtext= request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    space_remover = request.GET.get('space_remover', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'removed punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif uppercase == "on":
            param = {'purpose': 'Make Uppercase', 'analyzed_text':djtext.upper()}
            return render(request, 'analyze.html', param)

    elif space_remover == "on":
        analyzed= " "
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1] ==" "):
                analyzed= analyzed + char

        param = {'purpose': 'removed punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)




    else:
        return  HttpResponse("error")