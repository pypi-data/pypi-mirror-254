from setuptools import setup, find_packages

setup(
    name='zonotify',
    version='1.0.5',
    author='Siddhant',
    author_email='siddhant@zodevelopers.com',
    description='A simple package for sending notifications to Discord and Email in two lines.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SidmoGoesBrrr/Zonotify',
    packages=find_packages(),
    install_requires=[
        'requests',
        'webcolors',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
