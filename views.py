from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    #CheckBox Values.

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capitialize = request.POST.get('capitialize', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover =request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount','off')

    # Check with Checkbox values is on or not.

    if removepunc == "on":
        punctuations = '''<>.,:;?()![]/-''""...@$#%^&*'''
        analyzed =""
        for char in djtext :
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed


    if capitialize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed


    if lowercase =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'LowerCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !='\n'and char !='\r':
                    analyzed = analyzed + char
        params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount=="on":
        analyzed=""
        params = {'purpose': 'CharacterCount', 'analyzed_text': len(djtext)}

    if(removepunc!='on' and newlineremover!='on'and charcount!='on' and lowercase!='on' and capitialize!='on'):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)
