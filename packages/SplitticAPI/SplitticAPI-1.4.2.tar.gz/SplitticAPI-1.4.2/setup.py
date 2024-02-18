from setuptools import setup, find_packages
with open("README.rst", encoding='utf8') as f:
    long_description = f.read()

setup(
    name='SplitticAPI',
    author='CutyCat2000',
    license='MIT',
    url='https://github.com/Mike-FreeAI/splitticapi',
    version='1.4.2',
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'httpx',
        'Pillow',
        'requests',
    ],
    description='A Python wrapper for the SplitticAPI',
    long_description=long_description,
    long_description_content_type='text/x-rst',
)
