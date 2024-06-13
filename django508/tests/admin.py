from django.contrib import admin
from .filters import DummyModelNameFilter
from .models import DummyModel, DummyModel2


class ReadOnlyDummyMixin(admin.ModelAdmin):
    """Force ModelAdmin to be READ only."""

    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        """Force all fields to read only."""
        return (
            list(self.readonly_fields)
            + [field.name for field in obj._meta.fields]
            + [field.name for field in obj._meta.many_to_many]
        )

    def has_add_permission(self, request):
        """Deny add permisison."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Deny delete permission."""
        return False


class Dummy_Admin(ReadOnlyDummyMixin):
    """ModelAdmin class for parsed M1 data files."""

    list_display = [
        "name",
        "description",
        "created",
        "updated",
        "user",
    ]

    list_filter = [
        DummyModelNameFilter,
    ]


admin.site.register(DummyModel, Dummy_Admin)
