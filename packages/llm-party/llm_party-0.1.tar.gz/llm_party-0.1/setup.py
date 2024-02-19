from setuptools import setup, find_packages

setup(
    name='llm_party',
    version='0.1',
    author='Akihito Sudo',
    author_email="akihito.s.gm@gmail.com",
    url="https://github.com/sudodo/llm_party",
    packages=find_packages(),
    install_requires=[
        'llm_wrap==0.1.1',
        'marshmallow==3.20.1',
        'PyYAML==6.0.1',
    ],
)
