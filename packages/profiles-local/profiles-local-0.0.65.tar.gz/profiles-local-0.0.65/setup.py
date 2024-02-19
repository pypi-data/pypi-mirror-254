import setuptools

PACKAGE_NAME = "profiles-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.65',  # https://pypi.org/project/profiles-local/
    author="Circles",
    author_email="info@circles.life",
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    description="This is a package for sharing common crud operation to profile schema in the db",
    long_description="This is a package for sharing common profile functions used in different repositories",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=["database-mysql-local>=0.0.199",
                      "logger-local>=0.0.67",
                      "location-profile-local>=0.0.49",
                      "operational-hours-local>=0.0.19",
                      "person-local>=0.0.20",
                      "gender-local>=0.0.6",
                      "location-local>=0.0.81",
                      "reaction-local>=0.0.8",
                      "profile-reaction-local>=0.0.16",
                      "profile-profile-local>=0.0.9",
                      "language-local>=0.0.6",
                      "user-context-remote>=0.0.33",
                      "storage-local>=0.1.27",
                      "email-address-local>=0.0.16",
                      "group-profile-remote>=0.0.14"
                      ]
)
