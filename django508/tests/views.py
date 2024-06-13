"""Create views for testing django-508"""

from django.http import HttpResponse


def testadmin(request):
    return HttpResponse("test_admin")
