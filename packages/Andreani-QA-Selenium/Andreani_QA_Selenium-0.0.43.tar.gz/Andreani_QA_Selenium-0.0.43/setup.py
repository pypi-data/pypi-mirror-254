import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.43'
PACKAGE_NAME = 'Andreani_QA_Selenium'  # Debe coincidir con el nombre de la carpeta
AUTHOR = 'AndreaniTesting'
AUTHOR_EMAIL = 'user_appglatest@andreani.com'
URL = ''

LICENSE = 'MIT'  # Tipo de licencia
DESCRIPTION = 'SeleniumFramework para ejecución de casos automatizados'  # Descripción corta
LONG_DESCRIPTION = ""
LONG_DESC_TYPE = "text/markdown"

# Paquetes necesarios para que funcione la librería. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'allure-behave', 'allure-pytest', 'allure-python-commons', 'Andreani-QA-Parameters',
    'Andreani-QA-Functions', 'Andreani-QA-Debugger', 'Andreani-QA-Api', 'requests', 'selenium==4.16.0',
    'webdriver_manager', 'pywin32', 'humanize==4.3.0', 'loguru==0.6.0', 'numpy==1.23.2', 'opencv_python==4.6.0.66',
    'Pillow==9.2.0', 'PyAutoGUI==0.9.53', 'pyperclip'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
