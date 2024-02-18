import os

from setuptools import setup
from setuptools.command.install import install


class build_libbash(install):
    def run(self):
        install.run(self)
        result = os.system("cd " + os.path.join
                  (os.path.dirname(__file__), "libbash", "bash-5.2") +
                  " && ./configure && make clean all")
        if result != 0:
            raise Exception("Bash compilation failed")

setup(name='libbash',
      packages=['libbash', 'libbash.bash_command'],
      cmdclass={'install': build_libbash},
      package_data={'libbash': ['bash-5.2/*']},
      version='0.1.2',
      description="A Python library for parsing Bash scripts into an AST",
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url="https://github.com/binpash/libbash/",
      author='Seth Sabar',
      author_email='sethsabar@gmail.com',
      license="GPL-3.0",
      include_package_data=True,
      has_ext_modules=lambda: True)

