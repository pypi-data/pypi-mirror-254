from setuptools import setup, find_packages

setup(
    name='dLogpy',
    version='0.0.5',
    packages=find_packages(),
    install_requires=[
    ],
    author='Vos',
    author_email='your.email@example.com',
    description="""Compact logger for Python 3.10+""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dim-4/dLog',  # your repo link
    classifiers=[
        # Classifiers to indicate who your project is intended for, what it does, etc.
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
