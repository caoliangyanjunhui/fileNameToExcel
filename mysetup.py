from distutils.core import setup
import py2exe


options = {"py2exe":
				{"compressed": 1, 
			 "optimize": 2,
			 "bundle_files": 1,
			 "dll_excludes": ["w9xpopen.exe"]}
		}

setup(
    windows = [
    {
        "script": "main.py",
        "icon_resources": [(1, "ico/excel.ico")]
    }
    ],
	data_files=[("ico", 
			["ico/excel.ico",])]
)