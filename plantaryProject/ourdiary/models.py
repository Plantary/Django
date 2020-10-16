from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ourdiary(models.Model):
    #ForeignKey 다대일 관계 설정(연결된 모델, 삭제시 row 자체를 삭제)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    #like_user_set field
    likes_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        blank=True, 
        related_name='like_user', 
        through='Like'
    )
    
    def summary(self):
        return self.description[:50]

    @property
    #get method를 표현
    def count_likes_user(self):
        return self.likes_user.count()
    #좋아요 갯수를 세는 함수
    


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ourdiary = models.ForeignKey(Ourdiary, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (('user', 'ourdiary'))