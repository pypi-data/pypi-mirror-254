import os

from setuptools import setup, find_packages

locale = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(locale, "falu", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version)

setup(
    name='falu',
    version=version["VERSION"],
    description='The official Falu Python library',
    long_description=open("long_description.rst").read(),
    long_description_content_type="text/x-rst",
    url='https://github.com/faluapp/falu-python',
    author='Falu',
    author_email='support@falu.io',
    keywords=["falu api payments"],
    zip_safe=False,
    license='MIT',
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "pytest>=7.0.0",
        'requests >= 2.20; python_version >= "3.0"',
        'responses >=0.23',
        "urllib3 >= 1.26.14",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=["wheel"],
)
