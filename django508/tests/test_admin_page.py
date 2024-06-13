from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase
from django.test import RequestFactory
from django.test import Client
import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from django.contrib.admin import SimpleListFilter


class MockSuperUser:
    def has_perm(self, perm):
        return True

    def is_active(self):
        return True

    def is_staff(self):
        return True


class CustomListFilter(SimpleListFilter):
    title = "custom filter"
    parameter_name = "is_staff"

    def lookups(self, request, model_admin):
        return (
            ("1", "Yes"),
            ("0", "No"),
        )

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_staff=True)
        if self.value() == "0":
            return queryset.filter(is_staff=False)


class CustomListFilterAdmin(AdminSite):
    def get_filters_params(self, request):
        return {"is_staff": "10"}


class TestAdminPage:
    def setup(self):
        User.objects.create_superuser(username="john", password="smith")
        call_command("loaddata", "users")

    @pytest.mark.django_db
    def test_admin_page(self):
        self.client = Client()
        response = self.client.post(
            "/admin/login/", {"username": "john", "password": "smith"}
        )
        response = self.client.get("/admin/auth/user/")
        assert response.status_code == 200
        assert b"testuser1" in response.content

        response = self.client.get("/admin/auth/user/?is_staff__exact=1")
        assert b"testuser1" not in response.content
        assert b"Clear all filters" in response.content
        assert (
            b'<option selected value="?is_staff__exact=1">Yes</option>'
            in response.content
        )

    @pytest.mark.django_db
    def test_simple_list_filter(self):
        """
        Test a custom filter based on SimpleListFilter class
        """
        assert User.objects.count() == 40

        request = RequestFactory().get("/admin/auth/user/")
        request.user = MockSuperUser()
        request.session = {}
        request._messages = FallbackStorage(request)
        request.user = User.objects.get(username="john")
        model_admin = CustomListFilterAdmin()
        custom_list_filter = CustomListFilter(
            request, {"is_staff": "1"}, model=User, model_admin=model_admin
        )

        custom_list_filter.queryset(request, User.objects.all())

        assert custom_list_filter.title == "custom filter"
        assert custom_list_filter.parameter_name == "is_staff"
        assert custom_list_filter.lookups(request, model_admin) == (
            ("1", "Yes"),
            ("0", "No"),
        )
        assert custom_list_filter.queryset(request, User.objects.all()).count() == 1
        assert (
            custom_list_filter.queryset(request, User.objects.all())[0].username
            == "john"
        )

        custom_list_filter = CustomListFilter(
            request, {"is_staff": "0"}, model=User, model_admin=model_admin
        )
        assert custom_list_filter.queryset(request, User.objects.all()).count() == 39
