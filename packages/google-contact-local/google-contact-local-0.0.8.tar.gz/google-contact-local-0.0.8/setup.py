import setuptools

PACKAGE_NAME = "google-contact-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name='google-contact-local',
    version='0.0.8',  # https://pypi.org/project/google-contact-local
    author="Circles",
    author_email="valeria.e@circ.zone",
    description="PyPI Package for Circles google-contact-local Python",
    long_description="PyPI Package for Circles google-contact-local Python",
    long_description_content_type="text/markdown",
    url="https://github.com/circles-zone/google-contact-local-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'user-context-remote>=0.0.17',
        'python-sdk-local>=0.0.27',
        'importer-local>=0.0.36',
        'entity-type-local>=0.0.13',
        'url-remote>=0.0.65',
    ]
 )
