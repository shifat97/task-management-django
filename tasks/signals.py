from tasks.models import Task
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import m2m_changed


# Signals
@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
    
    if action == 'post_add':
        assigned_emails = [emp.email for emp in instance.assigned_to.all()]

        send_mail(
            'New task assigned',
            f'You have been assigned to the task: {instance.title}',
            'md.rudro1999@gmail.com',
            assigned_emails,
            fail_silently=False
        )