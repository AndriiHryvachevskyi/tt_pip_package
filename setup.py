import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tt_pip_package',
    version='0.0.1',
    author='Andrii Hryvachevskyi',
    author_email='andrii.hryvachevskyi@ringteam.com',
    description='Test Tast PIP Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AndriiHryvachevskyi/tt_pip_package',
    project_urls={
        "Bug Tracker": "https://github.com/AndriiHryvachevskyi/tt_pip_package/issues"
    },
    license='MIT',
    packages=['tt_pip_package'],
    install_requires=['requests'],
)