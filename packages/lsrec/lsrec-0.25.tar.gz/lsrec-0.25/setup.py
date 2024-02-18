from setuptools import setup

setup(
    name="lsrec",
    version="0.25",
    py_modules=["lsrec"],
    license="MIT",
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        lsrec=lsrec:cli
    """,
)
