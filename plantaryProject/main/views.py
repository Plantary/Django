from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    #모델.쿼리셋(objects).메소드