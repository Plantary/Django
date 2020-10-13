from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ourdiary
from django.contrib.auth.decorators import login_required # post_like함수가 실행될려면 먼저 로그인이 되어야 함
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
def ourdiary(request):
    ourdiarys = Ourdiary.objects
    current_user = request.user
    return render(request, 'ourdiary.html', {'ourdiarys':ourdiarys, 'current_user':current_user}) #'current_user':current_user

def detail(request, ourdiary_id):
    ourdiary_detail = get_object_or_404(Ourdiary, pk=ourdiary_id)
    return render(request, 'detail.html', {'ourdiary':ourdiary_detail})

@login_required #post_like함수가 실행될려면 먼저 로그인이 되어야 함. 
@require_POST #post request만 받기
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Ourdiary, pk=pk)
    #중간자 모델 Like를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져옴.
    #post_like, post_like_created = post.like_set.get_or_create(user=request.user)
    user = request.user

    if post.likes_user.filter(id=user.id).exists():
        post.likes_user.remove(user)
        message = '좋아요 취소'
    else:
        post.likes_user.add(user)
        message = '좋아요'
    
    context = {'likes_count':post.count_likes_user(), 'message':message}
    return HttpResponse(json.dumps(context), content_type="application/json")

    #if not post_like_created:
    #    post_like.delete()
    #    return redirect('/ourdiary/'+str(post.id))
    #return redirect('/ourdiary/'+str(post.id))