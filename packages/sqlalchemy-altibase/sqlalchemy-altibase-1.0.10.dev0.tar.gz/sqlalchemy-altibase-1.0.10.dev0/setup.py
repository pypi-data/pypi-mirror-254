import os
import re

from setuptools import setup, find_packages

package = "sqlalchemy_altibase"

readme = os.path.join(os.path.dirname(__file__), "README.md")


setup(
    name="sqlalchemy-altibase",
    use_scm_version=True,
    description="Altibase for SQLAlchemy",
    long_description=open(readme).read(),
    url="https://github.com/LGUPLUS-IPTV-MSA/sqlalchemy-altibase",
    author="DataX",
    author_email="datax@lguplus.co.kr",
    license="MIT",
    classifiers=[
        # 'Development Status :: 1 - Planning',
         "Development Status :: 2 - Pre-Alpha",
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database :: Front-Ends",
        "Operating System :: OS Independent",
    ],
    keywords="SQLAlchemy Altibase",
    project_urls={
    },
    packages=find_packages(include=[package]),
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    install_requires=["odbcinst", "pyodbc", "sqlalchemy>=1.3.24, <2"],
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            f"altibase.pyodbc = {package}.pyodbc:AltibaseDialect_pyodbc",
        ]
    },
)