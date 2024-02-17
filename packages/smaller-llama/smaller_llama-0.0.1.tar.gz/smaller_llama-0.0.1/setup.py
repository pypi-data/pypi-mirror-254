from setuptools import setup, find_packages

def post_install():
    """ Implement post installation routine """
    with open('./requirements.txt') as f:
        install_requires = f.read().splitlines()

    return install_requires

setup(
    name='smaller_llama',
    version='0.0.1',
    author='javad nematollahi',
    author_email='javadnematollahi92@gmail.com',
    description='Get information from custom text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://git.parstechai.com/parstech-nlp/nlg/parschat-logic/-/tree/feat/sensomatt_doc?ref_type=heads",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=post_install(),
    include_package_data=True,
)
