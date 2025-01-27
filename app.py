
"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()



with open('requirements.txt') as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace('\n', '') for lib in requirements_list]

requirements = requirements_list

test_requirements = []

setup(
    author="Gezahegne",
    #email="enggezahegn.w@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tellco User Analysis project",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts',
    name='scripts',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gezish/TellCo-UserDataAnalytics',
    version='0.1.0',
    zip_safe=False,
)