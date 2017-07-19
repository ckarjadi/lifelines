import os

from setuptools import setup


def filepath(fname):
    return os.path.join(os.path.dirname(__file__), fname)

exec(compile(open('lifelines/version.py').read(),
                  'lifelines/version.py', 'exec'))

readme_md = filepath('README.md')

try:
    import pypandoc
    readme_rst = pypandoc.convert_file(readme_md, 'rst')
except(ImportError):
    readme_rst = open(readme_md).read()


setup(
    name="lifelines",
    version=__version__,
    author="Cameron Davidson-Pilon, Jonas Kalderstam",
    author_email="cam.davidson.pilon@gmail.com",
    description="Survival analysis in Python, including Kaplan Meier, Nelson Aalen and regression",
    license="MIT",
    keywords="survival analysis statistics data analysis",
    url="https://github.com/CamDavidsonPilon/lifelines",
    packages=['lifelines',
              'lifelines.datasets',
              'lifelines.fitters',
              'lifelines.utils',
              ],
    long_description=readme_rst,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering",
        ],
    install_requires=[
        "numpy",
        "scipy",
        "pandas>=0.18",
    ],
    package_data={
        "lifelines": [
            "../README.md",
            "../README.txt",
            "../LICENSE",
            "../MANIFEST.in",
            "datasets/*",
        ]
    },
)
