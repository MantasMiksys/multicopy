from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='multicopy',
    version='0.0.1',
    description="An application for performing multiple copies",
    author="Mantas Miksys",
    author_email='man.miksys@gmail.com',
    url='https://github.com/mantasmiksys/multicopy',
    packages=['multicopy', 'multicopy.images',
              'multicopy.tests'],
    package_data={'multicopy.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'multicopy=multicopy.application:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='multicopy',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
