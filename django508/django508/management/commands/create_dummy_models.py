import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django508.models import DummyModel, DummyModel2


class Command(BaseCommand):
    help = "Creates a myriad of DummyModels."

    def handle(self, *args, **options):
        User = get_user_model()

        d_names = ["Joe", "Bill", "Jane", "Diane"]
        d2_names = ["Bob", "John", "Jill", "Jessica"]
        admin_user = User.objects.get(username='admin')
        for n1, n2 in zip(d_names, d2_names):
            DummyModel.objects.create(name=n1, description="", user=admin_user)
            DummyModel2.objects.create(name=n2, description="", user=admin_user)
