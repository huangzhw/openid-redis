from setuptools import setup, find_packages
import sys, os

version = '1.3'

setup(name='openid-redis',
      version=version,
      description="A Redis storage backend for the python-openid package",
      long_description="""\
""",
      classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP"
      ],
      keywords='openid redis',
      author='Ben Bangert',
      author_email='ben@groovie.org',
      url='http://github.com/bbangert/openid-redis',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["redis>=2.4.0", "python-openid>=2.2.5"],
      entry_points="""
      # -*- Entry points: -*-
      """,
)
