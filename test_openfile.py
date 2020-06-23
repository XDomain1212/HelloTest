with open('newfile.txt','a',encoding='utf-8') as steam:
    words='Hello, file.'
    if steam.writable() :
        steam.writelines('\n'+words)
