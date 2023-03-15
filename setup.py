from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='admin_tools_db',
    version='0.1',
    description='Simple functions for admin jobs in python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Dominic Burrows',
    author_email='dominicburrows@hotmail.co.uk',
    keywords=[''],
    url='https://github.com/dmnburrows/admin_tools_db',
    download_url='https://pypi.org/project/admin_tools_db/'
)

install_requires = [
                 'numpy'
]

setup(**setup_args, install_requires=install_requires)
