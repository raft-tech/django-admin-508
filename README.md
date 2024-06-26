
[![](https://img.shields.io/pypi/pyversions/django-admin-508.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/pypi/djversions/django-admin-508?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)

[![](https://img.shields.io/pypi/v/django-admin-508.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-admin-508/)
[![](https://img.shields.io/pypi/l/django-admin-508.svg?color=blue)](https://github.com/raft-tech/django-admin-508/blob/main/LICENSE.txt)

# django-admin-508

`django-admin-508` is a responsive interface that aims to be accessible to the 508 Standard.

## Features

## Installation

- Run `pip install django-admin-508`
- Add `admin_interface`, `flat_responsive`, `flat` and `colorfield` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`

```python
INSTALLED_APPS = (
    #...
    'admin_interface',
    'flat_responsive',  # only if django version < 2.0
    'flat',             # only if django version < 1.9
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
- Restart your application server

#### Upgrade

- Run `pip install django-admin-508 --upgrade`
- Restart your application server

## Publishing Updates

https://packaging.python.org/tutorials/packaging-projects/
https://realpython.com/installable-django-app/

```
python3 -m pip install --upgrade build
python3 -m build


python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```


## local development
In local development, the package has a parallel django508 application that can be started using Task file. The application has the admin_interface as one of the listed apps, so when started, the admin_interface project is automatically added.


To list the available commands, run ```task help```. A django server can be started using ```task up``` command. 

### Running pytest
Pytest test files can be ran using: ```task test```. If you need to add pytest command line option, you may do so using ```PYTEST_ARGS``` variable. E.g: ```task test  PYTEST_ARGS="./tests/test_models.py -s -vv"```

## License
Released under [MIT License](LICENSE.txt).

## See also

This project started out as a fork of the excellent [Django Admin Interface](https://github.com/fabiocaccamo/django-admin-interface).
