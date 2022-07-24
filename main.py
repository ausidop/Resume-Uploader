import os
import shutil
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from docx2pdf import convert
from dotenv import load_dotenv

# authenticate Google Drive
print('Authenticate Google...')
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
print('Connecting Google Drive...')
drive = GoogleDrive(gauth)
load_dotenv()
file = drive.CreateFile({'id': os.environ.get('FILE_ID')})
file.GetContentFile('Chergang Chang.docx')
print('File downloaded.')
# convert docx to pdf
print('Converting to PDF...')
convert("Chergang Chang.docx", "Chergang Chang.pdf")

# copy my resumes(.docx & .pdf) to resume folder
# also copy resume(.pdf) to portfolio website assets folder
src_path = r"C:\Users\ausid\PycharmProjects\updateResume\\"
resume_path = r'C:\Users\ausid\Downloads\Resume\\'
website_path = r'D:\Codes\VSCode\portfolio\src\assets\\'
file_docx = 'Chergang Chang.docx'
file_pdf = 'Chergang Chang.pdf'

print('Move to target folders...')
shutil.move(src_path+file_docx, resume_path+file_docx)
shutil.move(src_path+file_pdf, website_path+file_pdf)


print('Performing git commands...')
# perform git commit command to change resume file on github
os.chdir('D:\Codes\VSCode\portfolio')
os.system(r'git add .')
os.system(r'git commit -m "update Resume"')
os.system(r"git push origin main")
