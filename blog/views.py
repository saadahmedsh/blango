from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import redirect
from blog.forms import CommentForm

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request):
    if request.user is active :
        if request.method == "POST" :
            comment_form = commentForm(request.POST)

            if comment_form.is_valid() :
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return render(
                    request , "blog/post-detail.html" , {"post" : post , "comment_form" : comment_form}
                )

        else :
            comment_form = commentForm()

    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )