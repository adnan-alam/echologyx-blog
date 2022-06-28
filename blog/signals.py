from django.db.models import signals
from django.dispatch import receiver
from .models import CustomTemplate


@receiver(signals.post_save, sender=CustomTemplate)
def on_create_custom_template(sender, instance, created, **kwargs):
    if created:
        CustomTemplate.objects.exclude(id=instance.id).update(is_active=False)
