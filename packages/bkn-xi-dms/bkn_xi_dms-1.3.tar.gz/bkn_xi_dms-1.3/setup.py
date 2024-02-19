from setuptools import setup, find_packages

VERSION = '1.3'
DESCRIPTION = 'Document Management System (DMS) Assistan'
LONG_DESCRIPTION = 'A package that allows to Automation a process in DMS to spesific upload document'

# Setting up
setup(
    name="bkn_xi_dms",
    version=VERSION,
    author="Rifo Pangemanan (ifodigital)",
    author_email="<rifopangemanan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'openpyxl', 'PyPDF2','colorlog','colorama','logging'],
    keywords=['BKN'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
