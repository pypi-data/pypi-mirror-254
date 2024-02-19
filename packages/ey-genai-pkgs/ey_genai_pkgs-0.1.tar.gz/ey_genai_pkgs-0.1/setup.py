from setuptools import setup

setup(name='ey_genai_pkgs',
      version='0.1',
      description='Generate boiler plate code from LLD docx',
      author='Rohan',
      packages=['input','pkg_lld','output'],
      zip_safe=False)