from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from .models import Movies
from django.core.mail import send_mail

@receiver(post_delete, sender=Movies)
def notify_admin(**kwargs):
    instance = kwargs.get('instance')
    print(instance)
    send_mail(
        subject='Movie deleted',
        message='dear user {} is deleted'.format(instance.name),
        from_email='tony.samir53@mail.com',
        recipient_list=['antonsamirabdu@gmail.com', 'tony.samir53@gmail.com'],
        fail_silently=False
    )

# @receiver(post_save, sender=Movies)
# def my_handler(sender, instance, created, *args, **kwargs):
#     if created:
#         send_mail(
#             subject='New Movie',
#             message='dear user {}'.format(instance.name),
#             from_email='tony.samir53@mail.com',
#             recipient_list=['antonsamirabdu@gmail.com', 'tony.samir53@gmail.com'],
#             fail_silently=False
#         )
