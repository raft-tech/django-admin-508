[![](https://img.shields.io/pypi/pyversions/django-admin-interface.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-admin-interface?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-admin-interface.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-admin-interface/)
[![](https://pepy.tech/badge/django-admin-interface)](https://pepy.tech/project/django-admin-interface)
[![](https://img.shields.io/github/stars/fabiocaccamo/django-admin-interface?logo=github)](https://github.com/fabiocaccamo/django-admin-interface/)
[![](https://badges.pufler.dev/visits/fabiocaccamo/django-admin-interface?label=visitors&color=blue)](https://badges.pufler.dev)
[![](https://img.shields.io/pypi/l/django-admin-interface.svg?color=blue)](https://github.com/fabiocaccamo/django-admin-interface/blob/master/LICENSE.txt)

# django-admin-508
django-admin-interface is a modern **responsive flat admin interface customizable by the admin itself**.


## Features

## Installation
- Run `pip install django-admin-508`
- Add `admin_interface`, `flat_responsive`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    'admin_interface',
    'flat_responsive', # only if django version < 2.0
    'flat', # only if django version < 1.9
    'colorfield',
    #...
    'django.contrib.admin',
    #...
)

# only if django version >= 3.0
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']
```
- Run ``python manage.py migrate``
- Run ``python manage.py collectstatic``
- Restart your application server
- Run ``python manage.py loaddata admin_interface_theme_uswds.json``

#### Upgrade
- Run `pip install django-admin-interface --upgrade`
- Run ``python manage.py migrate`` *(add* ``--fake-initial`` *if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic --clear``
- Restart your application server


## Screenshots

## Testing

## License
Released under [MIT License](LICENSE.txt).

## See also
