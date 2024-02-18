from setuptools import setup, find_packages

# noinspection PyPackageRequirements
setup(
    name='dj-mpesa-payment',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Django',
        'django-phonenumber-field',
        'phonenumbers',
        'python-dateutil',
        'requests'
    ],
)
