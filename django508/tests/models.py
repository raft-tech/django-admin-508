"""
Dummy models for testing purposes.
"""

from django.db import models
from django.contrib.auth.models import User


class DummyModel(models.Model):
    """Dummy model for testing purposes."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Dummy Model"
        verbose_name_plural = "Dummy Models"


class DummyModel2(models.Model):
    """Dummy model for testing purposes."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Dummy Model 2"
        verbose_name_plural = "Dummy Models 2"
