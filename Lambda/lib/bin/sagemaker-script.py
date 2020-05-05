#!c:\users\hyper\appdata\local\programs\python\python38\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sagemaker==1.56.1.post1','console_scripts','sagemaker'
__requires__ = 'sagemaker==1.56.1.post1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sagemaker==1.56.1.post1', 'console_scripts', 'sagemaker')()
    )
