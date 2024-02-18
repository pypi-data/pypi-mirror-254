from setuptools import setup, find_packages
 
# classifiers = [
#   'Development Status :: 5 - Production/Stable',
#   'Intended Audience :: Education',
#   'Operating System :: Microsoft :: Windows :: Windows 10',
#   'License :: OSI Approved :: MIT License',
#   'Programming Language :: Python :: 3'
# ]
 
setup(
  name='run_my_monitoring_dashboard',
  version='0.0.1',
  description='A very basic monitoring package',
  # long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  # url='',  
  author='Ritik Saxena',
  author_email='ritiksaxena90@gmail.com',
  # license='MIT', 
  # classifiers=classifiers,
  keywords='package', 
  packages=find_packages(),
  install_requires=['pandas','streamlit','datetime','numpy'] 
)