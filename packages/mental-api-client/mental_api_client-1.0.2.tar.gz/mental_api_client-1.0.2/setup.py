from setuptools import setup, find_packages
from pkg_resources import parse_requirements


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name='mental_api_client',
    version='1.0.2',
    description='Client for team mental api',
    url='https://github.com/hqdem/team_mental_pyclient',
    author='Ilya Demidov',
    author_email='iademidov@edu.hse.ru',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=load_requirements('/Users/iademidov1/projects/python/team_mental_client/requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
