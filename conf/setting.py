import os

# 项目根目录
BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# case目录
CASEPATH = os.path.join(BASEPATH, 'case')

# report目录
REPORTPATH = BASEPATH + os.path.sep + 'report' + os.path.sep + 'report.html'

# log目录
LOGPATH = BASEPATH + os.path.sep + 'log' + os.path.sep
WEBLOGPATH = LOGPATH + 'server.log'
WEBPICTUREPATH = os.path.join(BASEPATH,'report','picture') + os.path.sep

