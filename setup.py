import setuptools

setuptools.setup(
    name='rst2html',
    version='2020.7.4',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
