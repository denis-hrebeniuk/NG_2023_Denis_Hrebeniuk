import sys


sys.path.append("..") # Import util.py by changing directory to ../
from util import request_list

unique_list = list(set(request_list()))
print(f"Your list of items (only unique items will be displayed): {unique_list}")