from logging import Logger
import pandas
import smtplib,sys,configparser,logging,copy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, datetime


# inifilepath=r'D:\Learning\Python\Random_Name_Generator\helper\config.ini'
inifilepath=sys.argv[1]

message=""
team_name=""

def get_email_config_info(EMAIL_CONFIG_FILE):
    """Get email config from email_config.ini

    Arguments:
        EMAIL_CONFIG_FILE {[file]} -- [It should be email config file]

    Returns:
        [string,string,string] -- [SMTP_SERVER,PORT,SENDER]
    """

    config = configparser.RawConfigParser()
    config.read(EMAIL_CONFIG_FILE)
    SMTP_SERVER = config.get("Email_Config","SMTP_SERVER")
    PORT=config.get("Email_Config","PORT")
    SENDER = config.get("Email_Config","SENDER")
    SUBJECT=config.get("Email_Config","SUBJECT")
    EMAILBODYFILEPATH=config.get("Email_Config","EMAILBODYFILEPATH")
    LOGFILE=config.get("Email_Config","LOGFILE")
    TEAM_NAME=config.get("Email_Config","TEAM_NAME")
    EXCEL_PATH=config.get("Email_Config","EXCEL_PATH")
    return SMTP_SERVER,PORT,SENDER,SUBJECT,EMAILBODYFILEPATH,LOGFILE,TEAM_NAME,EXCEL_PATH

def SendEmail(SMTP_SERVER,PORT,SENDER,Mail_List,SUBJECT,Message):
    """Send Email utility

    Arguments:
        Mail_List {[list]} -- [Email receiver]
        SUBJECT {[string]} -- [Email subject]
        Message {[string]} -- [Email body]
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = Mail_List 
    msg['Body'] = Message
    msg.attach(MIMEText(Message,'html'))
    try:
        
        smtpObj = smtplib.SMTP(SMTP_SERVER,int(PORT))
        smtpObj.sendmail(SENDER, Mail_List, msg.as_string())
        print ("Successfully sent email")
    except Exception:
        print ("Error: unable to send email")

def get_content(filepath):
    with open(filepath,'r',encoding='utf-8-sig') as bodyfile:
        return bodyfile.readlines()

def notify_santa(child_row,current_row,message):
    santadetails={}
    santadetails['Name']=current_row['Name']
    santadetails['Email']= current_row['Email']

    message=str(message).format(
        santa_name= santadetails['Name'].split(' ')[0],
        child_name=child_row['Name'].values[0:1][0],
        child_emp_id= child_row['Emp_Id'].values[0:1][0],
        address=child_row['Address'].values[0:1][0],
        child_email=child_row['Email'].values[0:1][0],
        project_name=team_name,
        child_note= child_row['Note'].values[0:1][0],
        )

    SendEmail(smptpserver,port,sender,santadetails['Email'],subject,message)
    logging.debug('Mail sent -> '+ str(date.today()))

def assign_child(team_members,child_row,current_row):
    counter = 0
    isvalid=False
    while(counter < 3):
        counter+=1
        if(child_row['Name'].values[0:1][0] == current_row['Name']):
            child_row= team_members.sample()
            print(f"Trying Again for {current_row['Name']}")
            continue
        else:
            isvalid=True
            break
    return isvalid,child_row
        
def get_rowdetails(df,team_members,message): 
    for _, current_row in df.iterrows():
        child_row= team_members.sample()
        isvalid,child_row = assign_child(team_members,child_row,current_row)
        if(not isvalid):
            print("Sorry, No child is assign for => "+ current_row['Name'])
        notify_santa(child_row,current_row,message)

if __name__ == "__main__":
    try:
        smptpserver,port,sender,subject,emailbodyfilepath,logfile,team_name,filepath= get_email_config_info(inifilepath)
        df = pandas.read_excel(filepath,sheet_name=team_name,header=0)
        team_members=copy.deepcopy(df)
        child_row= None
        logging.basicConfig(filename=logfile,level=logging.DEBUG)
        logging.debug(datetime.now())
        message=" ".join(get_content(emailbodyfilepath))
        get_rowdetails(df,team_members,message)
        
    except Exception as ex:
        logging.error(ex)