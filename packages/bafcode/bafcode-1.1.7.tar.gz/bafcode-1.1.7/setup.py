from setuptools import setup, find_packages

setup(
    name="bafcode",
    version="1.1.7",
    packages=find_packages(),
    install_requires=[
    'cryptography', 
    'requests',
    'Flask',
    'python-dotenv',
    'openai',
    ],
    entry_points={
        'console_scripts': [
            'bafcode = cli.main:main'
        ]
          },
     author="Imad Ait El Arabi",
     author_email="business@aitelabranding.com",
     description="BafCode Framework CLI",
     long_description=open('README.md').read(),
     long_description_content_type='text/markdown',
     url="https://github.com/aitelabranding/bafcode_cli",
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        ],
  
)

