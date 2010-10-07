#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os
from setuptools import setup, find_packages

version = '0.4'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmislib",
    description = 'CMIS client library for Python',
    version = version,
    author = 'Jeff Potts',
    author_email = 'jeffpotts01@gmail.com',
    license = 'Apache',
    url = 'http://code.google.com/p/cmislib/',
    package_dir = {'':'src'},
    packages = find_packages("src"),
    include_package_data = True,
    long_description = read('README.txt'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        ],
)