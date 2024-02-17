# django-staff-view

Generic non-model related admin views for Django.

## Rationale

Define admin views for Django admin not tied to a ModelAdmin.

## Support

Supports: Python 3.10.

Supports Django Versions: 4.2.9

## Installation

```shell
$ pip install django-staff-view
```

## Usage

Add `staff_views` to `INSTALLED_APPS`.

Import the view class from the package, and subclass it like this:

```python
from django import forms
from staff_view.views import StaffView


class MyForm(forms.Form):
    
    text = forms.CharField()
    
    
class MyView(StaffView):

    form_class = MyForm

    def form_valid(self, form):
        ...  # Return a response object
```