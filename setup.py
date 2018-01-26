from setuptools import setup

setup(name='lazzy_toggl',
      version='1.0.0',
      description='Toggl enhancement with Gmail -- too lazzy',
      url='https://github.com/mades-g/LazzyToggl/',
      author='eudes duarte',
      author_email='eudesgracias.duarte@gmail.com',
      license='GPLv3',
      packages=['lazzy_toggl'],
      entry_points={
          "console_scripts": ['lazzy_toggl = lazzy_toggl.lazzy_toggl:main']
      },
      install_requires=[
          'requests'
      ]
)