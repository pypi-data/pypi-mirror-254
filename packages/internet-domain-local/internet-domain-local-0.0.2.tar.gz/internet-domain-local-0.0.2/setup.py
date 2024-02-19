import setuptools

PACKAGE_NAME = "internet-domain-local"
package_dir = PACKAGE_NAME.replace("-", "_")


setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.2',  # update only the minor version each time # https://pypi.org/project/internet-domain-local/
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles internet-domain-local Python",
    long_description="PyPI Package for Circles internet-domain-local Python",
    long_description_content_type='text/markdown',
    url="https://github.com/circles-zone/internet-domain-local-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    # TODO: Update which packages to include with this package
    install_requires=[
        'PyMySQL>=1.0.2',
        'pytest>=7.4.0',
        'mysql-connector>=2.2.9',
        'logzio-python-handler>= 4.1.0',
        'user-context-remote>=0.0.17',
        'python-sdk-local>=0.0.27'
    ],
)
