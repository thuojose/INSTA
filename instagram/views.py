from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', locals())
