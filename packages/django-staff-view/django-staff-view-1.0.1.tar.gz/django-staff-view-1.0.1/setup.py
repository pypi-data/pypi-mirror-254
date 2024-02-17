from setuptools import setup, find_namespace_packages
from staff_view.version import Version


setup(name='django-staff-view',
     version=Version('1.0.1').number,
     description='Staff views for Django',
     long_description=open('README.md').read().strip(),
     long_description_content_type="text/markdown",
     author='Bram Boogaard',
     author_email='padawan@hetnet.nl',
     url='https://github.com/bboogaard/django-staff-view',
     packages=find_namespace_packages(include=['staff_view', 'staff_view.templates']),
     include_package_data=True,
     install_requires=[
         'pytest',
         'pytest-cov',
         'pytest-django~=4.5.2',
         'django~=4.2.9',
         'pyquery~=2.0.0'
     ],
     license='MIT License',
     zip_safe=False,
     keywords='Django Staff views',
     classifiers=['Development Status :: 3 - Alpha'])
