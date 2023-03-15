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


from distutils.core import setup
setup(
  name = 'admin_tools_db',         # How you named your package folder (MyLib)
  packages = ['admin_tools_db'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple functions for admin jobs in python',   # Give a short description about your library
  author = 'Dominic Burrows',                   # Type in your name
  author_email = 'dominicburrows@hotmail.co.uk',      # Type in your E-Mail
  url = 'https://github.com/dmnburrows/admin_tools_db',   # Provide either the link to your github or to your website
  download_url = 'https://pypi.org/project/admin_tools_db/' # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
