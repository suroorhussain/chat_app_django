from uuid import uuid4

from django.db import models

class Conversations(models.Model):

    GROUP = 'group'
    DM = 'dm'

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField('account.User', related_name='conversations')
    type = models.CharField(max_length=255, default=DM, choices=[(GROUP, 'group'), (DM, 'dm')])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

class Messages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('account.User', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']