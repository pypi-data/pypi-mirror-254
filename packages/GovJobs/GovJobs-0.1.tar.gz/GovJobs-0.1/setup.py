from setuptools import setup, find_packages

setup(
    name='GovJobs',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'asgiref==3.7.2',
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'Django>=3.2,<4.0',
        'django-bootstrap3==23.6',
        'docopt==0.6.2',
        'idna==3.6',
        'pipreqs==0.4.13',
        'psycopg==3.1.17',
        'psycopg2-binary==2.9.9',
        'requests==2.31.0',
        'sqlparse==0.4.4',
        'typing_extensions==4.9.0',
        'urllib3==2.1.0',
        'yarg==0.1.9',
    ],
)
