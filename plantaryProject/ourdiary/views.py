from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ourdiary
from django.contrib.auth.decorators import login_required # post_like함수가 실행될려면 먼저 로그인이 되어야 함

import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST

#댓글
from .forms import CommentForm
from .models import Comment

#from django import forms


# Create your views here.
def ourdiary(request):
    ourdiarys = Ourdiary.objects
    current_user = request.user
    return render(request, 'ourdiary.html', {'ourdiarys':ourdiarys, 'current_user':current_user}) #'current_user':current_user

def detail(request, ourdiary_id):
    ourdiary_detail = get_object_or_404(Ourdiary, pk=ourdiary_id)
    current_user = request.user
    return render(request, 'detail.html', {'ourdiary':ourdiary_detail, 'current_user':current_user})

@login_required #post_like함수가 실행될려면 먼저 로그인이 되어야 함. 
@require_POST #post request만 받기
def post_like(request):
    pk = request.POST.get('pk', None)
    ourdiary = get_object_or_404(Ourdiary, pk=pk)
    user = request.user

    if ourdiary.like_user_set.filter(id=user.id).exists():
        ourdiary.like_user_set.remove(user)
        message = '좋아요 취소'
    else:
        ourdiary.like_user_set.add(user)
        message = '좋아요'
    
    context = {'like_count':ourdiary.like_count, 'message':message, 'username':user.username} #에러가 이유 -> int형으로 바꿔줘야 함. 그런데 ourdiary.likes_count()가 함수라서 안된거임.
    return HttpResponse(json.dumps(context), content_type="application/json")

#comment
def add_comment(request, pk):
   #post
    post = get_object_or_404(Ourdiary, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', ourdiary.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', ourdiary.pk)



#로그인이 되어야 댓글달 수 있도록(다른 comment)
#@require_POST
#def comment_create(request, ourdiary_id):
#    post = get_object_or_404(Ourdiary, id=ourdiary_id)
#    comment_form = CommentForm(request.POST)
#    if comment_form.is_valid():
#        comment = comment_form.save(commit=Fasle)
#        comment.user = request.user
#        comment.post_id = post_id
#        comment.save()
#        return redirect('detail', ourdiary_id)
#    else:
#        form = CommentForm()
#    return render(request, 'add_comment.html', {'form':form})

#def list(request):
#    ourdiarys = Ourdiary.objects.order_by('-id').all()
#    comment_form = CommentForm()
#    return render(request, 'ourdiarys/list.html', {'ourdiarys':ourdiarys, 'comment_form':comment_form})