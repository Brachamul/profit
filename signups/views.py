from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

# Create your views here.

from .forms import SignUpForm

def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, "Thank you, I'll tell you when everything's ready !")

    return render_to_response("signups/signup.html",
                              locals(),
                              context_instance=RequestContext(request))
