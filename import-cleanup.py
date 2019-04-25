import pandas as pd
import zipfile
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()

import_data = zipfile.ZipFile(filedialog.askopenfilename())
import_data.extractall()

root.quit()


def clean():

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
    clean()
    if input('Delete another client ID? (y/n)') != 'y':
        break


def import_convert():

    #  get export id
    exp_df = pd.read_csv('Export.csv')
    export_id = exp_df.iloc[0]['ExportID']

    #  Project Identifiers
    df1 = pd.read_csv('Project.csv', dtype=object)
    df1.insert(4, 'OperatingStartDate',  '1990/01/01')
    df1.insert(5, 'OperatingEndDate', '')
    df1.insert(11, 'VictimServicesProvider', '0')
    df1.insert(12, 'HousingType', '')
    df1.to_csv('Project.csv', index=None)
    #  project.csv complete

    #  inventory, blank for now to match old imports. Leaving as notes in case needed later
    #  in_df = pd.read_excel('HMISinventory.xlsx')
    #  in_df['ExportID'] = export_id
    #  in_df.to_csv('Inventory.csv', index=None)
    #  inventory complete

    # Enrollment
    enrollment_df = pd.read_csv('Enrollment.csv', dtype=object)
    #  renames column names
    enrollment_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    enrollment_df.rename(columns={'ResidencePrior': 'LivingSituation'}, inplace=True)
    enrollment_df.rename(columns={'ResidencePriorLengthOfStay': 'LengthOfStay'}, inplace=True)
    enrollment_df.rename(columns={'ResidentialMoveInDate': 'MoveInDate'}, inplace=True)
    enrollment_df.rename(columns={'FYSBYouth': 'EligibleForRHY'}, inplace=True)
    enrollment_df.rename(columns={'LastPermanentZIP9': 'LastPermanentZIP'}, inplace=True)
    enrollment_df.insert(30, 'RunawayYouth', '')
    enrollment_df.drop(columns=['HousingIssuesYouth', 'HousingIssuesFam',
                                'SexualOrientationGenderIDYouth', 'SchoolEducationalIssuesYouth',
                                'SchoolEducationalIssuesFam', 'HouseholdDynamics', 'HousingStatus',
                                'UnemploymentYouth', 'MentalHealthIssuesYouth', 'HealthIssuesYouth',
                                'SexualOrientationGenderIDFam', 'PhysicalDisabilityYouth',
                                'MentalDisabilityYouth', 'MentalDisabilityFam', 'AbuseAndNeglectYouth',
                                'AbuseAndNeglectFam', 'AlcoholDrugAbuseYouth', 'ActiveMilitaryParent',
                                'IncarceratedParentStatus', 'ExchangeForSex', 'ExchangeForSexPastThreeMonths',
                                'CountOfExchangeForSex', 'AskedOrForcedToExchangeForSex',
                                'AskedOrForcedToExchangeForSexPastThreeMonths', 'WorkPlaceViolenceThreats',
                                'WorkplacePromiseDifference', 'CoercedToContinueWork',
                                'LaborExploitPastThreeMonths', 'ERVisits', 'JailNights',
                                'HospitalNights', 'HealthIssuesFam'], inplace=True)
    
    enrollment_df.to_csv('Enrollment.csv', index=None)
    #  Enrollment complete

    #  exit
    exit_df = pd.read_csv('Exit.csv', dtype=object)
    exit_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    exit_df.drop(columns={'WrittenAftercarePlan', 'AssistanceMainstreamBenefits', 'PermanentHousingPlacement',
                          'TemporaryShelterPlacement', 'ExitCounseling', 'FurtherFollowUpServices',
                          'ScheduledFollowUpContacts', 'ResourcePackage', 'OtherAftercarePlanOrAction',
                          'FamilyReunificationAchieved'}, inplace=True)
    exit_df.insert(12, 'ExchangeForSex', '')
    exit_df.insert(13, 'ExchangeForSexPastThreeMonths', '')
    exit_df.insert(14, 'CountOfExchangeForSex', '')
    exit_df.insert(15, 'AskedOrForcedToExchangeForSex', '')
    exit_df.insert(16, 'AskedOrForcedToExchangeForSexPastThreeMonths', '')
    exit_df.insert(17, 'WorkPlaceViolenceThreats', '')
    exit_df.insert(18, 'WorkPlacePromiseDifference', '')
    exit_df.insert(19, 'CoercedToContinueWork', '')
    exit_df.insert(20, 'LaborExploitPastThreeMonths', '')
    exit_df.insert(21, 'CounselingReceived', '')
    exit_df.insert(22, 'IndividualCounseling', '')
    exit_df.insert(23, 'FamilyCounseling', '')
    exit_df.insert(24, 'GroupCounseling', '')
    exit_df.insert(25, 'SessionCountAtExit', '')
    exit_df.insert(26, 'PostExitCounselingPlan', '')
    exit_df.insert(27, 'SessionsInPlan', '')
    exit_df.insert(28, 'DestinationSafeClient', '')
    exit_df.insert(29, 'DestinationSafeWorker', '')
    exit_df.insert(30, 'PosAdultConnections', '')
    exit_df.insert(31, 'PosPeerConnections', '')
    exit_df.insert(32, 'PosCommunityConnections', '')
    exit_df.insert(33, 'AftercareDate', '')
    exit_df.insert(34, 'AftercareProvided', '')
    exit_df.insert(35, 'EmailSocialMedia', '')
    exit_df.insert(36, 'Telephone', '')
    exit_df.insert(37, 'InPersonIndividual', '')
    exit_df.insert(38, 'InPersonGroup', '')
    exit_df.insert(39, 'CMExitReason', '')
    exit_df.to_csv('Exit.csv', index=None)
    #  exit done.

    #  health and DV
    dvdf = pd.read_csv('HealthAndDV.csv', dtype=object)
    dvdf.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    dvdf.to_csv('HealthandDV.csv', index=None)
    #  health and DV complete

    #  income and benefits
    benefits_df = pd.read_csv('IncomeBenefits.csv', dtype=object)
    benefits_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    benefits_df.drop(columns={'RentalAssistanceOngoing', 'RentalAssistanceTemp'}, inplace=True)
    #  benefits_df.loc[:, 'NoMedicaidReason'] = '99'
    #  benefits_df.loc[:, 'NoMedicareReason'] = '99'
    #  benefits_df.loc[:, 'NoSCHIPReason'] = '99'
    #  benefits_df.loc[:, 'NoVAMedReason'] = '99'
    #  benefits_df.loc[:, 'NoEmployerProvidedReason'] = '99'
    #  benefits_df.loc[:, 'NoCOBRAReason'] = '99'
    #  benefits_df.loc[:, 'NoPrivatePayReason'] = '99'
    #  benefits_df.loc[:, 'NoStateHealthInsReason'] = '99'
    #  benefits_df.loc[:, 'NoIndianHealthServicesReason'] = '99'
    #  benefits_df.loc[:, 'NoHIVAIDSAssistanceReason'] = '99'
    #  benefits_df.loc[:, 'NoADAPReason'] = '99'
    benefits_df.to_csv('IncomeBenefits.csv', index=None)
    #  income and benefits complete

    # employment/education
    emp_df = pd.read_csv('EmploymentEducation.csv', dtype=object)
    emp_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    emp_df.to_csv('EmploymentEducation.csv', index=None)
    #  employment/education complete

    #  disabilities
    dis_df = pd.read_csv('Disabilities.csv', dtype=object)
    dis_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    dis_df.drop(columns={'DocumentationOnFile', 'ReceivingServices',
                         'PATHHowConfirmed', 'PATHSMIInformation'}, inplace=True)
    dis_df.to_csv('Disabilities.csv', index=None)
    #  disabilities complete

    #  services
    serv_df = pd.read_csv('Services.csv', dtype=object)
    serv_df.rename(columns={'ProjectEntryID': 'EnrollmentID'}, inplace=True)
    serv_df.to_csv('Services.csv', index=None)
    #  services complete

    #  Create geography df, save as csv
    geo = {'GeographyID': [16, 77, 15, 33], 'ProjectID': [2, 4, 0, 6],
           'CoCCode': ['IN-503', 'IN-503', 'IN-503', 'IN-503'],
           'InformationDate': ['2018-09-28', '2019-03-11', '2018-09-28', '10/01/2018'],
           'Geocode': ['181404', '181404', '18104', '181404'],
           'GeographyType': ['1', '1', '1', '1'],
           'Address1': ['320 e Market St', '520 E Market ST', '520 e Market St', '245 N DELAWARE ST'],
           'Address2': [None, None, None, None], 'City': ['Indianapolis', 'Indianapolis', 'Indianapolis', 'Indianapolis'],
           'State': ['IN', 'IN', 'IN', 'IN'], 'ZIP': ['46201', '46204', '46204', '46204'],
           'DateCreated': ['2018-09-28 01:19:35', '2019-03-11 11:15:19', '2018-09-28 01:14:53', '2018-10-01 02:16:29'],
           'DateUpdated:': ['2018-09-28 01:19:35', '2019-03-11 11:15:19', '2018-09-28 01:14:53', '2018-10-01 02:16:29'],
           'UserID': ['AC3', 'AC3', 'AC3', 'AC3'], 'DateDeleted': [None, None, None, None],
           'ExportID': [None, None, None, None]}
    geo_df = pd.DataFrame(data=geo, dtype=object)
    geo_df['ExportID'] = export_id
    geo_df.to_csv('Geography.csv', index=None)
    #  geography complete

    # delete site.csv
    os.remove('Site.csv')

    # project coc update
    os.remove('ProjectCoC.csv')
    #  proj_coc_df = pd.read_excel('ProjectCoC.xlsx', dtype=object)
    proj = {'ProjectCoCID': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7'],
            'ProjectID': ['0', '1', '2', '4', '5', '6', '98'],
            'ProjectName': ['Wheeler Long Term Shelter', 'Wheeler Emergency Nights',
                            'Center for Women and Children (CWC)',
                            'Shelter for Men(SFM)', 'Training Center at Camp Hunt (TC)',
                            'Men\'s Residential Center (MRC)', 'Higher Ground'],
            'CoCCode': ['IN-503', 'IN-503', 'IN-503', 'IN-503', 'IN-503', 'IN-503', 'IN-503'],
            'DateCreated': ['1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00',
                            '1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00'],
            'DateUpdated': ['1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00',
                            '1990-01-01 12:00:00', '1990-01-01 12:00:00', '1990-01-01 12:00:00'],
            'UserID': ['2', '2', '2', '2', '2', '2', '2'],
            'DateDeleted': [None, None, None, None, None, None, None],
            'ExportID': [None, None, None, None, None, None, None]}
    proj_coc_df = pd.DataFrame(data=proj, dtype=object)
    proj_coc_df['ExportID'] = export_id
    proj_coc_df.to_csv('ProjectCoC.csv', index=None)
    # proj coc csv complete

    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)


while True:
    import_convert()
    break

newzip = zipfile.ZipFile(os.path.join(os.getcwd(), 'wheeler_data.zip'), 'w')
path = os.getcwd()
sys.path.append(path)
files = os.listdir(path)

for file in files:
    if file.endswith('.csv'):
        newzip.write(file)


newzip.close()

newname = input('Enter new name: ') + str('.zip')
os.rename('wheeler_data.zip', newname)

for file in files:
    if file.endswith('.csv'):
        os.remove(file)

input('Press "enter to close.')
