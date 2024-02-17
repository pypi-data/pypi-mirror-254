from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cpanel_xss_2023',
    version='1.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdaseem03/cpanel_xss_2023",
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'cpanel_xss_2023=cpanel_xss_2023.main:main',
        ],
    },
)

