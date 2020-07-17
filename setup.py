import datetime
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():

    def version_scheme(version):
        fmt = '%Y.%m.%d.%H.%M'
        now = datetime.datetime.now()
        return now.strftime(fmt)

    return {'version_scheme': version_scheme}


setuptools.setup(
    name="egencia-hotel-sort-revenue-optimization",
    use_scm_version=get_version,
    author="Egencia",
    description="Archetype for creating a Data Science project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.expedia.biz/Egencia/https://github.expedia.biz/Egencia/datascience-project-template-repo",
    packages=setuptools.find_packages(),
    setup_requires=['setuptools_scm'],
    install_requires=['pandas==0.21.0',
                      'numpy==1.14.0',
                      'pytz==2017.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
