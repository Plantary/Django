from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ourdiary(models.Model):
    # objects = models.Manager()
    #ForeignKey 다대일 관계 설정(연결된 모델, 삭제시 row 자체를 삭제)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    #like_user_set는 모델과 다대다관계를 형성
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        blank=True, 
        related_name='like_user_set', 
        through='Like'
    )
    


    @property
    #get method를 표현
    def like_count(self):
        return self.like_user_set.count()
    #좋아요 갯수를 세는 함수
    


class Like(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ourdiary = models.ForeignKey(Ourdiary, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   class Meta:
       unique_together = (('user', 'ourdiary'))

class Photo(models.Model):
    blog = models.ForeignKey(Ourdiary, on_delete = models.CASCADE, null = True)
    image = models.ImageField(upload_to='images/',blank = True, null = True)

    