from setuptools import setup

setup(
    name='Kalkayotl',
    version='0.7.0',
    author='Javier Olivares',
    author_email='javier.olivares-romero@u-bordeaux.fr',
    packages=['kalkayotl'],
    license='COPYING',
    description='Star distance inference code',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    python_requires='>=3.6',
    install_requires=[
        'pymc3==3.7',
        'matplotlib==3.1.1',
        'dynesty==1.0.0',
        'arviz==0.5.1'
    ],
    zip_safe=True
)
