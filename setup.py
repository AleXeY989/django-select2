
from setuptools import setup

setup(
    name='django-select2',
    version='3.5.0',
    url='https://github.com/AleXeY989/django_select2.git',
    description='Django package for django-select2: Select2 is a jQuery based replacement for select boxes. It supports searching',
    author='Igor Vaynberg',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'select2'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_select2'],
    package_data={'django_select2': ['static/django_select2/js/*.js', 'static/django_select2/img/*.png', 'static/django_select2/img/*.gif', 'static/django_select2/css/*.css']}
)
