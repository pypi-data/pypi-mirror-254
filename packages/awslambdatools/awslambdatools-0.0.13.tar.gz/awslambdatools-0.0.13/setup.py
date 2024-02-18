from setuptools import setup

setup(name='awslambdatools',
      version="0.0.13",
      description='Package for dealing with lambdas running on Python',
      author='Edward Velo',
      author_email='vattico@gmail.com',
      packages=['awslambdatools'],
#      install_requires=['boto3'],
      python_requires='>=3.6')