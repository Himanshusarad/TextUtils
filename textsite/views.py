# I have created this website
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed



    if (fullcaps == "on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Changed TO Uppercase', 'analysed_text': analysed}
        djtext = analysed

    if(newlineremover=="on"):
        analysed= ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analysed=analysed + char

        params = {'purpose': 'New Line Remover', 'analysed_text': analysed}
        djtext = analysed

    if (extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analysed = analysed + char
        params = {'purpose': 'New Line Remover', 'analysed_text': analysed}
        djtext = analysed
    if(charcount=="on"):
        count=0
        for char in djtext:
            count=count+1

        params = {'purpose': 'Character Count', 'analysed_text':count}
        return render(request, 'analyse.html', params)
    if(removepunc!="on"and extraspaceremover!="on" and newlineremover!="on" and charcount!="on" and fullcaps!="on"):
        return HttpResponse("Please Select Any Operation")

    return render(request, 'analyse.html', params)