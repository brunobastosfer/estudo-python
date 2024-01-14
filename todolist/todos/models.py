from django.db import models
from django.conf import settings


class Todo(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title