#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Copyright (c) 2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

from openstack.common import setup

requires = setup.parse_requirements()
depend_links = setup.parse_dependency_links()

setuptools.setup(
    name='openstack.common',
    version=setup.get_post_version('openstack'),
    description="Common components for Openstack",
    long_description="Common components for Openstack "
                     "including paster templates.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)', ],
    keywords='openstack',
    author='OpenStack',
    author_email='openstack@lists.launchpad.net',
    url='http://www.openstack.org/',
    license='Apache Software License',
    packages=setuptools.find_packages(exclude=['ez_setup',
                                               'examples', 'tests']),
    include_package_data=True,
    cmdclass=setup.get_cmdclass(),
    zip_safe=True,
    install_requires=requires,
    dependency_links=depend_links,
    setup_requires=['setuptools-git>=0.4'],
    entry_points="""
      # -*- Entry points: -*-
      """,
    namespace_packages=['openstack'],
)
