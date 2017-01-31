from setuptools import setup

setup(name='Tzara---A-Personal-Assistant',
      version='0.1',
      description='A Virtual Personal Assistant',
      url='https://github.com/Suman7495/Tzara---A-Personal-Assistant',
      author='Suman Pal',
      author_email='suman7495@gmail.com',
      license='MIT',
      packages=['tzara'],
      scripts=['bin/startup.sh']
      install_requires=[
            'gtts',
            'mpg123',
            'nltk',
            'firefox',
            'audacious',
            'wmctrl',
            'guake',
            'xdg-utils',
      ],
      include_package_data=True,
     )
