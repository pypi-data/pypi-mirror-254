import setuptools

PACKAGE_NAME = "sms-message-aws-sns-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.28',  # https://pypi.org/project/sms-message-aws-sns-local/
    author="Circles",
    author_email="info@circlez.ai",
    description="PyPI Package for Circles AWS SMS",
    long_description="PyPI Package for Circles AWS SMS",
    long_description_content_type='text/markdown',
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    install_requires=["api-management-local", "variable-local", "boto3>=1.28.70", "message-local",
                      "database-mysql-local>=0.0.121", "python-sdk-local"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
