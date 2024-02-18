from setuptools import setup, find_packages

setup(
    name='pdf_converter_nixx',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'pdf2image',
        'pillow',
        'progressbar2',
        'pymupdf',
        'pymupdfb',
        'pytesseract',
        'python-utils',
        'typing_extensions',
        'flask',
        'flask-cors',
    ],
)
