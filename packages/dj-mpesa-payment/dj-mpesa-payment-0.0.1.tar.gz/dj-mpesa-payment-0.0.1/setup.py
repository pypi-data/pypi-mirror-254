from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dj-mpesa-payment',
    version='0.0.1',
    author='Elijah Onduso',
    description='Mpesa payment gateway',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='zeffah.elly@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Django',
        'django-phonenumber-field',
        'phonenumbers',
        'python-dateutil',
        'requests',
        'djangorestframework'
    ],
)
