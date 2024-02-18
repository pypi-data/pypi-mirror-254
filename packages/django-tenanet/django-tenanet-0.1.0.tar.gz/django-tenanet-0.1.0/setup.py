from setuptools import setup, find_packages

setup(
    name='django-tenanet',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='Custom License: Django-Tenanet Limited Use License',
    description='A Django app for multi-tenancy.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rsjsoc/django-tenanet',
    author='He0468',
    author_email='rsjsoc@gmail.com',
    install_requires=[
        'Django>=4.0',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
