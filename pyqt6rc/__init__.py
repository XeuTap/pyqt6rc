import re
__version__ = "0.1.2"

resource_pattern = re.compile('":(\/.*?\.[\w:]+)"')
indent_pattern = re.compile('\s+')