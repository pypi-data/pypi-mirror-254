# your_library_name/setup.py
from setuptools import setup, find_packages

setup(
    name='doctext',
    version='0.1.9',
    packages=find_packages(),
    install_requires=['tika', 'Pillow', 'pytesseract', 'termcolor', 'python-magic', 'openai', 'chardet', 'langdetect', 'iso639-lang', 'pdfminer.six'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luckfamousa/doctext',
    author='Felix Nensa',
    author_email='felix.nensa@gmail.com'
)
