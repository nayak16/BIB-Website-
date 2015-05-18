from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db.models import F
from django.core.mail import send_mail


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

    if 'name' in request.POST:
        name = request.POST['name']
    if 'organizer' in request.POST:
        organizer = request.POST['organizer']
    if 'admin' in request.POST:
        admin = request.POST['admin']
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

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
# Create your views here.
