from setuptools import setup, find_packages

setup(
    name='request_response_logging',
    version='0.0.5',
    author='Pravin Tiwari',
    author_email='pravint198@gmail.com',
    description='Django logger to log request response',
    long_description='This logs request and response and also helps in generating request_id for each execution',
    packages=find_packages(),
    install_requires=['simplejson'],
    python_requires='>=3.7'
)