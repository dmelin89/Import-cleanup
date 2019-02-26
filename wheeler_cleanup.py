import os
import zipfile
from tkinter import *
from tkinter import filedialog
import pandas as pd

root = Tk()
root.withdraw()

import_file = (filedialog.askopenfilename())
data = zipfile.ZipFile(import_file)
data.extractall()

root.quit()


def main():

    clientid = input('What client ID needs to be deleted?')

    #  specify data type, otherwise these columns come out as float. Decimals prevent importation
    df1 = pd.read_csv('Client.csv', dtype=object)
    clientclean = df1.loc[df1['PersonalID'] != clientid]
    clientclean.to_csv('Client.csv', index=None)
    # client done

    df2 = pd.read_csv('Disabilities.csv', dtype=object)
    disclean = df2.loc[df2['PersonalID'] != clientid]
    disclean.to_csv('Disabilities.csv', index=None)
    # disabilities done

    df3 = pd.read_csv('EmploymentEducation.csv', dtype=object)
    empclean = df3.loc[df3['PersonalID'] != clientid]
    empclean.to_csv('EmploymentEducation.csv', index=None)
    # education done, I think

    df4 = pd.read_csv('Enrollment.csv', dtype=object)
    enrollclean = df4.loc[df4['PersonalID'] != clientid]
    enrollclean.to_csv('Enrollment.csv', index=None)
    # enrollment done

    df5 = pd.read_csv('Exit.csv', dtype=object)
    exitclean = df5.loc[df5['PersonalID'] != clientid]
    exitclean.to_csv('Exit.csv', index=None)
    # exit done

    df6 = pd.read_csv('HealthAndDV.csv', dtype=object)
    dvclean = df6.loc[df6['PersonalID'] != clientid]
    dvclean.to_csv('HealthAndDV.csv', index=None)
    # dv done, I think

    df7 = pd.read_csv('IncomeBenefits.csv', dtype=object)
    incclean = df7.loc[df7['PersonalID'] != clientid]
    incclean.to_csv('IncomeBenefits.csv', index=None)


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
