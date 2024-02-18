from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='alegriadb',
    version='0.0.3',
    license='MIT License',
    author='HappyBoyJF',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='joseprogfisica@gmail.com.br',
    keywords='django-alegriadb',
    description=u'Just a test',
    packages=[],
    install_requires=['django','requests'],)