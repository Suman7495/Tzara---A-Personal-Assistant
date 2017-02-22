from setuptools import setup
from setuptools.command.install import install
import os

class MyInstall(install):
    def run(self):
        install.run(self)
        path = os.getcwd().replace(" ", "\ ").replace("(","\(").replace(")","\)") + "/bin/"
        os.system("echo 'Setting up Tzara.desktop'")
        os.system("chmod +x "+path+"desktopsetup.sh")
        os.system("bash "+path+"desktopsetup.sh")
        os.system("chmod +x "+path+"startup.sh")
        os.system("sh "+path+"startup.sh")
        

setup(name='Tzara---A-Personal-Assistant',
      version='1.0.4',
      description='A Virtual Personal Assistant',
      url='https://github.com/Suman7495/Tzara---A-Personal-Assistant',
      author='Suman Pal',
      author_email='suman7495@gmail.com',
      license='MIT',
      packages=['tzara'],
      classifiers=['Development Status :: 4 - Beta',
      'Programming Language :: Python :: 2.7',            
      ],
      scripts=['bin/startup.sh', 'bin/desktopsetup.sh'],
      cmdclass={'install': MyInstall},
     )
