import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
   name="pyaconf",
   version="0.3.0",
   author="ikh software, inc.",
   author_email="ikh@ikhsoftware.com",
   description="Yet another config library that is built around python dict and supports native python dicts, json, yaml, ini",
   long_description=long_description,
   long_description_content_type="text/x-rst",
   url="https://bitbucket.org/ikh/pyaconf",
   packages=setuptools.find_packages(),
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
   ],
   python_requires = '>= 3.7',
   install_requires=[
      'pyyaml == 5.1.*',
   ],
   project_urls={
        'Bug Reports': 'https://bitbucket.org/ikh/pyaconf/issues',
   },
)

