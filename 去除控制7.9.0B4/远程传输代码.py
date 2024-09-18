#  -*- coding: UTF-8 -*-

# MindPlus
# Python


dress = (str("D:/001.txt"))
out_text = (str("@echo off"))
fileObj = open("001.py", "r", encoding="UTF8")
in_text = fileObj.readlines()
i = -1
i = (i + 1)
if ((str(((str((in_text[i])))[0:-1]))) == (str(""))):
    out_text = (str(out_text) + str((str(" && ") + str((str("echo") + str((str(".") + str((str(">") + str(dress))))))))))
else:
    out_text = (str(out_text) + str((str(" && ") + str((str("echo ") + str((str(((str((in_text[i])))[0:-1])) + str((str(">") + str(dress))))))))))
for index in range((len(in_text) - 2)):
    i = (i + 1)
    if ((str(((str((in_text[i])))[0:-1]))) == (str(""))):
        out_text = (str(out_text) + str((str(" && ") + str((str("echo") + str((str(".") + str((str(">>") + str(dress))))))))))
    else:
        out_text = (str(out_text) + str((str(" && ") + str((str("echo ") + str((str(((str((in_text[i])))[0:-1])) + str((str(">>") + str(dress))))))))))
i = (i + 1)
if ((str(((str((in_text[i])))[0:-1]))) == (str(""))):
    out_text = (str(out_text) + str((str(" && ") + str((str("echo") + str((str(".") + str((str(">>") + str(dress))))))))))
else:
    out_text = (str(out_text) + str((str(" && ") + str((str("echo ") + str((str((str((in_text[i])))) + str((str(">>") + str(dress))))))))))
out_text = str(out_text) + str(" && start ") + str(dress)
out_text = str(out_text) + str(" && TIMEOUT /T 1")
out_text = str(out_text) + str(" && ") + str('echo msgbox "请将文本全选复制到你的python程序中运行（Ctrl+A全选，Ctrl+C复制，Ctrl+V粘贴，Ctrl+S保存，F5运行）",64,"程序传输成功！">alert.vbs && start alert.vbs && ping -n 2 127.1>nul && del alert.vbs')
out_text = str(out_text) + str(" && exit")
fileObj.close()
fileObj = open("commond.txt", "w", encoding="UTF8")
fileObj.write("1\n")
fileObj.write(out_text)
fileObj.close()
