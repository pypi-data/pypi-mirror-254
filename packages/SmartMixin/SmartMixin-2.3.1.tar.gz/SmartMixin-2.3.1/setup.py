from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='SmartMixin',
    python_requires='>=3.10.0',
    description="""A Python library for Clash configuration file manipulation.""",
    long_description_content_type='text/markdown',
    long_description=long_description,
    author="_Fervor_",
    url="https://github.com/UFervor/SmartMixin",
    version='2.3.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyyaml',
    ],
)
