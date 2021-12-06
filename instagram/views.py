from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import LikesForm, CommentsForm

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

def likes(request,image_id):
    likesForm = LikesForm()
    if request.method == 'POST':
        likesForm = LikesForm(request.POST)
    if likesForm.is_valid():
            form = likesForm.save(commit=False)
            form.user=request.user
            form.image= get_object_or_404(Image,pk=image_id)
            form.like= 1
            form.save()     
    obj1=Like.objects.create(user=request.user,image=get_object_or_404(Image,pk=image_id),likes=1)
    obj1.save()
    print(obj1)
    return redirect('instagramHome')

def comments(request,image_id):
    commentsForm = CommentsForm()
    if request.method == 'POST':
        commentsForm = CommentsForm(request.POST)
        if commentsForm.is_valid():
            form = commentsForm.save(commit=False)
            form.user=request.user
            form.image = get_object_or_404(Image,pk=image_id)
            form.save()
  
    return redirect('instagramHome')
