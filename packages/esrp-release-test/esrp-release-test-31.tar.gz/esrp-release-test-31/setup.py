try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '31'

with open('README.rst', 'r') as f:
    readme = f.read()
with open('HISTORY.rst', 'r') as f:
    history = f.read().replace('.. :changelog:', '')

requirements = [
    'azure-storage-blob',
    'requests',
    'enum34;python_version<"3.9"',
]

setup(
    name='esrp-release-test',
    version=VERSION,
    description='ESRP Release is a pathway to many abilities some consider to be, unnatural.',
    long_description=readme + '\n\n' + history,
    long_description_content_type = 'text/x-rst',
    author = 'Vishal Jaishankar',
    author_email = 'vijaisha@microsoft.com',
    url='https://dev.azure.com/releaseado/MS.Ess.Release.VSTS.Extension/_git/esrp-release-test',
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='esrp-release-test',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)