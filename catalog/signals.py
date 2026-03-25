import os 
from django.db.models.signals import *
from django.dispatch import receiver

from .models import Movie

@receiver(post_delete,sender=Movie )
def delete_movie(sender,instance,**kwargs):
    if instance.imge:
        if os.path.isfile(instance.path):
            os.remove(instance.image.path)
            
    if instance.trailir_video:
        if os.path.isfile(instance.trailir_video.path):
            os.remove(instance.trailir_vidio.path)
        
        
@receiver(post_save, sender = Movie )
def create_movie(sender,instance,created,**kwargs):
    if created:
        print(f"Создан фильм {instance.title}")
    else:
        print(f"Обновлен фильм {instance.title}")