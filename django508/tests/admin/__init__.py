from django.contrib import admin
from .. import models
from .dummies import Dummy_Admin, Dummy2_Admin

admin.site.register(models.DummyModel, Dummy_Admin)
admin.site.register(models.DummyModel2, Dummy2_Admin)
