from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class PracticeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(material_type='practice')


class Material(models.Model):

    MATERIAL_TYPE = (('административное','Административное право'),
                     ('уголовное','Уголовное право'),
                     ('исполнительное','Исполнительное производство')
                     )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique='publish')
    body = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    publish = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_materials')

    material_type = models.CharField(max_length=20,
                                     choices=MATERIAL_TYPE,
                                     default='административное')
    objects = models.Manager()
    practice = PracticeManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:material_details',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    material = models.ForeignKey(Material,
                                 on_delete=models.CASCADE,
                                 related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to="user/%Y/%m/%d/", blank=True)

    def __str__(self):
        return '{} profile'.format(self.user.first_name)
