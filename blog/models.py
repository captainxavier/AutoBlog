from django.db import models
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from datetime import datetime  
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from comments.models import Comments
from category.models import Category


def upload_location(instance, filename):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id),title=str(instance.title), filename=filename)
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    thumbnail = models.ImageField(upload_to=upload_location, null=True, blank=True, max_length=500)
    caption = RichTextField(null=True,blank=False,max_length=300,default='')
    description_one = RichTextField(null=True, blank=False, default='')
    description_two = RichTextField(null=True, blank=False, default='')
    description_three = RichTextField(null=True,blank=False, default='')
    blogPicture = None
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published",blank = True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated",blank = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    super_featured = models.BooleanField()
    featured = models.BooleanField()
    slug = models.SlugField(blank=True, unique=True)
    categories = models.ManyToManyField(Category)

    tags = TaggableManager(blank=True)


    class Meta:
        db_table = 'blog_posts'
        verbose_name = ("BlogPost")
        verbose_name_plural = ("BlogPosts")



    def __str__(self):
        return self.title

    def get_absolute_url(self):       
        return reverse('single_post', kwargs={'slug': self.slug})

    @property
    def comments(self):
        instance = self
        qs = Comments.objects.filter_by_instance(instance).order_by('-time_stamp')
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    @property
    def get_pictures(self):
        return self.pictures.all()



def upload_location_blog_pics(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images_<id>/<filename>
    file_path = 'blogImages/{blog_post}/{blog_post}-{filename}'.format(author_id=str(instance.blog_post.id),blog_post=str(instance.blog_post), filename=filename)
    return file_path



@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.thumbnail.delete(False) 
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=BlogPost)


class BlogPicture(models.Model):
    picture = models.ImageField(upload_to=upload_location_blog_pics, null=True, blank=True, max_length=500)
    blog_post = models.ForeignKey(BlogPost, related_name='pictures', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = ("Picture")
        verbose_name_plural = ("Pictures")

    def __str__(self):
            return self.blog_post.slug

    def get_absolute_url(self):
        return reverse("blog_picture", kwargs={"pk": self.pk})



