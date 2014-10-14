from setuptools import setup

setup(name='enforcer',
      version='0.1',
      description='Tool which takes a two sets (current, desired) and then calls callbacks to enforce progression from current to desired state.',
      url='http://github.com/andrewguy9/enforcer',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['enforcer'],
      entry_points = {
        'console_scripts': [
          'enforce = enforcer.enforceui:main',
          ],
      },
      zip_safe=False)
