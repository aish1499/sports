from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.
def upload_image(instance, filename):
    return f'{instance.user}/{filename}'

def upload(instance, filename):
    return f'{instance.caption}/{filename}'

class Players(models.Model):
    caption = models.CharField(_("caption"), max_length=50,blank=True,null=True)
    image = models.ImageField(_("Image"), upload_to=upload, height_field=None, width_field=None, max_length=None)

class Message(models.Model):
    user = models.CharField(_("User"), max_length=100,blank=True,null=True)
    post = models.ForeignKey(Players, verbose_name=_("Post"), on_delete=models.CASCADE,blank=True,null=True)
    photo = models.ImageField(_("Photo"), upload_to=upload_image,blank=True,null=True)
    message= models.TextField(_("Message"),blank=True,null=True)



   
    def __str__(self):
        return self.user
