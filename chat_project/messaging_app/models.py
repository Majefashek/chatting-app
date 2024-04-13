from django.db import models
from django.contrib.auth.models import User

class PrivateMessage(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

    class Meta:
        # Specify the database for this model
        app_label = 'messaging_app'
        db_table = 'messaging_app'

