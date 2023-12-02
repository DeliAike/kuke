import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'data' + os.sep
# print(BASE_PATH)
BASE_PATH_REPORT_LOG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'report_log' + os.sep
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep

print(PROJECT_PATH)
print(BASE_PATH_REPORT_LOG + 'log' + os.sep + 'login_log.txt')
print(BASE_PATH_REPORT_LOG + 'report' + os.sep + 'login_report.html')