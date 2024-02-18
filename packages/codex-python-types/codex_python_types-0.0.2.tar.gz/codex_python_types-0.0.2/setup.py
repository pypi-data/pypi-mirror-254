from setuptools import setup, find_packages

setup(
    name='codex_python_types',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'annotated-types==0.6.0',
        'pydantic==2.6.0',
        'pydantic_core==2.16.1',
        'typing_extensions==4.9.0',
    ],
)
