from setuptools import setup

setup(
    name="span",
    version="0.0.1",
    description="Helper for determining basic relationships between datetime ranges",
    long_description="Helper for determining basic relationships between datetime ranges",
    keywords="span, datetime",
    author="Jared Morse <jared@appointlet.com>",
    author_email="jared@appointlet.com",
    url="https://github.com/appointlet/span",
    license="BSD",
    packages=["span"],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
