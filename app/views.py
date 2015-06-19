from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db.models import F
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


from validate_email import validate_email
import smtplib

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
    print request.POST
    if 'name' in request.POST:
        name = request.POST['name']
    else:
        context['failure'] = "Please fill out all fields"

    if 'email' in request.POST:
        email = request.POST['email']
    else:
        context['failure'] = "Please fill out all fields"

    if 'subject' in request.POST:
        subject = request.POST['subject']
    else:
        context['failure'] = "Please fill out all fields"

    if 'message' in request.POST:
        msg = request.POST['message']
    else:
        context['failure'] = "Please fill out all fields"    

    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("bhangraintheburgh@gmail.com", "SHINEforBIB9")
        message = 'Subject: %s\n\n%s' % (subject, msg)
        server.sendmail("bhangraintheburgh@gmail.com", email, message)
        server.quit()
    except Exception as e:
        context['failure'] = "Oops Something went wrong"
        print e

    if not ('failure' in context):
        context['success'] = "Thanks! We'll get back to you soon!"

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
