from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyredengine',
  version='0.0.1',
  description='A simple pygame game engine',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/RedEgs/PyRedEngine',  
  author='RedEgs',
  author_email='tothemuun21@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='engine', 
  packages=find_packages(),
  install_requires=['pygame-ce', 'pytweening'] 
)
