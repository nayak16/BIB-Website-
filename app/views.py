from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db.models import F
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


from validate_email import validate_email


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

# Renders home page with confirmation of email sent
def contact(request):
    assert isinstance(request, HttpRequest)
    context = {}
    name = ""
    email = ""
    subject = ""
    msg = ""
    if 'name' in request.POST:
        name = request.POST['name']
    else:
        context['failure'] = "Please fill out all fields"

    if 'email' in request.POST:
        email = request.POST['email']
    else:
        context['failure'] = "Please fill out all fields"

    if 'name' in request.POST:
        subject = request.POST['subject']
    else:
        context['failure'] = "Please fill out all fields"

    if 'name' in request.POST:
        msg = request.POST['message']
    else:
        context['failure'] = "Please fill out all fields"    

    if validate_email(email):
        context['success'] = "Thanks for your message! We'll get back to you soon."
    else:
        context['failure'] = "Sorry not a valid email address"
    
    return render(request,'app/index.html',context)


def board(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/board.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def tickets(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tickets.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def teams(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/teams.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

@csrf_exempt
def posttest(request):
    print "MADE IT---------"
    html = """<!DOCTYPE html> 
            <html>
            <body>
                <h1>My First Heading</h1>
                <p>My first paragraph.</p>
            </body>
            </html>
            """
    return render(
        request,'app/teams.html')
# Create your views here.
