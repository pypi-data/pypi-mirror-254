from setuptools import setup, find_packages

setup(name='whatsapp_parse',
      license='MIT',
      version='0.1.1',
      author='Hassn Hamada',
      author_email='hassneltokhy4@gmail.com',
      description='A parsing library for WhatsApp chat logs',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=[
          'pandas'
      ],
      url='https://github.com/HassnHamada/whatsapp-chat-parser.git',
      zip_safe=False)
