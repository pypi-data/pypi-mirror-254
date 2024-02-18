import setuptools

PACKAGE_NAME = "importer-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,  # https://pypi.org/project/importer-local
    version='0.0.44',
    author="Circlez",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles circles_importer Local/Remote Python",
    long_description="This is a package for sharing common importer function used in different repositories",
    long_description_content_type="text/markdown",
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'logger-local>=0.0.75',
        'database-mysql-local>=0.0.134',
        'location-local>=0.0.60',
    ],
)
