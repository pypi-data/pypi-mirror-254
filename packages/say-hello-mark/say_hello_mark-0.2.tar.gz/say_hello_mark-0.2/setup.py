from setuptools import setup, find_packages

setup(
  name="say_hello_mark",
  version="0.2",
  packages=find_packages(),
  install_requires=[

  ],
  entry_points={
    "console_scripts": [
      "say_hello_mark = say_hello_mark:hello" 
    ]
  }
)