from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

requirements=['packaging']

setup(
        name='raga_practice_util',
        description='This is a sample project',
        long_description = long_description,
        url = 'https://github.com/ragabala/Raga_Practise_Util',
        author = 'Ragavendran balakrishnan',
        author_email = 'ragbalak@redhat.com',
        license='TEST',
        install_requires = requirements,
        classifiers = [
                'Development Status :: 2 - Pre-Alpha,',
                'Operating System :: POSIX :: Linux',
                'License :: Freeware',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.7'],
        extras_require = {
            'dev' : [
                'pylint',
                ],
            
            },


        )

