from setuptools import setup,  find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Homework-7',
    author='Anzhelika Kodlubovska',
    author_email='angelikagymnasticschannel@gmail.com',
    license='MIT',
    packages= find_namespace_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
)
