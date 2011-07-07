try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='jellypy',
    version="0.1",
    description="jellypy is a port of the great node package 'Jellyfish'",
    author="Anthony Long",
    author_email="antlong@gmail.com",
    packages=["jellypy.selenium", "jellypy.webdriver","jellypy.zombie"],
    include_package_data=True,
    package_data={"*": "*"},
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python', ],
    zip_safe=False,
)
