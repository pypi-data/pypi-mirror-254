
from setuptools import setup, find_packages
from glob import glob

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()


setup(
   name='nriapp',
   version='1.2.07',
   description='This is an internal tool for querying MS 365 Defender using MSGraph and MS Sentinels API with NRI\n'
               'Added capability for MDR portal\n'
               'Changes: Fixed the impacted assets in new template.',
    license='MIT',
   author='Llallum Victoria',
   author_email='llallumvictoria@gmail.com',
#   packages=find_packages('src'),
   package_dir = {'':'src/nriapp'},
    
   packages=['.','config', 'core', 'helper'],  #same as name
#   packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
   data_files=[('.', ['src/nriapp/changelog.txt']),
               ('./session', glob('./src/session/*.*')),
               ('./logs', glob('./src/logs/*.*')),
               ('./output', glob('./src/output/*.*'))
              ],
   #setup_requires=['session', 'logs', 'output'],
   include_package_data=True,
   install_requires=[
        "selenium-wire",
        "webdriver-manager",
        "loguru",
        "tldextract",
        "python-dateutil",
        "pytz",
        "xmltodict",
        "azure-kusto-data",
        "azure-kusto-ingest",
        "pandas",
        "bs4",
        "keyring",
        "python-docx",
        "xlsxwriter"
       ],
#   install_requires=requirements, #external packages as dependencies,
   entry_points = '''
        [console_scripts]
        nriapp=nriapp:main
    '''

)
