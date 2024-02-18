import setuptools

PACKAGE_NAME = "email-message-aws-ses-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.10',  # https://pypi.org/project/email-message-aws-ses-local/
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles AWS email",
    long_description="PyPI Package for Circles AWS email",
    long_description_content_type='text/markdown',
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    install_requires=["boto3>=1.28.70",
                      "logger-local>=0.0.51 ",
                      "message-local",
                      "python_sdk_remote"
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
