"""Filter classes."""
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from ..models import DummyModel


class MultipleChoiceListFilter(SimpleListFilter):
    """Filter class allowing multiple filter options."""

    template = "multiselectlistfilter.html"

    def lookups(self, request, model_admin):
        """Must be overridden to return a list of tuples (value, verbose value)."""
        raise NotImplementedError(
            "The MultipleChoiceListFilter.lookups() method must be overridden to "
            "return a list of tuples (value, verbose value)."
        )

    def queryset(self, request, queryset):
        """Return queryset based on selected parameters."""
        if request.GET.get(self.parameter_name):
            kwargs = {self.parameter_name: request.GET[self.parameter_name].split(",")}
            queryset = queryset.filter(**kwargs)
        return queryset

    def value_as_list(self):
        """Convert multiple filter fields to list."""
        return self.value().split(",") if self.value() else []

    def choices(self, changelist):
        """Overriden choices method."""

        def amend_query_string(include=None, exclude=None):
            selections = self.value_as_list()
            if include and include not in selections:
                selections.append(include)
            if exclude and exclude in selections:
                selections.remove(exclude)
            if selections:
                csv = ",".join(selections)
                return changelist.get_query_string({self.parameter_name: csv})
            else:
                return changelist.get_query_string(remove=[self.parameter_name])

        yield {
            "selected": self.value() is None,
            "query_string": changelist.get_query_string(remove=[self.parameter_name]),
            "display": "All",
            "reset": True,
        }
        for lookup, title in self.lookup_choices:
            yield {
                "selected": str(lookup) in self.value_as_list(),
                "query_string": changelist.get_query_string(
                    {self.parameter_name: lookup}
                ),
                "include_query_string": amend_query_string(include=str(lookup)),
                "exclude_query_string": amend_query_string(exclude=str(lookup)),
                "display": title,
            }


class DummyModelNameFilter(MultipleChoiceListFilter):
    """Simple filter class to show records based on stt."""

    title = _("Name")

    parameter_name = "name"

    def lookups(self, request, model_admin):
        """Available options in dropdown."""
        options = list()
        objs = DummyModel.objects.all()
        for obj in objs:
            name = obj.name
            options.append((name, name))

        return options

    def queryset(self, request, queryset):
        """Return queryset of records based on stt code(s)."""
        if self.value() is not None and queryset.exists():
            names = self.value().split(",")
            queryset = queryset.filter(name__in=names)
        return queryset
