from ftplib import FTP

ftp = FTP(host='localhost',user='user',passwd='12345')
ftp.encoding = 'gbk'
ftp.cwd('test')
ftp.retrlines('list')
ftp.retrbinary('RETR test',open('note.txt','wb').write)
ftp.storbinary('STOR ftpserver.py',open('ftpserver.py','rb'))
for f in ftp.mlsd(path='/test'):
    print(f)
