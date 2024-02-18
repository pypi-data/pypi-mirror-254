from django.db import models

class AppsToVerifyModel(models.Model):
    name = models.CharField(max_length=400)
    db_external_name = models.CharField(max_length=400, blank=True, null=True)
    should_verify = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class RedirectEmail(models.Model):
    email = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.email}'


class Verified(models.Model):
    data = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    