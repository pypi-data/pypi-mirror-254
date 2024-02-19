from setuptools import setup, find_packages

setup(
    name="bc_sus_columnvalidation",
    version="0.3.3",
    package_dir={"": "src"},  # Tells setuptools that packages are under src
    packages=find_packages(where="src"),
    install_requires=[
        'pandas',
        'openpyxl'
    ]
)
