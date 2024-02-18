from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='Predatamaker',
    version='0.0.5',
    license='MIT License',
    author_email='gabrielqs543543@gmail.com',
    description='Ajuda na utilização de dados',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='Predatamaker',
    packages=['Predatamaker'],
    install_requires=['pandas'],
)