import os
import importlib.util
import sys

# import sub_folder.test2 as test2

CurrDirPath = os.path.dirname(__file__)
CurrFileName = os.path.join(CurrDirPath, r"sub_folder\test2.py")

spec = importlib.util.spec_from_file_location("test2", CurrFileName)
test2 = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = test2
spec.loader.exec_module(test2)

if __name__ == '__main__':
    print(test2.test3())