import os
import shutil
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from docx2pdf import convert

# authenticate Google Drive
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")

# connect to Google Drive and download my resume
drive = GoogleDrive(gauth)
file_id = '1H0Xmx5m0L-15cfpBJT30_BV8ZE-YzO29'
file = drive.CreateFile({'id': file_id})
file.GetContentFile('Chergang Chang.docx')

# convert docx to pdf
convert("Chergang Chang.docx", "Chergang Chang.pdf")

# copy my resumes(.docx & .pdf) to resume folder
# also copy resume(.pdf) to portfolio website assets folder
src_path = r"C:\Users\ausid\PycharmProjects\updateResume\\"
resume_path = r'C:\Users\ausid\Downloads\Resume\\'
website_path = r'D:\Codes\VSCode\portfolio\src\assets\\'
file_docx = 'Chergang Chang.docx'
file_pdf = 'Chergang Chang.pdf'

shutil.move(src_path+file_docx, resume_path+file_docx)
shutil.move(src_path+file_pdf, website_path+file_pdf)


# perform git commit command to change resume file on github
os.chdir('D:\Codes\VSCode\portfolio')
os.system(r'git add .')
os.system(r'git commit -m "update Resume"')
os.system(r"git push origin main")
