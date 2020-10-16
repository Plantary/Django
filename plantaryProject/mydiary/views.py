from django.shortcuts import render, redirect, get_object_or_404
from .models import Diary

def create(request):
    return render(request,'create.html')

def myhome(request):
    diarys = Diary.objects.all()
    return render(request, 'myhome.html', {'diarys': diarys})

def write(request):
    if request.method == "POST":
        diary = Diary()
        if 'image' in request.FILES:
            diary.image = request.FILES['image']
        diary.title = request.POST['title']
        diary.description = request.POST['description']

        diary.save()

        return redirect('detail', diary.id)

def detail(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'detail.html', {'diary':diary})

def delete(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)
    diary.delete()

    return redirect ('myhome')

def update(request, diary_id):
    diary = get_object_or_404(Diary, pk = diary_id)

    if request.method == "POST":
        if 'image' in request.FILES:
            diary.image = request.FILES['image']
        diary.title = request.POST['title']
        diary.description = request.POST['description']

        diary.save()

        return redirect('detail', diary.id)    

    else:
        return render(request, 'update.html', { 'diary' : diary })