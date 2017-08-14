from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "string14" : get_random_string(length=14)
    }
    return render(request, 'randoword/index.html', context)

def makenewword(request):
    if request.method == "POST":
        print "post it is"
        request.session['string14'] = get_random_string(length=14)

        if 'count' in request.session:
            request.session['count'] += 1
        else:
            request.session['count'] = 1
        print request.session['string14']
        return redirect('/')



def reset(request):
    try:
        del request.session['string14']
        request.session['count'] = 0
    # this try except is needed just in case the key doesn't exist!
        return redirect('/random_word/')
    except:
        return redirect('/random_word/')
