from distutils.core import setup
import py2exe

setup(windows=['main.py'],
      name="HotSpot Management by Himanshu Shankar",
      options = {'py2exe': {
        "optimize": 2,
        "bundle_files": 2, # This tells py2exe to bundle everything
      }},
)
