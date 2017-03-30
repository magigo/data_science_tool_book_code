# ! /usr/bin/python
# -*- coding: utf-8 -*-
"""亲爱的读者您好，如果这是您第一次接触Python，还没有足够的知识运行这一段代码，请先学习之后的章节"""

import sys

from colorama import init

init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('welcome', font='starwars'),
       'yellow', 'on_blue', attrs=['bold'])
