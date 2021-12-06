from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', locals())

#home page
@login_required(login_url='/accounts/login')
def home(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    profile = Profile.objects.all()
    likes = Like.objects.all()
    numberOfLikes = len(likes)
    comments = Comment.get_comments(id)
    comments = Comment.objects.all()
    numberOfComments=len(comments)
    commentsPerImage = Comment.objects.filter(image_id=images.id).all()
    
    
    return render(request,'instagram_pages/home.html', locals())
