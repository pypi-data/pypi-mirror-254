from setuptools import setup, find_packages


def get_long_description():
    with open('README.md') as f:
        return f.read()


setup(
    name='varcache',
    version="0.1.0",
    author='Alexander Khlebushchev',
    packages=find_packages(),
    license="MIT",
    zip_safe=False,
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
)
