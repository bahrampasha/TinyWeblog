from django.db import models
from django.utils import timezone
from django.urls import reverse




# Create your models here.



class post(models.Model):
    author = models.ForeignKey ('auth.user')
    title = models.CharField(max_length= 50)
    text = models.TextField ()
    created_date = models.DateTimeField(deafult = timezone.now())
    published_date = models.DateTimeField(blank=True , null = True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def aprrove_comments (self):
        return self.comments.filter(approved_comments = True)
    
    def __str__ (self):
        return self.title
    
    def get_absoloute_url (self):
        return reverse ("post_detail",kwargs ={'pk':self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField (default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)





