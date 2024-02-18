from setuptools import setup, find_packages

setup(
    name='TXTpresso',
    version='0.1.0',
    author='Uli Hitzel',
    author_email='uli.hitzel@gmail.com',
    description='A lightweight DNS-based message broker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/TXTpresso',
    packages=find_packages(),
    install_requires=[
        'dnspython',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

