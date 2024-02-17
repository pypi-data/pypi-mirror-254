from setuptools import setup, find_packages

# Define your package name
PACKAGE_NAME = 'uzbekistan'

# Read the long description from your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    version='2.7.2',
    description='Full Database of Uzbekistan Regions, Districts & Quarters with Latin, Cyrillic and Russian versions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jakhongir Ganiev',
    author_email='ganiyevuzb@gmail.com',
    url='https://github.com/ganiyevuz/uzbekistan',
    packages=['uzbekistan'],
    include_package_data=True,
    install_requires=[
        'Django',
        'djangorestframework',
        'django-filter',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Choose an appropriate open-source license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='uzbekistan regions districts',
    python_requires='>=3.9',
)
