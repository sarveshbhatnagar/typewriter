from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = ['time'] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers', 
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python', 
    ] 
  
# calling the setup function  
setup(name='typewriter',
      version='1.0.0',
      description='Program with multiple ways to print output on your console!',
      long_description=long_description,
      long_description_content_type='text/markdown',
      py_modules = ["typewriter"],
      url='https://github.com/sarveshbhatnagar/typewriter',
      author='Sarvesh Bhatnagar', 
      author_email='sarveshbhatnagar08@gmail.com', 
      license='MIT', 
      packages=find_packages(),
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='typewriter print console type write'
      ) 