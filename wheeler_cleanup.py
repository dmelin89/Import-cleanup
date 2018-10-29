import os
import zipfile
from tkinter import *
from tkinter import filedialog
import pandas as pd


def main():
    root = Tk()
    root.withdraw()

    data = zipfile.ZipFile(filedialog.askopenfilename())
    data.extractall()

    root.quit()

    clientid = int(input('What client ID needs to be deleted?'))

    df1 = pd.read_csv('Client.csv')
    clientclean = df1.loc[df1['PersonalID'] != clientid]
    clientclean.to_csv('Client.csv')

    df2 = pd.read_csv('Disabilities.csv')
    disclean = df2.loc[df2['PersonalID'] != clientid]
    disclean.to_csv('Disabilities.csv')

    df3 = pd.read_csv('EmploymentEducation.csv')
    empclean = df3.loc[df3['PersonalID'] != clientid]
    empclean.to_csv('EmploymentEducation.csv')

    df4 = pd.read_csv('Enrollment.csv')
    enrollclean = df4.loc[df4['PersonalID'] != clientid]
    enrollclean.to_csv('Enrollment.csv')

    df5 = pd.read_csv('Exit.csv')
    exitclean = df5.loc[df5['PersonalID'] != clientid]
    exitclean.to_csv('Exit.csv')

    df6 = pd.read_csv('HealthAndDV.csv')
    dvclean = df6.loc[df6['PersonalID'] != clientid]
    dvclean.to_csv('HealthAndDV.csv')

    df7 = pd.read_csv('IncomeBenefits.csv')
    incclean = df7.loc[df7['PersonalID'] != clientid]
    incclean.to_csv('IncomeBenefits.csv')


while True:
    main()
    if input('Delete another client ID? (y/n)') != 'y':
        break

 # zip csv files into new folder
newzip = zipfile.ZipFile(os.path.join(os.getcwd(), 'import.zip'), 'w')

path = os.getcwd()
sys.path.append(path)
files = os.listdir(path)

for file in files:
    if file.endswith('.csv'):
        newzip.write(file)

newzip.close()

#  Deletes csv files
for file in files:
    if file.endswith('.csv'):
        os.remove(file)
