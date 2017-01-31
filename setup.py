from setuptools import setup

setup(name='tzara',
      version='0.1',
      description='A Virtual Personal Assistant',
      url='https://github.com/Suman7495/Tzara---A-Personal-Assistant',
      author='Suman Pal',
      author_email='suman7495@gmail.com',
      license='MIT',
      packages=['tzara'],
      install_requires=[
            'gtts',
            'mpg123',
            'nltk',
            'firefox',
            'audacious',
            'wmctrl',
            'guake',
            'xdg-utils',]
     )
