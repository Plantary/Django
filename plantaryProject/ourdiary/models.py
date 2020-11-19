from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Ourdiary(models.Model):
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
    
    def summary(self):
        return self.description[:50]

    @property
    #get method를 표현
    def like_count(self):
        return self.like_user_set.count()
    #좋아요 갯수를 세는 함수
    
    #approved_comments
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Like(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
   ourdiary = models.ForeignKey(Ourdiary, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   class Meta:
       unique_together = (('user', 'ourdiary'))
    

class Comment(models.Model):
    post = models.ForeignKey('ourdiary.Ourdiary', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Ourdiary, on_delete=models.CASCADE, editable=False, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

#class Comment(models.Model):
#    post = models.ForeignKey(Ourdiary, on_delete=models.CASCADE)
#    body = models.CharField('댓글', max_length=150)
#    created_at = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.body

#class Comment(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    post = models.ForeignKey(Ourdiary, on_delete=models.CASCADE)
#    content = models.TextField()

