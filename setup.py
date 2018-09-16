from distutils.core import setup

setup(
  name = 'code-gov-web-tester',
  packages = ['code_gov_web_tester'],
  package_dir = {'code_gov_web_tester': 'code_gov_web_tester'},
  package_data = {'code_gov_web_tester': ['__init__.py']},
  version = '0.0.0',
  description = 'test code.gov using Python and Selenium',
  author = 'Victoria D. Mak',
  author_email = 'viymak@icloud.com',
  url = 'https://github.com/viymak/code-gov-web-tester',
  download_url = 'https://github.com/viymak/code-gov-web-tester/tarball/download',
  keywords = ['civic'],
  classifiers = [],
)
