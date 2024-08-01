import os,sys
os.system("git pull")
try:
    __import__("SWAGXD").swag()
except Exception as e:
    exit(str(e))
