from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='athenapi',
    version='0.1.4',
    packages=find_packages(include=['athenapi']),
    package_data={
        'athenapi': ['assets/*']
    },
    install_requires=requirements,
    author='Xiaomeng Zhang',
    author_email="zhang123cnn@gmail.com",
    description='AI Agent on Raspberry Pi',
    readme='README.md',
    entry_points={
        'console_scripts': [
            'conversation=athenapi.conversation:main',
            'conversation_lite=athenapi.conversation_lite:main',
        ]
    }
)
