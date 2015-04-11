#python first
#django second
#yourapp
#localapp

from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import SignUpForm
# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None  )
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(subject, message,from_mail, to_list, fail_silently=True)
        message = 'We have registered your email and would get back to you when we launch'
        to_list = [save_it.email,settings.EMAIL_HOST_USER]
        send_mail('Thank you for registering', message,settings.EMAIL_HOST_USER, to_list, fail_silently=False)
        messages.success(request, 'Thanks for joining')
        return HttpResponseRedirect('/thank-you/')
        
        
    return render_to_response("signup.html",locals(), context_instance=RequestContext(request))

def thankyou(request):
        
    return render_to_response("thankyou.html",locals(), context_instance=RequestContext(request))

def aboutus(request):
        
    return render_to_response("aboutus.html",locals(), context_instance=RequestContext(request))