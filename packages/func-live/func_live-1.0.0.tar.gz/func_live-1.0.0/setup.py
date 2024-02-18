from setuptools import setup, find_packages

setup(
    name='func_live',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description="Allows you to import and call the functions on www.func.live",
    author="Aravind Vakil",
    license="ISC",
    keywords="func.live func functions",
)
