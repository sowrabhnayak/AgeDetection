from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="Age Detection",
    long_description=readme,
    author_email='nayaksowrabh40@gmail.com',
    url='https://github.com/sowrabhnayak/AgeDetection',
    license=license,
    packages=find_packages()
)
