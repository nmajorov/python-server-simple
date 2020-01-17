#!/usr/bin/env python

from setuptools import setup,Command
import shutil,os,glob

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob.glob(os.path.normpath(os.path.join(".", path_spec)))
            for path in [str(p) for p in abs_paths]:
                #if not path.startswith("."):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                 #   raise ValueError("%s is not a path inside %s" % (path, "."))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)


setup(name='python_server_simple',
      version='1.0',
      description='simple server in python',
      author='Nikolaj Majorov',
      author_email='nikolaj@majorov.biz',
      url='https://www.majorov.biz',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3','requests'],
      entry_points={
          'console_scripts': ['python_server_simple=server:main'],
      },
       cmdclass={'clean': CleanCommand}
     )
