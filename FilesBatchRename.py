# FilesBatchRename.py
# 导入os库
import os

# 图片存放的路径
path = r"D:/temp"

# 遍历更改文件名
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,str(num))+".jpg")
    num = num + 1
