#!c:\blog_depend\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ghp-import==2.0.1','console_scripts','ghp-import'
__requires__ = 'ghp-import==2.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ghp-import==2.0.1', 'console_scripts', 'ghp-import')()
    )
