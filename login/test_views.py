from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import pypyodbc
import pandas as pd
import plotly
import plotly.graph_objects as go
from datetime import datetime, timedelta
from dateutil import relativedelta
from onedash import graphs
from django.core.files.storage import default_storage
import os
from .convert import *
from sqlalchemy import create_engine
from .models import *
import win32security
import random
import sys
import math
import json
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pdfkit
import os
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt



BASE_DIR = os.path.dirname(__file__)

int_cols = ['callcount', 'calls', 'switched', 'offered', 'ivr_abd', 'agent_abd', 'answered', 'call count']

agent_desig = ['Customer Relationship Executive','Customer Response Executive', 'CRE Reliance Work From Home', 'Customer Response Executive-Part Timer',
             'Tele callers', 'Tele caller', 'Sr. CRE', 'Apprentice', 'CRE LOI', 'Help Desk Executive','Sr Customer Response Executive','Apprentice']

time_cols = ['aht', 'talk time(s)', 'avg wrap time', 'idle', 'avg handle time', 'staff time(s)', 'login time(s)',
             'aux time(s)', 'avg talk time', 'wait', 'ring', 'inbound_talk', 'ob talk time', 'consult',	'hold time(s)',
             'inbound_hold', 'ob hold time', 'acw time(s)',	'inbound_wrap',	'[ob wrap time', 'acw time', 'break time',
             'tea lunch', 'emergency', 'quality', 'call handle time', 'holdtime', 'talktime', 'wraptime',
             'login_duration_avg', 'training_time',	'ring_time', 'total_not_ready_time', 'dialing_time', 'lunch_time',
             'tea_time', 'emergency_time', 'totlogintime', 'total_wrap', 'hold', 'total_notready', 'tea', 'lunch',
             'training', 'bio break(s)', 'talk', 'wrap', 'talk time', 'wrap time', 'hold time', 'bio', 'bio break']

incols = "[LocID],	[ProcessID],	[BusDate],	[Reqiured_Agents],	[Shrikage],	[Attriation],	[Downtime],	" \
         "[Downtime_Reason],	[Abandoned_at_agent],	[Abandoned_at_IVR],	[ACD_Offered],	[ASA],	[ATT],	" \
         "[Non_working_hours_data],	[Occupancy],	[Total_Call_Received_at_IVR],	[SL],	[AL],	" \
         "[LOGIN_DURATION_Avg],	[TRAINING_TIME],	[RING_TIME],	[TOTAL_NOT_READY_TIME],	[DIALING_TIME],	" \
         "[LUNCH_TIME],	[TEA_TIME],	[EMERGENCY_TIME],	[AFD],	[Target_AHT],	[Total_Short_Calls],	[Calls_answered_In_20Sec],	[Calls_answered_In_21_30Sec],	[Calls_answered_In_31_45Sec],	[Calls_answered_In_46_60_Sec],	" \
         "[Calls_answered_In_LessThan_2_Min],	[Calls_answered_In_GreatThan_2_Min],	[Call_Abandoned_in_20Sec],	[Call_Abandoned_In_21_30Sec],	[Call_Abandoned_In_31_45_Sec],	[Call_Abandoned_In_46_60Sec],	[Call_Abandoned_In_LessThan_2_Min],	[Call_Abandoned_In_GreatThan_2_Min],	[Complaint_Call_Service_Issues],	[Kids_Call],	[Langauge_Barrier],	[No_Response],	[Not_Interested],	[Prank_call],	[Wrong_Number],	[Switch_call],	[Calls_Forecasted],	[Location],	[Answered_Calls],	[ProcessName],	[Total_Talk_Time],	[Wrap],	[Hold],	[Wait_Time],	[Not_Taggin],	[Overall_Lead],	[Order_Count],	[Call_to_Order_Conversion],	[Bill_Per_Order],	[Tagging],	[Order_Ammount], [Order_count1], [Total_no_of_calls_closed], [Total_no_of_calls_Open], [Sale], [Avg Handling Time], [Abandoned Percentage],	[FD]"

outcols = "[LocID],	[ProcessID],	[BusDate],	[AgentCount],	[TotalCalls],	[Total_Input],	[Conv_Or_Objective],	[Reqiured_Agents],	[Todays_Target],	[Shrikage],	[Attriation],	[Downtime],	[Downtime_Reason],	[Overall_Leads],	[Unique_Leads],	[Non_Attempted_Cases],	[Booking],	[Wrong_Closure],	[Contacted],	[Unique_Connect],	[Occupancy],	[LOGIN_DURATION_Avg],	[TRAINING_TIME],	[RING_TIME],	[TOTAL_NOT_READY_TIME],	[DIALING_TIME],	[LUNCH_TIME],	[TEA_TIME],	[EMERGENCY_TIME],	[Target_AHT],	[Total_complaint],	[Total_Attempts],	[Disposition_Not_Tagged],	[Non_Contact],	[Orders],	[Complaint_Call_Service_Issues],	[Kids_Call],	[Langauge_Barrier],	[No_Response],	[Not_Interested],	[Prank_call],	[Wrong_Number],	[TOTAL_DIALOUTS],	[Lead],	[ACPA],	[APAD],	[Allocation],	[Location],	[Appointments],	[Met],	[BPO],	[Installation],	[ProcessName],	[Total_Talk_Time],	[Wrap],	[Hold],	[Wait_Time],	[Not_Taggin],	[Punch],	[Not_Tried],	[SR_Count],	[Conversion],	[Service_Activated],	[CANCELLED],	[Pending],	[Pending_For_Cancellation],	[Pending_For_Installation],	[Pending_For_Order_Booking],	[Prospective_Installations],	[Prospective_Pending_Dump],	[OB_CRM_Dispositions],	[OB_Installations],	[Complaints],	[Order_Count],	[Call_to_Order_Conversion],	[Bill_Per_Order],	[Tagging],	[Order_Ammount],	[Order_count1],	[Total_no_of_calls_closed],	[Total_no_of_calls_Open],	[Allocation_Amount_In_CR],	[Collection],	[Paid_count],	[Contacted_paid],	[Outstanding],	[Sale],	[Avg Handling Time]"


def connection():
    try:
        conn = pypyodbc.connect("Driver={SQL Server}; Server=192.168.0.130; Database=ReportAutomationPMS; "
                                "uid=sa;pwd=sa@123;")
        # conn = sqlite3.connect('db.sqlite3')
    except pypyodbc.Error as e:
        print(e)

    return conn


def connection_hrmis():
    try:
        conn = pypyodbc.connect("Driver={SQL Server}; Server=192.168.0.31; Database=HRMIS; "
                                "uid=servicedesk;pwd=Servicedesk@123;")
        # conn = sqlite3.connect('db.sqlite3')
    except pypyodbc.Error as e:
        print(e)

    return conn


def connection_to_mysql():
    try:
        # conn = pymysql.connect(host='172.18.16.145', user='root', passwd='opo@123', db='onetouch',
        #                        cursorclass=pymysql.cursors.DictCursor)
        conn = create_engine('mysql+pymysql://root:opo@123@172.18.16.145/onetouch')
    except Exception as e:
        print(e)

    return conn


def connectionHRMISReport():
    try:
        conn = pypyodbc.connect("Driver={SQL Server}; Server=192.168.0.31; Database=HRMIS_Report; "
                                "uid=sa; pwd=sa@123;")
        # conn = sqlite3.connect('db.sqlite3')
    except pypyodbc.Error as e:
        print(e)

    return conn


def userinfoacces(username,password,domain):
    try:
        token = win32security.LogonUser(
        username,
        domain,
        password,
        win32security.LOGON32_LOGON_NETWORK,
        win32security.LOGON32_PROVIDER_DEFAULT)
        return 1
    except:
        return 0


def login(request):
    try:
        msg = request.msg
    except:
        msg = ""
    return render(request, 'login.html', {'msg': msg})


def dialer_login(request):
    return render(request, 'dialer_login.html')


def register(request):
    return render(request, 'register.html')


def validate(request):
    username = request.POST.dict().get('username')
    password = request.POST.dict().get('password')
    domain= request.POST.dict().get('domain')
    
    valid = userinfoacces(username, password,domain)
    #Uncomment this block to bypass the password
    # request.session['username'] = username.strip()
    # return index2(request)
    ####
    if valid == 1:
        request.session['username'] = username.strip()
        request.session['domain'] = domain.strip()
        return index2(request)
    else:
        request.msg = "Wrong Username or Password"
        return login(request)
    
def validate_User(request):
    username = request.POST.dict().get('username')
    password = request.POST.dict().get('password')
    domain= request.POST.dict().get('domain')
    valid = userinfoacces(username, password,domain)
    if valid == 1:
        return HttpResponse("1")
    else:
        return HttpResponse("0")


def dashboard_data(request):
    conn1 = connection_to_mysql()
    input_type = request.POST.dict().get("src_type[]")
    pro_name = request.POST.dict().get("pro_name")
    pro_uname = request.POST.dict().get("pro_uname")
    pro_password = request.POST.dict().get("pro_password")
    request.session['input_type'] = input_type

    if 'file' in request.FILES:
        file = request.FILES['file']
    else:
        file = ""
    u_type = 'admin'
    msg = ''

    batch_cols = ['rowid', 'smsid', 'processid', 'SourceOfLead', 'LeadDate', 'CityName',
                  'StateName', 'tele_office', 'tele_resi', 'vcno', 'SubscriberName',
                  'ComplaintNo', 'PHONE1', 'PHONE2', 'AlternateNo', 'ZSHName', 'CallCategory', 'Address',
                  'PinCode', 'Locality', 'ResolvedDate', 'NotDoneReason', 'OfferDesc', 'dnc']
    if "xlsx" or "xls" in file:
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)
    raw_cols = df.columns.tolist()
    file_url = default_storage.save('rawfile.csv', file)

    request.session['file_url'] = file_url
    request.session['pro_name'] = pro_name

    if input_type == 'FTP':
        ftp_uname = request.POST.dict().get("ftp_uname")
        ftp_password = request.POST.dict().get("ftp_password")
        ftp_url = request.POST.dict().get("ftp_url")
        ftp_port = request.POST.dict().get("ftp_port")

        input_type_dict = {'username': ftp_uname, 'password': ftp_password, 'url': ftp_url, 'port': ftp_port}
        conn1.execute("INSERT INTO process_master (p_name, p_input_type, p_input_type_values) values ('" + pro_name
                      + "', '" + input_type + "', \"" + str(input_type_dict) + "\")")
    elif input_type == 'API':
        api_url = request.POST.dict().get("api_url")
        api_port = request.POST.dict().get("api_port")
        input_type_dict = {'url': api_url, 'port': api_port}

        conn1.execute("INSERT INTO process_master (p_name, p_input_type, p_input_type_values) values ('" + pro_name
                      + "', '" + input_type + "', '" + str(input_type_dict) + "')")

    elif input_type == 'WEB':
        web_url = request.POST.dict().get("web_url")
        web_uname = request.POST.dict().get("web_uname")
        web_password = request.POST.dict().get("web_password")
        input_type_dict = {'url': web_url, 'username': web_uname, 'password': web_password}

        conn1.execute("INSERT INTO process_master (p_name, p_input_type, p_input_type_values) values ('" + pro_name
                               + "', '" + input_type + "', '" + str(input_type_dict) + "')")

    else:
        email_uname = request.POST.dict().get("email_uname")
        file_name = request.POST.dict().get("file_name")
        input_type_dict = {'username': email_uname, 'file_name': file_name}

        conn1.execute("INSERT INTO process_master (p_name, p_input_type, p_input_type_values) values ('"
                      + str(pro_name)+ "', '" + str(input_type) + "', \"" + str(input_type_dict) + "\")")

    p_id = pd.read_sql_query("SELECT p_id FROM process_master WHERE p_name = '" + str(pro_name) + "'", conn1)
    conn1.execute("INSERT INTO process_user_info (p_id, user_name, password, u_type) values (" + str(p_id['p_id'][0])
                  + ", '" + str(pro_uname) + "', '" + str(pro_password) + "', '" + str(u_type) + "')")

    request.session['p_id'] = int(p_id['p_id'][0])
    request.session['raw_cols'] = raw_cols
    request.session['batch_cols'] = batch_cols

    return render(request, 'data_mapping.html', {'cols': raw_cols, 'batch_cols': batch_cols, 'msg': msg})


def data_mapping(request):
    conn1 = connection_to_mysql()
    p_id = request.session['p_id']
    raw_cols = request.session['raw_cols']
    batch_cols = request.session['batch_cols']
    map_fields = request.POST.dict().get("mapping_data")
    cap_fields = request.POST.getlist("cap[]")
    disp_fields = request.POST.getlist("disp[]")

    conn1.execute("INSERT INTO mapping_master (p_id, cap_fields, disp_fields, raw_fields, batch_fields, "
                  f"map_fields) values ('{str(p_id)}', \"{str(cap_fields)}\", \"{str(disp_fields)}\", \""
                  + str(raw_cols).replace('"', "'") + "\", \"" + str(batch_cols).replace('"', "'")
                  + "\", \"" + str(map_fields) + "\")")

    file_url = BASE_DIR+default_storage.url(request.session['file_url'])
    pro_name = request.session['pro_name']

    if "xlsx" or "xls" in file_url:
        raw_df = pd.read_excel(file_url)
    else:
        raw_df = pd.read_csv(file_url)

    raw_df_trunc = pd.DataFrame(columns=raw_df.columns)
    raw_df_trunc.to_sql('raw_'+pro_name, conn1, if_exists='replace', index=False)
    call_trans_col_list = ['phone', 'conn_id', 'disp_code', 'sub_disp_code', 'sub_sub_disp_code', 'emp_id',
                           'callbacktime', 'cap_data']
    call_trans_df = pd.DataFrame(columns=call_trans_col_list)
    call_trans_df.to_sql('call_trans_data_'+pro_name, conn1, if_exists='replace', index=False)
    batch_cols = request.session['batch_cols']
    batch_df = pd.DataFrame(columns=batch_cols)
    batch_df.to_sql('batch_'+pro_name, conn1, if_exists='replace', index=False)
    request.msg = "Process created successfully"
    return login(request)


def dialer_dash(request):
    conn1 = connection_to_mysql()
    proc = pd.read_sql_query("SELECT p_name FROM process_master", conn1)
    proc_list = proc['p_name'].tolist()

    return render(request, 'dialer_dash.html', {'proc': proc_list})


def raw_to_batch(request):
    conn1 = connection_to_mysql()
    proc = request.POST.dict().get('process[]')
    raw_file = request.FILES['file']

    proc_id = pd.read_sql_query(f"SELECT p_id FROM process_master WHERE p_name = '{str(proc)}'", conn1)

    if '.xls' in str(raw_file):
        raw_df = pd.read_excel(raw_file)
    elif '.csv' in str(raw_file):
        raw_df = pd.read_csv(raw_file)
    else:
        raise Exception

    raw_df.to_sql('raw_'+proc, conn1, if_exists='append', index=False)
    map_fields = pd.read_sql_query(f"SELECT map_fields FROM mapping_master WHERE p_id = {str(proc_id['p_id'][0])}", conn1)
    map_fields_list = map_fields['map_fields'][0].split(",")
    map_fields_list.pop(-1)
    raw_cols = []
    batch_cols = []

    for i in map_fields_list:
        map_col = i.split('::')
        batch_col = map_col[0].strip()
        raw_col = map_col[1].strip()
        raw_cols.append(raw_col)
        batch_cols.append(batch_col)

    cols = ['rowid', 'smsid', 'processid', 'SourceOfLead', 'LeadDate', 'CityName', 'StateName', 'tele_office',
            'tele_resi', 'vcno', 'SubscriberName', 'ComplaintNo', 'PHONE1', 'PHONE2', 'AlternateNo', 'ZSHName',
            'CallCategory', 'Address', 'PinCode', 'Locality', 'ResolvedDate', 'NotDoneReason', 'OfferDesc', 'dnc']

    batch_df = pd.DataFrame(columns=cols)

    for i, j in zip(raw_cols, batch_cols):
        batch_df[j] = raw_df[i]

    batch_df['Address'].replace("[\W]", " ", regex=True, inplace=True)
    batch_df["PHONE1"].fillna("00", inplace=True)
    batch_df["PHONE2"].fillna("00", inplace=True)
    batch_df["PHONE1"] = batch_df.apply(convertphone, axis=1)
    batch_df["AlternateNo"] = batch_df.apply(alternatephone, axis=1)
    batch_df.to_sql("batch_"+proc, conn1, if_exists='append', index=False)

    return HttpResponse("Done "+str(raw_cols)+str(batch_cols))


def graphs_var(conn, camp_count, agent_count):
    fig = go.Figure(data=[go.Pie(labels=camp_count['campaign'], values=camp_count['count_x'])],
                    layout_title_text="CALL COUNT")
    fig2 = go.Figure(data=[go.Bar(x=agent_count['count'], y=agent_count['campaign'], marker_color='crimson',
                                  orientation='h')])
    fig2.update_layout(plot_bgcolor='White')
    fig2.update_xaxes(showgrid=False, zeroline=False)
    fig2.update_yaxes(showgrid=False, zeroline=False)
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
    graph2 = plotly.offline.plot(fig2, auto_open=False, output_type="div")
    camp_count.replace('nan', '0', inplace=True)
    pro_list = pro_list2(conn)

    form = {'graph_div': graph_div, 'graph2': graph2, 'pro_list': pro_list}

    return form


def index(request, time_period):
    try:
        conn = connection()
        if time_period == 'Today':
            yest_date = datetime.now() - timedelta(days=1)
            two_days_before = datetime.now() - timedelta(days=2)
            yest_date_str = yest_date.strftime('%Y%m%d')
            two_days_before_str = two_days_before.strftime('%Y%m%d')
            camp_count, agent_count = single_day(conn, yest_date_str, two_days_before_str)
        else:
            if time_period == 'Week':
                to_date = datetime.now().strftime('%Y%m%d')
                from_date = datetime.now() - timedelta(days=7)
                from_date2 = datetime.now() - timedelta(days=14)
                from_date_str = from_date.strftime('%Y%m%d')
                from_date2_str = from_date2.strftime('%Y%m%d')
            else:
                to_date = datetime.now().strftime('%Y%m%d')
                from_date = datetime.now() - timedelta(days=30)
                from_date2 = datetime.now() - timedelta(days=60)
                from_date_str = from_date.strftime('%Y%m%d')
                from_date2_str = from_date2.strftime('%Y%m%d')
            camp_count, agent_count = many_days(conn, from_date_str, from_date2_str, to_date, '%')

        # listofseries = [pd.Series(['SBI', '452'], index=camp_count.columns),
        #                 pd.Series(['DISHTV', '1102'], index=camp_count.columns)]
        # camp_count = camp_count.append(listofseries, ignore_index=True)
        form = graphs_var(conn, camp_count, agent_count)
        form1 = {'time_period': time_period, 'camp1': camp_count.loc[0, :]['campaign'], 'camp2':
            camp_count.loc[1, :]['campaign'], 'camp3': camp_count.loc[2, :]['campaign'], 'camp4':
            camp_count.loc[3, :]['campaign'], 'count1': camp_count.loc[0, :]['count_x'], 'count2':
            camp_count.loc[1, :]['count_x'], 'count3': camp_count.loc[2, :]['count_x'], 'count4':
            camp_count.loc[3, :]['count_x'], 'diff_percentage1': camp_count.loc[0, :]['diff'],
            'diff_percentage2': camp_count.loc[1, :]['diff'], 'diff_percentage3': camp_count.loc[2, :]['diff'],
            'diff_percentage4': camp_count.loc[3, :]['diff']}
        form.update(form1)
        conn.close()
        return render(request, 'index.html', form)

    except Exception as e:
        print(e)
        request.msg = "Not Enough Data To Analyse"
        return login(request)


def index2(request):
    conn = connection()
    opo_id = request.session['username']
    try:
        emp_id = request.POST.dict().get('emp_id')
        agent_id = request.POST.dict().get('agent_id')
        kpi, role, proc, role_desc, name, loc = get_access(conn, opo_id)
        hrmis_proc = pd.read_sql(f"SELECT SubDept FROM EmpMaster WHERE EmpCode = '{opo_id}'", connection_hrmis())['subdept'][0]
        from_to_date = request.POST.dict().get('daterange')
        selected_proc = request.POST.dict().get('changeproc')

        if role == 'PO':
            multi_proc = proc.split(', ')
            if selected_proc is not None:
                proc = selected_proc
            else:
                try:
                    proc = request.session['proc']
                except:
                    proc = multi_proc[0]
        else:
            multi_proc = []

        footprint(request, conn, opo_id, role, name, proc, loc, "login")

        if from_to_date is not None:
            from_to_date = from_to_date.split('-')
            from_date = from_to_date[0].strip().replace("/", "")
            to_date = from_to_date[1].strip().replace("/", "")
        else:
            to_date = datetime.now().strftime('%Y%m%d')
            from_date_time = datetime.now() - timedelta(days=7)
            from_date = from_date_time.strftime('%Y%m%d')

        if role != 'CH':
            proc_id = int(pd.read_sql(f"SELECT Process_ID FROM [PMS_ProcessMaster] WHERE ProcessName = '{proc}'",
                                  conn)['process_id'][0])
            proc_type = int(pd.read_sql(f"SELECT TOP 1 ProcessType FROM [PMS_ProcessMaster] WHERE ProcessName = '{proc}'", conn)['processtype'][0])
        else:
            proc_type = ''
            proc_id = ''

        try:
            loc_id = int(pd.read_sql(f"SELECT ID FROM PMS_LocationMaster WHERE LocationName = '{loc}'", conn)['id'][0])
        except:
            loc_id = ''

        if 'GGN' in loc:
            loc = '_GGN'
        else:
            loc = ''

        if len(multi_proc) > 1:
            kpi_ids = pd.read_sql(f"SELECT KPI_IDs FROM [PMS_ProcessKPIMapping] WHERE ProcessID = {proc_id} AND OPO_ID = '{opo_id}'", conn)['kpi_ids'][0]
            kpi_extr = pd.read_sql(f"SELECT KPI_Name, ExtractionType FROM PMS_MatricesMaster WHERE ID in ({kpi_ids})", conn)
            kpi = ", ".join([f"{j}([{i}]) AS '{i}'" for i, j in zip(kpi_extr['kpi_name'].to_list(),
                                                                    kpi_extr['extractiontype'].to_list())])

        if role != 'TR':
            if role == 'CH':
                metrics_dict, emp_list = get_data_ch(conn, from_date, to_date, kpi, loc, loc_id)
            elif role == 'PO':
                external_kpi_form, metrics_dict = get_data_po(conn, proc_id, from_date, to_date, kpi, loc, loc_id)
            elif 'MGR' in role:
                if role == 'SMGR':
                    emp_list = getMgrList(conn, opo_id, loc)
                else:
                    emp_list = getTlList(conn, opo_id, loc)
                external_kpi_form, metrics_dict = get_data_mgr(opo_id, proc_id, from_date, to_date, agent_id, emp_id, role, kpi, loc, loc_id)
            elif role == 'TL':
                emp_list = getAgentList(conn, opo_id, loc)
                if len(str(emp_id)) > 4:
                    metrics_dict = for_agent(conn, from_date, to_date, proc_id, kpi, emp_id, role, loc)
                else:
                    metrics_dict = for_TL(conn, from_date, to_date, proc_id, kpi, emp_id, role, opo_id, loc)
                    del metrics_dict['metrics_data']['sl']
                    del metrics_dict['metrics_data']['al']
            else:
                metrics_dict = for_agent(conn, from_date, to_date, proc_id, kpi, opo_id, role, loc)

            if proc_type == 1 and 'MGR' in role and len(str(agent_id)) <= 4:
                del metrics_dict['metrics_data']['sl']
                del metrics_dict['metrics_data']['al']

            if role != 'PO':
                metrics_graphs = {}
                for col in metrics_dict['call_count'].columns:
                    if col not in ['date', 'agent count', 'processname']:
                        color = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                        if role != 'CH':
                            metrics_graphs[col] = graphs.bar(metrics_dict['call_count']['date'], metrics_dict['call_count'][col],
                                                         '#' + color, 'v', col.title())
                        else:
                            metrics_graphs[col] = graphs.multi_bar(metrics_dict['call_count']['date'], metrics_dict['call_count'][[col, 'processname']],
                                                             '#' + color, 'v', col.title())
                if role != 'TR':
                    for col in metrics_dict['metrics_data'].columns:
                        if col in time_cols:
                            metrics_dict['metrics_data'][col] = pd.to_datetime(metrics_dict['metrics_data'][col], unit='s').dt.strftime("%H:%M:%S")
            else:
                metrics_graphs = ''

            metrics_data_t = metrics_dict['metrics_data'].T.reset_index()
            metrics_data_t.rename(columns={'index': 'Metric'}, inplace=True)
            metrics_data_t.fillna(0, inplace=True)

            if role == 'PO':
                for kpi in metrics_data_t['Metric'].to_list():
                    if kpi != 'date':
                        color = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
                        external_kpi_form['external_kpi_graph'][kpi] = graphs.line(metrics_dict['metrics_data']['date'],
                                metrics_dict['metrics_data'][kpi.lower()], '#' + color, 'lines+markers', kpi.title())

            metrics_data_t['Metric'] = metrics_data_t['Metric'].str.upper()

            if len(str(agent_id)) <= 4 and 'MGR' in role:
                agent_count_graph = graphs.bar(metrics_dict['call_count']['agent count'],
                                               metrics_dict['call_count']['date'], 'brown', 'h', "Agent Count")
            elif role == 'TL' and len(str(emp_id)) <= 4:
                agent_count_graph = graphs.bar(metrics_dict['call_count']['agent count'],
                                               metrics_dict['call_count']['date'], 'brown', 'h', "Agent Count")
            else:
                agent_count_graph = ""

                if (role == 'AGT') or (role == 'PO'):
                    emp_list = ""

            if ('MGR' in role) and (len(str(agent_id)) == 4) and proc_type == 0:
                sl_graph = graphs.line(metrics_dict['metrics_data']['date'], metrics_dict['metrics_data']['sl'], 'blue', 'lines+markers', "SL")
                al_graph = graphs.line(metrics_dict['metrics_data']['date'], metrics_dict['metrics_data']['al'], 'green', 'lines+markers', "AL")
            else:
                sl_graph = ""
                al_graph = ""

            metrics = metrics_data_t.to_html(index=False, header=False, classes="table table-hover table-dark", border=0)

            if emp_id is None:
                if 'MGR' in role:
                    emp_id = ""
                else:
                    emp_id = ""
            if agent_id is None:
                agent_id = ""

            kpi_list = ['Staff Time(S)', 'Login Time(S)', 'AUX Time(s)', 'Talk Time(S)', 'Avg talk Time', 'Inbound_talk',
                        'OB talk time', 'Hold Time(s)', 'ACW Time(s)', 'inbound_wrap', '[OB Wrap Time', 'Avg Handle Time',
                        'Answered Calls', 'Answered Calls <10Sec', 'Answered Calls <30Sec', 'OB ACHT', 'TotDaysInCompany',
                        'TotLoginTime']

            form = {'metrics_data': metrics, 'proc': proc, 'metrics_graphs': metrics_graphs, 'agent_count_graph':
                    agent_count_graph, 'sl': sl_graph, 'al': al_graph, 'emp_list': emp_list, 'time_period': 'Daterange',
                    'role': role, 'emp_id': emp_id, 'agent_id': agent_id, 'startdate': from_date, 'enddate': to_date,
                    'opo_id': opo_id, 'role_desc': role_desc, 'name': name, 'kpi_list': kpi_list, 'proc_type':
                    proc_type, 'hrmis_proc': hrmis_proc}
        else:
            form = {'role': role, 'role_desc': role_desc, 'name': name, 'startdate':
                     from_date, 'enddate': to_date}

        if role == 'TL' or role == 'TR':
            assigned_ap = pd.read_sql(f"SELECT DISTINCT Actionplanid, mm.KPI_Name, pm.ProcessName, ApForOPO FROM "
                                         f"PMS_Actionplan a LEFT JOIN [PMS_Actionplan_What] b ON a.Actionplanid = "
                                         f"b.Parent_action_ID LEFT JOIN PMS_Actionplan_When c ON a.Actionplanid = "
                                         f"c.Parent_action_ID LEFT JOIN PMS_MatricesMaster mm ON a.Kpi_ID = mm.ID LEFT"
                                         f" JOIN PMS_ProcessMaster pm ON a.Process_ID = pm.Process_ID WHERE "
                                         f"b.Assignee_Opo_ID LIKE '%{opo_id}%'", conn)
            # if len(assign_kpi_ids) > 0:
            #     assign_kpi_ids_str = ["'"+str(k)+"'" for k in assign_kpi_ids]
            #     assign_kpi = pd.read_sql(f"SELECT KPI_Name FROM PMS_MatricesMaster WHERE ID IN ({', '.join(assign_kpi_ids_str)})",
            #                              conn)['kpi_name'].to_list()
            #     assign_proc_ids = pd.read_sql(f"SELECT DISTINCT Process_ID FROM [PMS_Actionplan] WHERE ApForOPO = "
            #                               f"'{opo_id}'", conn)['process_id'].to_list()
            #     assign_proc_ids_str = ["'"+str(p)+"'" for p in assign_proc_ids]
            #     assign_proc = pd.read_sql(f"SELECT ProcessName FROM PMS_ProcessMaster WHERE Process_ID IN "
            #                               f"({', '.join(assign_proc_ids_str)})", conn)['processname'].to_list()
            form.update({'assigned_ap': assigned_ap})

        if role != 'AGT' and role != 'TR':
            attr_data = get_attr_data(conn, opo_id, role, from_to_date, 'summary')
            attr_data_graph = graphs.multi_line(attr_data['sdate'],
                                                  attr_data.iloc[:, 2:], 'lines+markers', 'Attrition Info')

            notifs = get_notifs(conn, opo_id, role)
            form.update({'notifs': notifs})
            if role == 'PO':
                not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                                 "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                                 f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
                form.update({'nac': not_approved_count, 'multi_proc': multi_proc, 'form_type': 'index'})
            form.update({'attr_data_graph': attr_data_graph})

        if 'MGR' in role or role == 'PO':
            form.update(external_kpi_form)

        create_session(request, from_date, to_date, emp_id, role, agent_id, name, role_desc, proc, from_to_date,
                       proc_type, proc_id, loc, hrmis_proc, multi_proc, emp_list, loc_id)

        conn.close()
        return render(request, 'index.html', form)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        try:
            get_designation = pd.read_sql("SELECT CurrentDesignation, CurrentLocation FROM "
                                          f"[192.168.0.31].[HRMIS].[DBO].EmpMaster WHERE EmpCode = '{opo_id}'", conn)
            designation = get_designation['currentdesignation'][0]
            cur_loc = get_designation['currentlocation'][0]
            request.session['cur_loc'] = cur_loc
            if designation in agent_desig:
                return agent_register(request)

        except Exception as e:
            print(e)

        request.msg = "User is not registered"
        return login(request)



def agent(request):
    conn = connection()
    # todays_date = datetime.now().strftime('%Y-%m-%d')
    back_date = datetime.now() - timedelta(days=1)
    back_date_str = back_date.strftime('%Y-%m-%d')
    to_date = datetime.now().strftime('%Y%m%d')
    from_date = datetime.now() - timedelta(days=7)
    from_date_str = from_date.strftime('%Y-%m-%d')
    agent_count = pd.read_sql_query("SELECT Date, COUNT(AGENT_ID) AS 'COUNT' FROM PMS_AgentRelatedInfo WHERE "
                                    f"CONVERT(varchar, [BIOLoginDate], 112) BETWEEN '{from_date_str}' AND '{to_date}' "
                                    f" GROUP BY Date", conn)
    agent_gender = pd.read_sql_query("SELECT AGENT_GENDER, COUNT(*) AS 'COUNT' FROM PMS_AgentRelatedInfo GROUP BY "
                                     "AGENT_GENDER", conn)
    aht = pd.read_sql_query("SELECT TOP 10 [Avg Handle Time], Agent_ID  FROM PMS_AgentRelatedInfo WHERE Date = "
                            f"'{back_date_str}' AND [Avg Handle Time] != 0  ORDER BY [Avg Handle Time] ASC", conn)
    tl_per_head_cnt = pd.read_sql_query("SELECT TOP 15 COUNT(*) AS 'COUNT', TLName FROM PMS_AgentRelatedInfo WHERE Date"
                                        f" = '{back_date_str}' AND TLName != '' AND TLName IS NOT NULL GROUP BY TLName "
                                        f"ORDER BY 'COUNT' DESC", conn)

    agent_count['date'] = pd.to_datetime(agent_count['date'])
    ac_graph = graphs.bar(agent_count['date'], agent_count['count'], '#6d4c41', 'v', "Agent Count")
    tlphc_graph = graphs.line(tl_per_head_cnt['tlname'], tl_per_head_cnt['count'], '#f57f17', 'lines', "TL Per Head Count")
    ag_graph = graphs.pie(agent_gender['agent_gender'], agent_gender['count'], 0, "Agent Gender")
    aht_graph = graphs.line(aht['agent_id'], aht['avg handle time'], 'crimson', 'markers', "AHT")
    conn.close()

    return render(request, 'agent.html', {'graph2': ac_graph, 'graph': ag_graph, 'aht_graph': aht_graph, 'tlphc_graph': tlphc_graph})


def process(request):
    conn = connection()
    to_date = datetime.now().strftime('%Y%m%d')
    from_date = datetime.now() - timedelta(days=7)
    from_date_str = from_date.strftime('%Y%m%d')
    agent_count = pd.read_sql_query("SELECT Date, COUNT(AGENT_ID) AS 'COUNT' FROM PMS_AgentRelatedInfo WHERE "
                                    f"CONVERT(varchar, [BIOLoginDate], 112) BETWEEN '{from_date_str}' AND '{to_date}' "
                                    f" GROUP BY Date", conn)

    call_count = pd.read_sql_query("SELECT CONVERT(varchar, CALL_DATE, 112) AS 'Date', COUNT(*) AS 'COUNT' FROM "
                                   "PMS_CallReltdInfoMaster WHERE CONVERT(varchar, CALL_DATE, 112) BETWEEN "
                                   f"'{from_date_str}' AND '{to_date}' GROUP BY "
                                   "CONVERT(varchar, CALL_DATE, 112)", conn)

    agent_count['date'] = pd.to_datetime(agent_count['date'])
    call_count['date'] = pd.to_datetime(call_count['date'])

    ac_graph = graphs.bar(agent_count['date'], agent_count['count'], 'crimson', 'v', "Agent Count")
    cc_graph = graphs.bar(call_count['count'], call_count['date'], '#673ab7', 'h', "Call Count")
    conn.close()

    return render(request, 'process.html', {'graph2': ac_graph, 'graph_div': cc_graph})


def call(request):
    conn = connection()
    back_date = datetime.now() - timedelta(days=1)
    back_date_str = back_date.strftime('%Y%m%d')
    to_date = datetime.now().strftime('%Y%m%d')
    from_date = datetime.now() - timedelta(days=7)
    from_date_str = from_date.strftime('%Y-%m-%d')
    call_count = pd.read_sql_query("SELECT CONVERT(varchar, CALL_DATE, 112) AS 'DATE', COUNT(*) AS 'COUNT' FROM "
                                    "PMS_CallReltdInfoMaster WHERE CONVERT(varchar, CALL_DATE, 112) BETWEEN "
                                    f"'{from_date_str}' AND '{to_date}' GROUP BY CONVERT(varchar, CALL_DATE, 112)", conn)
    mode_dist = pd.read_sql_query("SELECT Mode, COUNT(*) AS 'COUNT' FROM [dbo].[PMS_CallReltdInfoMaster] WHERE "
                                  f"CONVERT(varchar, CALL_DATE, 112) = '{back_date_str}' GROUP BY MODE", conn)
    aht = pd.read_sql_query("SELECT TOP 10 [Avg Handle Time], Agent_ID  FROM PMS_AgentRelatedInfo WHERE Date = "
                            f"'{back_date_str}' AND [Avg Handle Time] != 0  ORDER BY [Avg Handle Time] ASC", conn)
    tl_per_head_cnt = pd.read_sql_query("SELECT TOP 15 COUNT(*) AS 'COUNT', TLName FROM PMS_AgentRelatedInfo WHERE Date"
                                        f" = '{back_date_str}' AND TLName != '' AND TLName IS NOT NULL GROUP BY TLName "
                                        f"ORDER BY 'COUNT' DESC", conn)

    call_count['date'] = pd.to_datetime(call_count['date'])
    ac_graph = graphs.bar(call_count['count'], call_count['date'], '#424242', 'h', "Agent Count")
    tlphc_graph = graphs.line(tl_per_head_cnt['tlname'], tl_per_head_cnt['count'], '#f57f17', 'lines', "TL Per Head Count")
    md_graph = graphs.pie(mode_dist['mode'], mode_dist['count'], 0, "Mode Distribution")
    aht_graph = graphs.line(aht['agent_id'], aht['avg handle time'], 'crimson', 'markers', "AHT")
    conn.close()

    return render(request, 'call.html', {'graph2': ac_graph, 'graph': md_graph, 'aht_graph': aht_graph, 'tlphc_graph': tlphc_graph})


def excopy(request):
    return render(request, 'excopy.html')


def dyn_reports(request, rep_type):
    conn = connection()
    opo_id = request.session['username']
    proc_type = request.session['proc_type']
    loc = request.session['loc']
    kpi, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']
    proc_id = int(pd.read_sql(f"SELECT TOP 1 Process_id FROM PMS_ProcessMaster WHERE ProcessName = '{proc}'", conn)['process_id'][0])

    '''
    if rep_type == 'Agent':
        table = 'PMS_AgentRelatedInfo'+loc
        if role == 'TL':
            where = f"WHERE TLName = '{opo_id}' AND process_id = '{int(proc_id)}'"
        else:
            where = f"WHERE MgrName = '{opo_id}' AND process_id = '{int(proc_id)}'"
    elif rep_type == 'Call':
        table = 'PMS_CallReltdInfoMaster'+loc
        where = f'WHERE ProcessID = {int(proc_id)}'
    else:
        table = 'PMS_ProcessWiseActMaster'+loc
        where = f'WHERE ProcessID = {int(proc_id)}'
        process_type = pd.read_sql(f"SELECT processtype FROM [PMS_ProcessMaster] WHERE Process_ID = {proc_id}", conn)['processtype'][0]
        if process_type == 0:
            tcols = pd.read_sql_query(f"SELECT TOP 1 {incols} FROM {table} {where}", conn)
        else:
            tcols = pd.read_sql_query(f"SELECT TOP 1 {outcols} FROM {table} {where}", conn)

    request.session['table'] = table
    request.session['where'] = where
    request.session['proc_id'] = proc_id

    #0 is for Inbound and 1 is for Outbound
    if rep_type != 'Process':
        tcols = pd.read_sql_query(f"SELECT TOP 1 * FROM {table} {where}", conn)

    conn.close()
    
    tcols1 = []
    for col in tcols.columns.to_list():
        tcols1.append(col.replace("(", "-").replace(")", "*"))
        if 'id' in col:
            del tcols[col]

    coldict = {}
    for i in range(len(list(tcols.columns))):
        coldict[tcols.columns[i]] = tcols.iloc[:, i].tolist()
    '''
    form = {'rep_type': rep_type, 'tcols': 'tcols1', 'coldict': 'coldict', 'opo_id': opo_id,'role_desc': role_desc,
            'name': name, 'role': role, 'proc_type': proc_type, 'hrmis_proc': hrmis_proc, 'proc': proc, 'multi_proc':
            multi_proc}

    return render(request, 'dyn_reports.html', form)


def compare(request, emp_type):
    conn = connection()
    opo_id = request.session['username']
    loc = request.session['loc']
    loc_id = request.session['loc_id']
    hrmis_proc = request.session['hrmis_proc']
    request.session['emp_type'] = emp_type
    kpi, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    multi_proc = request.session['multi_proc']
    emp_list = request.session['emp_list']

    if emp_type == 'Process':
        if role == 'PO':
            emp_list = multi_proc
        kpi_detail = pd.read_sql("SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Proc' "
                                     "ORDER BY ID ASC", conn)
        kpi_list = [str(int(i)) + ". " + str(j) for i, j in
                    zip(kpi_detail["id"].to_list(), kpi_detail["kpi_name"].to_list())]
    elif emp_type == 'MGR':
        # emp_list = getMgrList(conn, opo_id, loc)
        kpi_detail = pd.read_sql("SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Agent' "
                                     "OR KPI_Type = 'BOTH' ORDER BY ID ASC", conn)
        kpi_list = [str(int(i)) + ". " + str(j) for i, j in
                    zip(kpi_detail["id"].to_list(), kpi_detail["kpi_name"].to_list())]
    elif emp_type == 'Agent':
        emp_list = getAgentListComp(conn, opo_id, role, loc)
        # emp_list = getTlList(conn, opo_id, loc)


    try:
        msg = request.msg
    except:
        msg = ''

    to_date = datetime.now().strftime('%Y%m%d')
    from_date_time = datetime.now() - timedelta(days=7)
    from_date = from_date_time.strftime('%Y%m%d')

    form = {'startdate': from_date, 'enddate': to_date, 'emp_list': emp_list, 'opo_id': opo_id, 'role_desc': role_desc,
            'name': name, 'role': role, 'emp_type': emp_type, 'msg': msg, 'proc': proc, 'hrmis_proc': hrmis_proc,
            'multi_proc': multi_proc}

    if role not in ['AGT', 'TR', 'CH']:
        notifs = get_notifs(conn, opo_id, role)
        form.update({'notifs': notifs})
        if role == 'PO':
            not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                             f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
            form.update({'nac': not_approved_count})
    if emp_type != 'MGR' and emp_type != 'Process':
        return render(request, 'compare.html', form)
    else:
        form.update({'kpi_list': kpi_list})
        return render(request, 'compare2.html', form)


def compare_data(request):
    conn = connection()
    emp_type = request.session['emp_type']
    try:
        opo_id = request.session['username']
        loc = request.session['loc']
        loc_id = request.session['loc_id']
        hrmis_proc = request.session['hrmis_proc']
        emps = request.POST.getlist('emps[]')
        from_to_date = request.POST.dict().get('comdaterange')
        date_list = from_to_date.split('-')
        from_date = date_list[0].strip().replace("/", "")
        to_date = date_list[1].strip().replace("/", "")
        kpi, role, _, role_desc, name, _ = get_access(conn, opo_id)
        proc = request.session['proc']
        multi_proc = request.session['multi_proc']
        emp_list = request.session['emp_list']

        if emp_type == 'MGR' or emp_type == 'Process':
            if emp_type == 'MGR':
                kpi_detail = pd.read_sql("SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Agent' "
                                     "OR KPI_Type = 'BOTH' ORDER BY ID ASC", conn)
            else:
                kpi_detail = pd.read_sql(
                    "SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Proc' "
                    "ORDER BY ID ASC", conn)
            kpi_list = [str(int(i)) + ". " + str(j) for i, j in
                        zip(kpi_detail["id"].to_list(), kpi_detail["kpi_name"].to_list())]
            kpis = request.POST.getlist('kpis[]')
            if emp_type == 'MGR':
                compare_data_dict, disp_dict = get_compare_data_mgr(conn, from_date, to_date, emps, loc, kpis)
            else:
                if role == 'PO':
                    emp_list = multi_proc
                compare_data_dict, disp_dict = get_compare_data_proc(conn, from_date, to_date, emps, loc, kpis)
        elif emp_type == "TL":
            # emp_list = getTlList(conn, opo_id, loc)
            compare_data_dict, disp_dict = get_compare_data_tl(conn, from_date, to_date, emps, opo_id, loc)
            agent_count_dict = {}

            for key, value in compare_data_dict.items():
                agent_count_dict[key] = value['agent count']

            if len(compare_data_dict) != 0:
                agent_count_graph = graphs.multi_line(compare_data_dict[list(compare_data_dict.keys())[0]]['date'], agent_count_dict, 'lines+markers', 'Agent Count')
            else:
                agent_count_graph = ""
        else:
            emp_list = getAgentListComp(conn, opo_id, role, loc)
            compare_data_dict, disp_dict = get_compare_data_agent(conn, from_date, to_date, emps, opo_id, role, loc)

        if emp_type == 'MGR' or emp_type == 'Process':
            data_dict = {}
            graph_dict = {}
            key_list = list(compare_data_dict.keys())

            for col in compare_data_dict[key_list[0]].columns:
                up_col = col.upper()
                data_dict[up_col] = {}
                if col not in ['manager', 'date', 'process']:
                    for key, value in compare_data_dict.items():
                        data_dict[up_col][key] = value[col]

                    if len(compare_data_dict) > 0:
                        graph_dict[up_col] = graphs.multi_line(compare_data_dict[list(compare_data_dict.keys())[0]]['date'], data_dict[up_col],
                                                  'lines+markers', up_col)

            form = {'graph_dict': graph_dict}
        else:
            aht_dict = {}
            call_count_dict = {}
            for key, value in compare_data_dict.items():
                aht_dict[key] = value['aht']
                call_count_dict[key] = value['call count']

            if len(compare_data_dict) > 0:
                aht_graph = graphs.multi_line(compare_data_dict[list(compare_data_dict.keys())[0]]['date'], aht_dict, 'lines+markers', 'AHT')
                call_count_graph = graphs.multi_line(compare_data_dict[list(compare_data_dict.keys())[0]]['date'], call_count_dict, 'lines+markers', 'Call Count')
            else:
                aht_graph = ""
                call_count_graph = ""

            form = {'aht_graph': aht_graph, 'call_count_graph': call_count_graph}

        for key, value in compare_data_dict.items():
            for col in value.columns:
                if col in time_cols:
                    value[col] = pd.to_datetime(value[col], unit='s').dt.strftime("%H:%M:%S")
                elif col in int_cols:
                    value[col] = value[col].astype(int)

            value.columns = value.columns.str.upper()
            compare_data_dict[key] = value[value.columns[0:-2]].to_html(index=False,
                                                                       classes="table table-hover table-dark "
                                                                               "datashow", border=0)

        for key, value in disp_dict.items():
            for col in value.columns:
                if col in time_cols:
                    value[col] = pd.to_datetime(value[col], unit='s').dt.strftime("%H:%M:%S")
            value.columns = value.columns.str.upper()
            disp_dict[key] = value.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

        form.update({'startdate': from_date, 'enddate': to_date, 'emp_list': emp_list, 'compare_data': compare_data_dict,
                'opo_id': opo_id, 'role_desc': role_desc, 'name': name, 'role': role, 'emp_type': emp_type,
                'from_to_date': from_to_date.replace("-", " to "), 'disp_dict': disp_dict, 'proc': proc,
                'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc})

        if role not in ['AGT', 'TR', 'CH']:
            notifs = get_notifs(conn, opo_id, role)
            form.update({'notifs': notifs})
            if role == 'PO':
                not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                                 "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                                 f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
                form.update({'nac': not_approved_count})

        if emp_type == 'TL':
            form.update({'agent_count_graph': agent_count_graph})

        if emp_type == 'MGR' or emp_type == 'Process':
            form.update({'kpi_list': kpi_list})
            return render(request, 'compare2.html', form)
        else:
            return render(request, 'compare.html', form)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        request.msg = "No data or no employee selected"
        return compare(request, emp_type)


def get_agent_list(request):
    conn = connection()
    loc = request.session['loc']
    tl_id = request.POST.dict().get('tl_id')
    emp_list = getAgentList(conn, tl_id, loc)
    return HttpResponse(','.join(emp_list))


def disp_ajax(request):
    conn = connection()
    opo_id = request.session['username']
    from_date = request.session['from_date']
    to_date = request.session['to_date']
    emp_id = request.session['emp_id']
    agent_id = request.session['agent_id']
    role = request.session['role']
    proc_id = request.session['proc_id']
    loc = request.session['loc']

    disp = get_disp(conn, from_date, to_date, emp_id, opo_id, role, agent_id, proc_id, loc)
    disp = disp.replace('0', 'Okay')
    # sub_disp = sub_disp.replace('0', 'Okay')
    disp.columns.values[3] =  disp.columns.values[3] + ' (seconds)'
    disp.columns =  disp.columns.str.upper()
    # sub_disp.columns =  sub_disp.columns.str.upper()
    disp = disp.to_html(index=False, classes="table table-hover table-dark datashow", border=0)
    # sub_disp = sub_disp.to_html(index=False, classes="table table-hover table-dark", border=0)

    return HttpResponse(disp)


def ajax_reports(request):
    conn = connection()
    cols = request.POST.dict().get('cols')
    # filterval = request.POST.dict().get('filterval')
    fdate = request.POST.dict().get('fdate')
    tdate = request.POST.dict().get('tdate')

    type='report'
    cols = cols[:-1].replace('~', ", ")
    # filterval = filterval[:-4]
    request.session['fdate'] = fdate
    request.session['tdate'] = tdate

    table = request.session['table']
    where = request.session['where']
    proc_id = request.session['proc_id']

    report = get_report(conn, cols, table, fdate, tdate, where, type, proc_id)
    conn.close()

    request.session['cols'] = cols
    # request.session['filterval'] = filterval

    # request.report = report
    report =report.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    return HttpResponse(report)


def export(request):
    conn = connection()
    formatted_date = datetime.now().strftime('%Y-%m-%d')
    cols = request.session['cols']
    # filterval = request.session['filterval']
    table = request.session['table']
    where = request.session['where']
    fdate = request.session['fdate']
    tdate = request.session['tdate']
    proc_id = request.session['proc_id']

    type = 'export'
    report = get_report(conn, cols, table, fdate, tdate, where, type, proc_id)
    conn.close()

    filename = BASE_DIR + f"/media/report-{str(formatted_date)}.xls"
    report.to_excel(filename, index=False)
    if os.path.exists(filename):
        with open(filename, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
    raise Http404


def base(request):
    return render(request, 'base.html')


def kpi(request):
    conn = connection()
    opo_id = request.session['username']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    proc_id = request.session['proc_id']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']

    kpi = pd.read_sql("SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Agent' OR KPI_Type = "
                      "'BOTH' ORDER BY ID ASC", conn)
    proc_df = pd.read_sql("SELECT Process_ID, ProcessName FROM PMS_ProcessMaster ORDER BY Process_ID ASC", conn)
    target_kpi = pd.read_sql("SELECT b.ProcessName, c.KPI_Name, a.* FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID LEFT JOIN PMS_MatricesMaster c ON "
                             f"a.kpi_id = c.ID WHERE b.ProcessName = '{proc}'", conn)

    kpi_list = [str(int(i))+". "+str(j)+f" ({k})" for i, j, k in zip(kpi["id"].to_list(), kpi["kpi_name"].to_list(), kpi["kpi_unit"].to_list())]
    proc_list = [str(int(i))+". "+str(j) for i, j in zip(proc_df["process_id"].to_list(), proc_df["processname"].to_list())]
    today = datetime.now()
    nextday = (today+timedelta(days=1)).strftime("%Y-%m-%d")
    # target_kpi = target_kpi.to_html(index=False, classes="table table-hover table-dark datashow", border=0)
    target_kpi.is_approved = target_kpi.is_approved.replace({0: 'Not Approved', 1: 'Approved'})
    target_kpi['from_date'] = pd.to_datetime(target_kpi['from_date']).dt.strftime('%d %B, %Y')
    target_kpi['to_date'] = pd.to_datetime(target_kpi['to_date']).dt.strftime('%d %B, %Y')

    if role == 'TL':
        target_kpi = target_kpi[target_kpi['is_approved']=='Approved']

    kpi_ref_table = pd.read_sql(f"SELECT b.ProcessName, c.KPI_Name, a.* FROM [PMS_KPI_REF] a LEFT JOIN "
                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID LEFT JOIN PMS_MatricesMaster c ON "
                             f"a.kpi_id = c.ID WHERE b.ProcessName = '{proc}'", conn)
    # del kpi_ref_table['id']
    # kpi_ref_table = kpi_ref_table.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    form = {'kpi_list': kpi_list, 'proc_list': proc_list, 'role_desc': role_desc, 'name': name, 'proc': proc, 'proc_id':
        str(proc_id)+'. '+proc, 'target_kpi': target_kpi, 'role': role, 'nextday': nextday, 'kpi_ref_table':
        kpi_ref_table, 'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc}

    if role != 'AGT' and role != 'TR':
        notifs = get_notifs(conn, opo_id, role)
        form.update({'notifs': notifs})
        if role == 'PO':
            not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                             f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
            form.update({'nac': not_approved_count})

    return render(request, 'kpi.html', form)


def kpi_add(request):
    conn = connection()
    loc = request.POST.dict().get("loc")
    proc = request.POST.dict().get("process")
    kpi = request.POST.dict().get("kpi")
    tenurity = request.POST.dict().get("tenurity")
    target = request.POST.dict().get("target")
    tolerance_val = request.POST.dict().get("tolerance_val")
    fdate = request.POST.dict().get("fdate")
    tdate = request.POST.dict().get("tdate")
    opo_id = request.session['username']
    role = request.session['role']

    if proc is not None:
        proc_id = proc.split(".")[0]
    else:
        proc_id = ""

    if kpi is not None:
        kpi_id = kpi.split(".")[0]
    else:
        kpi_id = ""

    kpi_available = pd.read_sql(f"SELECT * FROM [PMS_Target_Process_KPI] WHERE kpi_id = '{kpi_id}' AND process_id = '{proc_id}' "
                              f"AND location = '{loc}' AND tenurity = '{tenurity}'  AND CONVERT(DATE, to_date) > '{fdate}'", conn)
    today = datetime.now().date()
    from_date = datetime.strptime(fdate, '%Y-%m-%d').date()

    if kpi_available.shape[0] == 0 and from_date > today:
        conn.cursor().execute("INSERT INTO PMS_Target_Process_KPI (location, process_id, kpi_id, tenurity, target, "
                              f"from_date, to_date, emp_code, role_code, tolerance_val) values ('{loc}', '{proc_id}', '{kpi_id}', "
                              f"'{tenurity}', '{target}', '{fdate}', '{tdate}', '{opo_id}', '{role}', {tolerance_val})")
        conn.commit()
        msg = "KPI added"
    else:
        msg = f"KPI exists or invalid date selected"

    conn.close()

    return HttpResponse(msg)


def action_plan(request):
    conn_hrmis = connection_hrmis()
    user_list = get_userlist(conn_hrmis)
    conn = connection()
    opo_id = request.session['username']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    from_date = request.session['from_date']
    to_date = request.session['to_date']
    loc = request.session['loc']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']

    try:
        try:
            notif_id = request.notif_id
        except:
            notif_id = ""

        conn.cursor().execute(f"UPDATE PMS_NotificationFlag SET InApp_Status=1 WHERE ID = {notif_id.split('. ')[0]}")
        conn.commit()

        notif_data = pd.read_sql(f"SELECT * FROM PMS_NotificationFlag WHERE id = {notif_id.split('. ')[0]}", conn)
        kpi_data = pd.read_sql_query(f"SELECT ExtractionType, id FROM [PMS_MatricesMaster] WHERE kpi_name = "
                                     f"'{notif_data['kpi_name'][0][1:-1]}'", conn)
        ext_type = kpi_data['extractiontype'][0]
        tar_tol = pd.read_sql(f"SELECT target, tolerance_val FROM PMS_Target_Process_KPI WHERE "
                              f"kpi_id = {kpi_data['id'][0]} AND process_id = {notif_data['processid'][0]} AND "
                              f"'{str(notif_data['busdate'][0]).split(' ')[0]}' BETWEEN from_date AND to_date", conn)

        if role == 'TL':
            hist_query = f"SELECT DATE, {notif_data['kpi_name'][0]} AS '{notif_data['kpi_name'][0][1:-1]}' FROM " \
                         f"[PMS_AgentRelatedInfo{loc}] WHERE Agent_ID = '{notif_data['agentopo'][0]}' AND " \
                         f"CONVERT(varchar, CONVERT(DATE, DATE), 112) BETWEEN '{from_date}' AND '{to_date}'"
        else:
            hist_query = f"SELECT DATE, {ext_type}({notif_data['kpi_name'][0]}) AS '{notif_data['kpi_name'][0][1:-1]}'" \
                f" FROM [PMS_AgentRelatedInfo{loc}] WHERE TLName = '{notif_data['tl_opo'][0]}' AND CONVERT(varchar, " \
                f"CONVERT(DATE, DATE), 112) BETWEEN '{from_date}' AND '{to_date}' GROUP BY DATE"

        hist = pd.read_sql(hist_query, conn)
        hist['avg handle time'] = pd.to_datetime(hist['avg handle time'], unit='s').dt.strftime("%H:%M:%S")
        hist = hist.to_html(index=False, border=0, classes="table table-hover table-dark datashow")

        try:
            tar_tol_val = tar_tol.iloc[0]
        except:
            tar_tol_val = ""
        today = datetime.now().strftime("%Y-%m-%d")
        form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'notif_id': notif_id, 'tar_tol': tar_tol_val,
                'role': role, 'user_list': user_list, 'notif_data': notif_data, 'hist': hist, 'today': today,
                'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc}

        if role != 'AGT' and role != 'TR':
            notifs = get_notifs(conn, opo_id, role)
            form.update({'notifs': notifs})
            if role == 'PO':
                not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                                 "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                                 f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
                form.update({'nac': not_approved_count})

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'user_list': user_list, 'hrmis_proc':
            hrmis_proc, 'multi_proc': multi_proc,'notif_id':notif_id}

    return render(request, 'action_plan.html', form)


def save_aplan(request):
    conn = connection()
    cur_date = datetime.now().strftime("%Y-%m-%d")
    opo_id = request.session['username']
    wh_cmnt = request.POST.dict().get("wh_cmnt")
    hts_cmnt = request.POST.dict().get("hts_cmnt")
    dept = request.POST.getlist("dept[]")
    user = request.POST.getlist("user[]")
    what_to_do = request.POST.dict().get("what_to_do")
    total_goal = request.POST.getlist("total_goal[]")
    notif_id = request.POST.dict().get("notif_id")

    role = request.session['role']
    proc = request.session['proc']
    proc_id = pd.read_sql(f"SELECT Process_ID FROM PMS_ProcessMaster WHERE ProcessName = '{proc}'", conn)['process_id'][0]

    if role == 'PO':
        emp_type = "Mgr_OPO"
    elif 'MGR' in role:
        emp_type = 'TL_OPO'
    else:
        emp_type = 'AgentOPO'

    notif = pd.read_sql(f"SELECT KPI_NAME, {emp_type} FROM PMS_NotificationFlag WHERE id = '{notif_id}'", conn)
    kpi_name = notif['kpi_name'][0]
    ap_for_opo = notif[emp_type.lower()][0]

    kpi_id = pd.read_sql(f"SELECT id FROM PMS_MatricesMaster WHERE KPI_Name = '{kpi_name[1:-1]}'", conn)

    if 'why_happen' in request.FILES:
        why_happen = request.FILES['why_happen']
        wh_file_url = default_storage.save('why_happen.xlsx', why_happen)
    else:
        wh_file_url = "none"

    if 'how_to_solve' in request.FILES:
        how_to_solve = request.FILES['how_to_solve']
        hts_file_url = default_storage.save('how_to_solve.xlsx', how_to_solve)
    else:
        hts_file_url = "none"

    max_date = datetime.strptime(request.POST.dict().get("date0"), "%Y-%m-%d").date()
    for i in range(int(total_goal[0])):
        if datetime.strptime(request.POST.dict().get("date" + str(i)), "%Y-%m-%d").date() > max_date:
            max_date = datetime.strptime(request.POST.dict().get("date" + str(i)), "%Y-%m-%d").date()

    conn.cursor().execute(f"INSERT INTO PMS_Actionplan (Process_ID, Kpi_ID, Opo_ID, ParentActionplan_ID, Create_date, "
                          f"IsValid, ApForOPO, IsActive, Close_Date) VALUES ({proc_id}, '{kpi_id['id'][0]}', '{opo_id}'"
                          f", 0, '{cur_date}', 0, '{ap_for_opo}', 'True', '{max_date}')")
    conn.commit()

    p_id = pd.read_sql("SELECT Max(Actionplanid) AS 'PID' FROM PMS_Actionplan", conn)

    for i in range(int(total_goal[0])):
        date = request.POST.dict().get("date"+str(i))
        goal = request.POST.dict().get("goal"+str(i))
        conn.cursor().execute(f"INSERT INTO PMS_Actionplan_when (Parent_action_ID, Stage_Start_Date, Goal_Value) VALUES ('{p_id['pid'][0]}', '{date}', '{goal}')")

    conn.cursor().execute(f"INSERT INTO PMS_Actionplan_why (Parent_action_ID, Attachfilename_ID, Comment) VALUES ('{p_id['pid'][0]}', '{wh_file_url}', '{wh_cmnt}')")
    conn.cursor().execute(f"INSERT INTO PMS_Actionplan_how (Parent_action_ID, Attachfilename_ID, Comment) VALUES ('{p_id['pid'][0]}', '{hts_file_url}', '{hts_cmnt}')")
    conn.cursor().execute(f"INSERT INTO PMS_Actionplan_what (Parent_action_ID, Departmentname, Assignee_Opo_ID, Comment) VALUES ('{p_id['pid'][0]}', '{dept[0]}'"
                          f", '{user[0]}', '{what_to_do}')")
    conn.commit()
    request.msg = "Action Plan has been created"

    return action_plan_view(request)


def kpi_target_ajax(request):
    try:
        conn = connection()
        kpi = request.POST.dict().get("kpi")
        opo_id = request.session['username']
        loc = request.session['loc']
        proc = request.session['proc']
        role = request.session['role']

        if kpi is not None:
            kpi_target = get_kpi_target(conn, kpi, opo_id, role, proc, loc)
            kpi_target = kpi_target.hide_index().render().replace('nan', 'No info')
        else:
            kpi_target = ""
    except Exception as e:
        print(e)
        kpi_target = "No Data Available"

    return HttpResponse(kpi_target)


def action_plan_view(request):
    conn = connection()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    multi_proc = request.session['multi_proc']

    try:
        if role != 'PO':
            action_plan_data, goal_value = get_actionplan_data(conn, opo_id, role, proc)
            form = {'action_plan_data': action_plan_data, 'goal_value': goal_value}
        else:
            form = {}

        team_action_plan, tgoal_value = get_team_ap(conn, opo_id, role, proc)

        form.update({'proc': proc, 'role_desc': role_desc, 'name': name,  'role': role, 'team_action_plan':
            team_action_plan, 'tgoal_value': tgoal_value, 'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc})

        if role != 'AGT' and role != 'TR':
            notifs = get_notifs(conn, opo_id, role)
            form.update({'notifs': notifs})
            if role == 'PO':
                not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                                 "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                                 f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
                form.update({'nac': not_approved_count})
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        msg = "No Active Action Plan for you"
        form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'msg': msg, 'hrmis_proc': hrmis_proc,
                'multi_proc': multi_proc}

    return render(request, 'action_plan_view.html', form)


def why_file_download(request, why_file):
    filename = BASE_DIR + f"/media/{str(why_file)}"
    if os.path.exists(filename):
        with open(filename, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
    raise Http404


def how_file_download(request, how_file):
    filename = BASE_DIR + f"/media/{str(how_file)}"
    if os.path.exists(filename):
        with open(filename, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
    raise Http404


def notification(request):
    conn = connection()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    multi_proc = request.session['multi_proc']

    notifs = get_notifs(conn, opo_id, role)

    form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'notifs': notifs, 'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc}
    return render(request, 'notification.html', form)


def create_plan(request, notif_id):
    request.notif_id = notif_id.replace("%20", " ")
    return action_plan(request)


def assigned_ajax(request):
    conn = connection()
    apid = request.POST.dict().get('apid')
    # opo_id = request.session['username']
    # kpi = kpiproc.split(" - ")[0].strip()
    # proc = kpiproc.split(" - ")[1].strip()
    goal_df = pd.read_sql(f"SELECT Stage_Start_Date AS 'Goal Date', Goal_Value AS 'Goal Value' FROM "
                          f"[PMS_Actionplan_When] WHERE Parent_action_ID = {apid}", conn)
    goal_df = goal_df.to_html(index=False, classes="table table-hover table-dark", border=0)
    return HttpResponse(goal_df)


def kpi_approve_ajax(request):
    conn = connection()
    kpi_id = request.POST.dict().get('kpi_id')
    conn.cursor().execute(f"UPDATE [PMS_Target_Process_KPI] SET is_approved = 1 WHERE id = {kpi_id}")
    conn.commit()
    return HttpResponse(f"KPI Approved of id {kpi_id}")


def team_info(request):
    conn = connection()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']
    _, role, _, role_desc, name, loc = get_access(conn, opo_id)
    proc = request.session['proc']

    if role != 'CH':
        agt_data, tl_data = get_team_data(conn, opo_id, role)
        agt_data.fillna(0, inplace=True)
        agt_data['agtjoindays'] = agt_data['agtjoindays'].astype('int')
        tl_summary = tl_data.rename(columns={'thirty': 'Vintage <= 30', 'sixty': 'Vintage 31 to 60', 'ninety':
            'Vintage 61 to 90', 'greater_ninety': 'Vintage 91 and above'})

        if role in ['PO', 'CH', 'SMGR']:
            cols_tl = tl_summary.columns
            new_cols_tl = [i.replace('tl', 'mgr').replace('agt', 'tl') for i in cols_tl]
            tl_summary.columns = new_cols_tl

        tl_summary = tl_summary.to_html(index=False, border=0, classes="table table-hover table-dark datashow")
        # agt_data = agt_data.to_html(index=False, border=0, classes="table table-hover table-dark datashow")
        notifs = get_notifs(conn, opo_id, role)
        form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'notifs': notifs, 'agt_data': agt_data,
                'tl_data': tl_data, 'tl_summary': tl_summary, 'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc}
    else:
        total_count, emp_count = get_team_data_ch(conn, loc)
        total_count = total_count.to_html(index=False, border=0, classes="table table-hover table-dark datashow")

        form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'tl_summary': total_count,
                'emp_count': emp_count}

    return render(request, 'team_info.html', form)


def quick_report2(request):
    conn = connection()
    fdate = str(request.POST.dict().get('fdate')).replace("-", "")
    tdate = str(request.POST.dict().get('tdate')).replace("-", "")
    cols = request.POST.getlist('cols[]')
    qrtype = request.POST.dict().get('qrtype')
    proc_id = request.session['proc_id']
    opo_id = request.session['username']
    role = request.session['role']
    loc = request.session['loc']

    if 'MGR' in role:
        role = 'manager'
    print(proc_id)
    if 'GGN' in loc:
        loc = '_GGN'
    else:
        loc = ''

    if qrtype == '1':
        query = f"SP_Get_PMS_views{loc} {proc_id},'APR','agent','overall','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '2':
        query = f"SP_Get_PMS_views{loc} {proc_id},'APR','agent','avg','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '3':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','opoDisposition','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '4':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '5':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','Dispowisesum','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '6':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','datewise','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '7':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','TL','DateTL','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '8':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','TL','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '9':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','manager','DateMGR','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '10':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','manager','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '11':
        query = f"SP_Get_PMS_views{loc} {proc_id},'Dump','agent','{opo_id}', ' ','{fdate}','{tdate}'"
    elif qrtype == '12':
        query = f"SP_Get_PMS_views{loc} {proc_id},'SLA','{role}','{opo_id}', ' ','{fdate}','{tdate}'"
    elif qrtype == '13':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','Dispowiseavg','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '14':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','summary','DialerNC'"
    elif qrtype == '15':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','summary','CallDump'"
    elif qrtype == '16':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','Raw','DialerNC'"
    elif qrtype == '17':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','Raw','CallDump'"
    else:
        query = f"SP_Get_Waterfall_Report{loc} {proc_id},'{fdate}'"

    print(query)
    report_data = pd.read_sql(query, conn)

    if len(cols) != 0:
        cols = [i.lower() for i in cols]
        report_data = report_data[cols]

    report_data.fillna(0, inplace=True)
    if 'date' in report_data.columns.to_list():
        report_data['date'] = pd.to_datetime(report_data['date'])

    for col in report_data.columns.to_list():
        if col in time_cols:
            report_data[col] = pd.to_datetime(report_data[col], unit='s').dt.strftime("%H:%M:%S")
        elif col in int_cols:
            report_data[col] = report_data[col].astype('int')

        if 'disp' in col:
            report_data[col] = report_data[col].replace(0, 'None')

    # if qrtype in ['16', '17', '18']:
    #     formatted_date = datetime.now().strftime("%Y-%m-%d")
    #     filename = BASE_DIR + f"/media/report{qrtype}-{str(formatted_date)}.xls"
    #     report_data.to_excel(filename, index=False)
    #     if os.path.exists(filename):
    #         with open(filename, 'rb') as fh:
    #             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
    #             return response
    #     raise Http404


    report_data = report_data.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    return HttpResponse(report_data)


def attr_ajax(request):
    conn = connection()
    opo_id = request.session['username']
    from_to_date = request.session['from_to_date']
    role = request.session['role']

    attr_data = get_attr_data(conn, opo_id, role, from_to_date, 'details')
    attr_data = attr_data.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    return HttpResponse(attr_data)


def kpi_ref(request):
    conn = connection()
    opo_id = request.session['username']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    proc_id = request.session['proc_id']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']

    kpi = pd.read_sql("SELECT ID, KPI_Name FROM PMS_MatricesMaster WHERE KPI_Type = 'Agent' OR KPI_Type = 'Both' ORDER BY ID ASC", conn)
    proc_df = pd.read_sql("SELECT Process_ID, ProcessName FROM PMS_ProcessMaster ORDER BY Process_ID ASC", conn)

    kpi_list = [str(int(i)) + ". " + str(j) for i, j in zip(kpi["id"].to_list(), kpi["kpi_name"].to_list())]
    proc_list = [str(int(i)) + ". " + str(j) for i, j in
                 zip(proc_df["process_id"].to_list(), proc_df["processname"].to_list())]
    today = datetime.now().strftime("%Y-%m-%d")
    kpi_ref_table = pd.read_sql("SELECT b.ProcessName, c.KPI_Name, a.* FROM [PMS_KPI_REF] a LEFT JOIN "
                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID LEFT JOIN PMS_MatricesMaster c ON "
                             f"a.kpi_id = c.ID WHERE b.ProcessName = '{proc}'", conn)

    # kpi_ref_table = kpi_ref_table.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    form = {'kpi_list': kpi_list, 'proc_list': proc_list, 'role_desc': role_desc, 'name': name, 'role': role,
            'today': today, 'kpi_ref_table': kpi_ref_table, 'proc': proc, 'proc_id': str(proc_id)+'. '+proc,
            'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc}

    if role != 'AGT' and role != 'TR':
        notifs = get_notifs(conn, opo_id, role)
        form.update({'notifs': notifs})
        if role == 'PO':
            not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                             f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
            form.update({'nac': not_approved_count})

    return render(request, 'kpi_ref.html', form)


def kpi_ref_add(request):
    conn = connection()
    loc = request.POST.dict().get("loc")
    proc = request.POST.dict().get("process")
    kpi = request.POST.dict().get("kpi")
    tenurity = request.POST.dict().get("tenurity")
    target = request.POST.dict().get("target")
    tolerance_val = request.POST.dict().get("tolerance_val")
    opo_id = request.session['username']
    created_date = datetime.now().strftime('%Y-%m-%d')

    if proc is not None:
        proc_id = proc.split(".")[0]
    else:
        proc_id = ""

    if kpi is not None:
        kpi_id = kpi.split(".")[0]
    else:
        kpi_id = ""

    conn.cursor().execute("INSERT INTO PMS_KPI_REF (location, process_id, kpi_id, tenurity, target, "
                          f"tolerance, added_by, created_date) values ('{loc}', {proc_id}, {kpi_id}, "
                          f"'{tenurity}', {target}, {tolerance_val}, '{opo_id}', '{created_date}')")
    conn.commit()

    return HttpResponse("Successfully Added")


def kpiref_update_ajax(request):
    conn = connection()
    loc = request.POST.dict().get("loc")
    proc = request.POST.dict().get("process")
    kpi = request.POST.dict().get("kpi")
    tenurity = request.POST.dict().get("tenurity")
    target = request.POST.dict().get("target")
    tolerance_val = request.POST.dict().get("tolerance_val")
    kpi_ref_id = request.POST.dict().get('kpi_ref_id')
    opo_id = request.session['username']
    updated_date = datetime.now().strftime('%Y-%m-%d')

    if proc is not None:
        proc_id = proc.split(".")[0]
    else:
        proc_id = ""

    if kpi is not None:
        kpi_id = kpi.split(".")[0]
    else:
        kpi_id = ""

    conn.cursor().execute(f"UPDATE PMS_KPI_REF SET location='{loc}', process_id={proc_id}, kpi_id={kpi_id}, "
                          f"tenurity='{tenurity}', target={target}, tolerance={tolerance_val}, added_by='{opo_id}', "
                          f"created_date='{updated_date}' WHERE id={kpi_ref_id}")
    conn.commit()

    return HttpResponse("Updated")


def ajax_ap_create(request):
    conn = connection()
    opoid = request.POST.dict().get('opoid')
    role = request.session['role']

    if role == 'PO':
        emp = 'ProcessID'
    elif role == 'TL':
        emp = 'AgentOPO'
    else:
        emp = 'TL_OPO'
    print(f"SELECT top 1 id FROM [PMS_NotificationFlag] WHERE {emp} = '{opoid}' ORDER BY id DESC")
    notif_id = pd.read_sql(f"SELECT top 1 id FROM [PMS_NotificationFlag] WHERE {emp} = '{opoid}' ORDER BY id DESC", conn)['id'][0]

    return HttpResponse(notif_id)


def ajax_ap_view(request, opoid):
    conn = connection()
    action_plan_data, goal_value = get_actionplan_data(conn, opoid, "", "")
    # print(action_plan_data.columns, action_plan_data['days_remaining'])
    form = {'action_plan_data': action_plan_data, 'goal_value': goal_value, 'opoid': opoid}

    return render(request, 'view_ap.html', form)


def agent_register(request):
    conn = connection()
    conn1 = connection_hrmis()
    try:
        opo_id = request.session['username']
        cur_loc = request.session['cur_loc']
        if 'GURGAON' in cur_loc:
            loc = "_GGN"
        else:
            loc = ""

        agent_info = pd.read_sql(f"SELECT TOP 1 a.EmpCode AS 'opo id', a.FirstName+' '+a.LastName AS 'Name', "
                                 f"a.CurrentLocation, a.SubDept AS 'Process Name', b.FirstName+' '+b.LastName "
                                 f"AS 'Team Leader', c.FirstName+' '+c.LastName AS 'Manager' FROM "
                                 f"[HRMIS].[dbo].[EmpMaster] a JOIN [HRMIS].[dbo].[EmpMaster] b ON a.EmpCodeLM = "
                                 f"b.EmpCode JOIN [HRMIS].[dbo].[EmpMaster] c ON b.EmpCodeLM = c.EmpCode WHERE "
                                 f"a.EmpCode =  '{opo_id}'", conn1)
        proc = pd.read_sql(f"SELECT TOP 1 PROCESS_ID FROM PMS_AgentRelatedInfo{loc} WHERE Agent_ID = '{opo_id}' ORDER BY DATE desc", conn)
        request.session['proc_id'] = int(proc['process_id'][0])
        agent_info_t = agent_info.T.reset_index()
        agent_info_t['index'] = agent_info_t['index'].str.upper()
        agent_info_t = agent_info_t.to_html(index=False, header=False, classes="table table-hover table-dark", border=0)

        form = {'agent_info_t': agent_info_t}
        return render(request, 'agent_register.html', form)
    except:
        request.msg = "No data found for the USER, Contact Supervisor"
        return login(request)


def create_agent_user(request, ans):
    conn = connection()
    opo_id = request.session['username']
    cur_loc = request.session['cur_loc']
    proc_id = request.session['proc_id']

    if 'GURGAON' in cur_loc:
        loc = 'GGN'
    else:
        loc = cur_loc

    assigned_kpis = pd.read_sql(f"SELECT AssiginedKPI_IDs FROM PMS_RoleMaster WHERE RoleCode='AGT' AND Location = "
                                f"'{cur_loc}' AND ProcessId={proc_id}", conn)

    if ans == 'yes':
        print(proc_id)
        proc_name = pd.read_sql(f"SELECT ProcessName FROM PMS_ProcessMaster WHERE Process_ID = {proc_id}",
                                conn)['processname'][0]
        print(proc_name)
        print(loc)

        if assigned_kpis.shape[0] != 0:
            conn.cursor().execute(f"INSERT INTO PMS_OpoKpiMapping (LocName, ProcessName, OPO_ID, EmpName, KPI_IDs, RoleID) "
                                  f"Values ('{loc}', '{proc_name}', '{opo_id}', 'agent', '{assigned_kpis['assiginedkpi_ids'][0]}', 2)")
            conn.commit()
            return index2(request)
        else:
            request.msg = "No KPI mapped to your process, Please Contact your Supervisor"
    else:
        request.msg = "Contact Supervisor"

    return login(request)


def pms_agent_api(request, opo_id, loc):
    conn = connection()
    to_date = datetime.now().strftime('%Y%m%d')
    from_date_time = datetime.now() - timedelta(days=8)
    from_date = from_date_time.strftime('%Y%m%d')

    if 'GURGAON' in loc:
        loc = 'GGN'
    else:
        loc = ""

    agent_data = pd.read_sql_query(f"SELECT CONVERT(varchar, Convert(Date, Date), 105) AS 'Date', [Avg Handle Time], "
                                   f"[Answered Calls], [Login Time(S)], [Talk Time(S)] FROM "
                                   f"PMS_AgentRelatedInfo{loc} WHERE CONVERT(varchar, CONVERT(Date, Date), 112) BETWEEN"
                                   f" '{from_date}' AND '{to_date}' AND AGENT_ID LIKE '{opo_id}%'", conn)
    agent_data.fillna(0, inplace=True)
    agent_data[agent_data.columns[1:]] = agent_data[agent_data.columns[1:]].astype(int)

    return HttpResponse(agent_data.to_json())


def agent_info_api(request, opo_id):
    conn1 = connection_hrmis()

    agent_info = pd.read_sql(f"SELECT TOP 1 EmpCode,(FirstName + ' '+LastName) as FullName, DOB, Gender, BloodGroup, "
                             f"Emailid, CurrentMobile, DOJ, [Status], currentlocation, SubDept, EmpCodeLM FROM "
                             f"[hrmis].[dbo].EmpMaster WHERE EMPCode='{opo_id}'", conn1)
    # parsed = json.loads(agent_info.to_json(orient='split'))
    # json_dump = json.dumps(parsed)

    return HttpResponse(agent_info.to_json(orient='records'))


def logout(request):
    conn = connection()
    opo_id = request.session['username']
    kpi, role, _, role_desc, name, loc = get_access(conn, opo_id)
    proc = request.session['proc']
    request.session.flush()
    footprint(request, conn, opo_id, role, name, proc, loc, "logout")
    return login(request)


def emi_calc(request):
    return render(request, 'emi_calc.html')


def get_emi_result(request):
    amount = int(request.POST.dict().get('amount'))
    rate = float(request.POST.dict().get('rate'))
    tenure = int(request.POST.dict().get('tenure'))
    rate = (rate / 100)
    start_amount = amount
    end_amount = 0
    diff_amount = start_amount - end_amount
    df = pd.DataFrame(columns=['Outstanding', 'Interest', "Principle", 'Installment'])
    payment_frequency = int(12)
    nr_months = tenure  # = nr_years * payment_frequency
    per_np = np.arange(nr_months) + 1  # +1 because index starts with 1 here
    pay_b = rate / payment_frequency * end_amount
    ipmt_np = np.ipmt(rate / payment_frequency, per_np, nr_months, diff_amount) - pay_b
    ppmt_np = np.ppmt(rate / payment_frequency, per_np, nr_months, diff_amount)
    count = 0
    for payment in per_np:
        idx = payment - 1
        principal = math.fabs(ppmt_np[idx])
        start_amount = start_amount - principal
        interest = math.fabs(ipmt_np[idx])
        instalment = principal + interest
        df.loc[count] = [start_amount, interest, principal, instalment]
        count = count + 1
        print(payment, "\t", principal, "\t", interest, "\t\t", instalment, "\t\t", start_amount)
    df['Outstanding'] = np.where(df['Outstanding'] < 0, 0, df['Outstanding'])
    df = df.round(2)
    df['Month'] = df.index+1
    return HttpResponse(df[['Month', 'Outstanding', 'Interest', "Principle", 'Installment']].to_html(index=False, classes="table table-hover table-dark", border=0))


def analytics(request):
    conn = connection()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    kpi, role, _, role_desc, name, _ = get_access(conn, opo_id)
    proc = request.session['proc']
    loc = request.session['loc']
    multi_proc = request.session['multi_proc']

    kpi_detail = pd.read_sql("SELECT ID, KPI_Name, KPI_Unit FROM PMS_MatricesMaster WHERE KPI_Type = 'Agent' "
                             "OR KPI_Type = 'BOTH' ORDER BY ID ASC", conn)
    kpi_list = [str(int(i)) + ". " + str(j) for i, j in
                zip(kpi_detail["id"].to_list(), kpi_detail["kpi_name"].to_list())]

    if role == 'PO':
        emp_list = multi_proc
    else:
        emp_list = request.session['emp_list']

    try:
        msg = request.msg
    except:
        msg = ''

    form = {'opo_id': opo_id, 'role_desc': role_desc, 'emp_list': emp_list,
            'name': name, 'role': role, 'msg': msg, 'proc': proc, 'hrmis_proc': hrmis_proc,
            'multi_proc': multi_proc, 'kpi_list': kpi_list}

    if role != 'AGT' and role != 'TR':
        notifs = get_notifs(conn, opo_id, role)
        form.update({'notifs': notifs})
        if role == 'PO':
            not_approved_count = pd.read_sql("SELECT COUNT(*) AS 'count' FROM [PMS_Target_Process_KPI] a LEFT JOIN "
                                             "PMS_ProcessMaster b ON a.process_id = b.Process_ID WHERE b.ProcessName ="
                                             f" '{proc}' AND a.is_approved = 0", conn)['count'][0]
            form.update({'nac': not_approved_count})

    return render(request, 'analytics.html', form)


def analytics_ajax(request):
    conn = connection()
    opo_id = request.session['username']
    loc = request.session['loc']
    emp_list = request.session['emp_list']
    proc_id = request.session['proc_id']
    loc_id = request.session['loc_id']
    _, role, _, role_desc, name, _ = get_access(conn, opo_id)
    kpi = request.POST.dict().get('kpi')
    emp = request.POST.dict().get('emp')

    if 'GGN' in loc:
        loc = '_GGN'
    else:
        loc = ''

    to_date = datetime.now().strftime('%Y%m%d')
    from_date_time = datetime.now() - relativedelta.relativedelta(months=3)
    from_date = from_date_time.strftime('%Y%m%d')

    analytics_data, df = get_analytics_data(conn, from_date, to_date, kpi, opo_id, role, loc, emp, emp_list, proc_id, loc_id)
    # analytics_table = analytics_data.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    # print(analytics_data, df)

    return JsonResponse({"predicted": analytics_data.to_dict(orient="list"), "actual": df.to_dict(orient="list")},
                        safe=False)


def create_session(request, from_date, to_date, emp_id, role, agent_id, name, role_desc, proc, from_to_date,
                   proc_type, proc_id, loc, hrmis_proc, multi_proc, emp_list, loc_id):
    request.session['from_date'] = from_date
    request.session['to_date'] = to_date
    request.session['emp_id'] = emp_id
    request.session['role'] = role
    request.session['agent_id'] = agent_id
    request.session['name'] = name
    request.session['role_desc'] = role_desc
    request.session['proc'] = proc
    request.session['from_to_date'] = from_to_date
    request.session['proc_type'] = proc_type
    request.session['proc_id'] = proc_id
    request.session['loc'] = loc
    request.session['hrmis_proc'] = hrmis_proc
    request.session['multi_proc'] = multi_proc
    request.session['emp_list'] = emp_list
    request.session['loc_id'] = loc_id


def recruitment_data_api(request):
    participant_name = request.GET.dict().get('pname')
    recruiter_name = request.GET.dict().get('rname')
    mobile_number = request.GET.dict().get('mno')
    osversion = request.GET.dict().get('osversion')
    phonemodel = request.GET.dict().get('phonemodel')
    network = request.GET.dict().get('network')
    astrikresult = request.GET.dict().get('astrikresult')
    genesysresult = request.GET.dict().get('genesysresult')
    infopageresult = request.GET.dict().get('infopageresult')
    dn = request.GET.dict().get('dn')
    did = request.GET.dict().get('did')
    finalresult = request.GET.dict().get('finalresult')
    empuid = request.GET.dict().get('empuid')
    tdate = datetime.now().strftime('%Y-%m-%d')
    ttime = datetime.now().strftime('%H:%M:%S')

    conn = connection()
    if participant_name is not None and recruiter_name is not None and mobile_number is not None:
        conn.cursor().execute(f"INSERT INTO Recruitment_Data (participantname, recruitername, mobilenumber, osversion, "
                              f"phonemodel, network, testdate, testtime, astrikresult, genesysresult, infopageresult, dn, "
                              f"did, finalresult, empuid) VALUES ('{participant_name}', '{recruiter_name}', '{mobile_number}', {osversion}, "
                              f"'{phonemodel}', '{network}', '{tdate}', '{ttime}', {astrikresult}, {genesysresult}, "
                              f"{infopageresult}, '{dn}', '{did}', '{finalresult}', '{empuid}')")
        conn.commit()
        conn.close()
        msg = 'Data has been saved'
    else:
        msg = "Participant, recruiter name and mobile number is compulsory, Please enter it"

    return HttpResponse(msg)


def dnInfoApi(request, mobile):
    conn = connection()
    dnInfo = pd.read_sql(f"SELECT * FROM DnHrInfo WHERE mobile = '{mobile}'", conn)
    del dnInfo['id']

    return HttpResponse(dnInfo.to_json(orient='records'))


def AttRosterApi(request):
    opoid = request.GET.dict().get('opoid')
    try:
        month = int(request.GET.dict().get('month'))
    except:
        month = None

    if opoid is not None and month is not None:
        conn =connectionHRMISReport()
        today = datetime.now()
        if month == 1:
            lastmonth = today - relativedelta.relativedelta(months=1)
            month_str = lastmonth.strftime("%m")
        else:
            month_str = today.strftime("%m")

        year = today.strftime("%Y")
        ardata = pd.read_sql(f"[GetAttendanceData_HRMISReport_MobileApp] '{opoid}','{month_str}','{year}'", conn)
        ardata['atate'] = pd.to_datetime(ardata['atate'], unit='s').dt.strftime("%Y-%m-%d")

        return HttpResponse(ardata.to_json(orient='records'))
    else:
        return HttpResponse("OPO ID or Month is empty")


def LeaveTrackerApi(request):
    opoid = request.GET.dict().get('opoid')
    conn = connection()
    Ltdata = pd.read_sql(f"select * from [192.168.0.31].[HRMIS].dbo.LeaveTracker  where EMPCODE='{opoid}'", conn)

    return HttpResponse(Ltdata.to_json(orient="records"))


def DevDetailsApi(request):
    dstype = request.GET.dict().get('devtype')
    dtype = request.GET.dict().get('type')
    opoid = request.GET.dict().get('opoid')
    date = request.GET.dict().get('date')
    mgropo = request.GET.dict().get('mgropo')
    subtype = request.GET.dict().get('subtype')
    conn = connection()
    conn.cursor().execute(f"[USP_InsertDeviationDetailsForALL] '{dtype}','{dstype}','{opoid}','{date}','{mgropo}','{subtype}'")
    conn.commit()
    conn.close()

    return HttpResponse("Data has been saved")


def fetchDeviationApi(request):
    devtype = request.GET.dict().get('devtype')

    conn = connectionHRMISReport()
    bio_data = pd.read_sql(f"SP_FetchDeviationMaster 'bio','{devtype}'", conn)
    roster_data = pd.read_sql(f"SP_FetchDeviationMaster 'roster','{devtype}'", conn)
    talk = pd.read_sql(f"SP_FetchDeviationMaster 'talk','{devtype}'", conn)
    toss = pd.read_sql(f"SP_FetchDeviationMaster 'toss','{devtype}'", conn)
    # print(bio_data, roster_data)
    form = {'bio': bio_data.to_json(orient="records", force_ascii=False),
            'roster': roster_data.to_json(orient="records", force_ascii=False),
            'talk': talk.to_json(orient="records", force_ascii=False),
            'toss': toss.to_json(orient="records", force_ascii=False)}

    return HttpResponse(str(form))


def DevDataApi(request):
    opoid = request.GET.dict().get('opoid')

    if opoid is not None:
        today = datetime.now()
        month_str = today.strftime("%m")
        year = today.strftime("%Y")
        conn = connectionHRMISReport()
        devdata = pd.read_sql(f"select DeviationdetailsID, Deviation, DeviationDate, DeviationType, ChangeType, IsManagerApproved, IsHRApproved, IsCHApproved, "
                    f"IsPOApproved, HRReason from deviationdetails where Empcode='{opoid}' and month(recdate)={month_str} and "
                    f"year(recdate)={year} order by DeviationdetailsID desc", conn)
        devdata[['ismanagerapproved', 'ishrapproved', 'ischapproved', 'ispoapproved']] = devdata[['ismanagerapproved', 'ishrapproved', 'ischapproved', 'ispoapproved']].astype('str')
        replace_val = {'None': 'No', '0': 'No', '1': 'yes'}
        devdata[['ismanagerapproved', 'ishrapproved', 'ischapproved', 'ispoapproved']] = devdata[['ismanagerapproved', 'ishrapproved', 'ischapproved', 'ispoapproved']].replace(replace_val)
        devdata.fillna('NA', inplace=True)

        return HttpResponse(devdata.to_json(orient='records'))
    else:
        return HttpResponse("OPO ID or Month is empty")


def DevDeleteApi(request):
    devid = request.GET.dict().get('devid')
    if devid is not None:
        conn = connectionHRMISReport()
        conn.cursor().execute(f"DELETE FROM DeviationDetails WHERE DeviationdetailsID = {devid}")
        conn.commit()
        conn.close()
        msg = f"Deviation deleted with id {devid}"
    else:
        msg = "Deviation ID is None"

    return HttpResponse(msg)


def salaryslipApi(request):
    opoid = request.GET.dict().get('opoid')
    mmyy = request.GET.dict().get('mmyy')
    receiver_email = request.GET.dict().get('mail')

    smtp_server = "mail.onepointone.in"
    port = 587  # For starttls
    sender_email = "no-reply@1point1.in"
    password = "Opo@1234"
    body = f"Greetings from the team, \n please find the attached salary slip for the following month and year {mmyy}\n"
    # message = "testing.... sending mail via python"
    filename = BASE_DIR+f'/media/salary/salary_slip_{opoid}_{mmyy.replace(" ", "")}.pdf'
    # Create a secure SSL context
    context = ssl.create_default_context()
    print(filename)
    path_wkthmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_url(f'http://192.168.0.30/ess/ViewSalarySlipNewMobile.aspx?pubUserName={opoid}&MonthYear={mmyy}',
                    filename, configuration=config)

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename.split('/')[-1]}",
    )

    # Add attachment to message and convert message to string
    message = MIMEMultipart()
    message['Subject'] = 'Auto Generated Mail by One Point One for salary slip'
    message.attach(MIMEText(body, "plain"))
    message.attach(part)
    text = message.as_string()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        # server.ehlo() # Can be omitted
        server.starttls(context=context)  # Secure the connection
        # server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        msg = "mail sent successfully"
        os.remove(filename)
        # TODO: Send email here
    except Exception as e:
        msg = "Server Error, mail can't be sent try after sometime"
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

    return HttpResponse(msg)


def SalaryMYApi(request):
    opoid = request.GET.dict().get('opoid')
    conn = connection_hrmis()

    salarymy = pd.read_sql("select distinct salary_Month, RIGHT(salary_Month, 4) AS salary_Year from SalaryTransaction "
                           f"where empcode='{opoid}' and salary_month is not null order by salary_Year desc", conn)

    finalyear = pd.DataFrame(columns=["Year", "Month"])
    count=0
    for i in salarymy['salary_year'].unique():
        dfyr=salarymy[salarymy['salary_year']==i]
        dfyr['salary_month']=dfyr['salary_month'].str.split(" ", expand=True)[0]
        finalyear.loc[count] = [str(i), dfyr['salary_month']]
        count = count+1

    return HttpResponse(finalyear.to_json(orient='records'))


def team_feedback(request):
    success_msg = None

    conn = connection()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']
    _, role, _, role_desc, name, loc = get_access(conn, opo_id)
    proc = request.session['proc']
    

    conn1 = connection_hrmis()
    tlinfo = pd.read_sql(f"SELECT (FirstName+REPLACE(LastName,'-','')+'-'+EmpCode) as empcode_tr FROM [hrmis].[dbo].EmpMaster WHERE EMPCodeLM='{opo_id}' and activeEmp=1 order by FirstName+REPLACE(LastName,'-','') ", conn1)
   

    
    opoid_list = list(tlinfo['empcode_tr'])
    

    selectopo = request.POST.get('selected-opoid')
    selectdate = request.POST.get('selected-date')
    selectfeedback = request.POST.get('Feedbacktext')
    
    

        # agt_data, tl_data = get_team_data(conn, opo_id, role)
        # agt_data.fillna(0, inplace=True)
        # agt_data['agtjoindays'] = agt_data['agtjoindays'].astype('int')
        # tl_summary = tl_data.rename(columns={'thirty': 'Vintage <= 30', 'sixty': 'Vintage 31 to 60', 'ninety':
        #     'Vintage 61 to 90', 'greater_ninety': 'Vintage 91 and above'})

        # if role in ['PO', 'CH', 'SMGR']:
        #     cols_tl = tl_summary.columns
        #     new_cols_tl = [i.replace('tl', 'mgr').replace('agt', 'tl') for i in cols_tl]
        #     tl_summary.columns = new_cols_tl

        # tl_summary = tl_summary.to_html(index=False, border=0, classes="table table-hover table-dark datashow")
        # # agt_data = agt_data.to_html(index=False, border=0, classes="table table-hover table-dark datashow")
        # notifs = get_notifs(conn, opo_id, role)
        # form = {'proc': proc, 'role_desc': role_desc, 'name': name, 'role': role, 'notifs': notifs, 'agt_data': agt_data,
        #         'tl_data': tl_data, 'tl_summary': tl_summary, 'hrmis_proc': hrmis_proc, 'multi_proc': multi_proc, 'opo_data':opoid_list}
    form = {'opo_data':opoid_list,'role': role, 'proc': proc, 'role_desc': role_desc, 'name': name,}

    return render(request,'team_feedback.html',form)

def submit_feedback(request):
    conn = connection()
    opo_id = request.session['username']
    selectopo2 = request.POST.get('selected-opoid')
    selectdate = request.POST.get('selected-date')
    selectfeedback = request.POST.get('Feedbacktext')
    selectfeedback=selectfeedback.replace("'","").replace('"','')
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']
    _, role, _, role_desc, name, loc = get_access(conn, opo_id)
    conn1 = connection_hrmis()
    tlinfo = pd.read_sql(f"SELECT (FirstName+REPLACE(LastName,'-','')+'-'+EmpCode) as empcode_tr FROM [hrmis].[dbo].EmpMaster WHERE EMPCodeLM='{opo_id}' and activeEmp=1 order by FirstName+REPLACE(LastName,'-','') ", conn1) 
    opoid_list = list(tlinfo['empcode_tr'])
    proc = request.session['proc']
    selectopo = selectopo2.split('-')[1]
    oponame = selectopo2.split("-")[0]
    
    sql = "INSERT INTO PMS_Feedback values('"+opo_id+"','"+selectopo+"','"+selectdate+"','','"+selectfeedback+"',GETDATE(),'"+oponame+"','"+loc+"',0,GETDATE())"    
    try:
        conn.cursor().execute(sql)
        conn.commit()
        print("data submitted")
        msg = "Feedback submitted successfully..!!"
        success_flag = True
        return render(request,'team_feedback.html',{'success_msg':msg,'success_flag':success_flag,'role': role, 'proc': proc, 'role_desc': role_desc, 'name': name, 'opo_data':opoid_list})
    except Exception as e:
        print("wrong data")
        print(e)    
        return team_feedback(request)

def quick_report(request):
    conn = connection()
    fdate = str(request.POST.dict().get('fdate')).replace("-", "")
    tdate = str(request.POST.dict().get('tdate')).replace("-", "")
    cols = request.POST.getlist('cols[]')
    qrtype = request.POST.dict().get('qrtype')
    proc_id = request.session['proc_id']
    opo_id = request.session['username']
    role = request.session['role']
    loc = request.session['loc']

    if 'MGR' in role:
        role = 'manager'
    print(proc_id)
    if 'GGN' in loc:
        loc = '_GGN'
    else:
        loc = ''

    if qrtype == '1':
        query = f"SP_Get_PMS_views{loc} {proc_id},'APR','agent','overall','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '2':
        query = f"SP_Get_PMS_views{loc} {proc_id},'APR','agent','avg','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '3':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','opoDisposition','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '4':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '5':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','Dispowisesum','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '6':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','datewise','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '7':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','TL','DateTL','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '8':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','TL','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '9':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','manager','DateMGR','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '10':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','manager','DispoSubdispo','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '11':
        query = f"SP_Get_PMS_views{loc} {proc_id},'Dump','agent','{opo_id}', ' ','{fdate}','{tdate}'"
    elif qrtype == '12':
        query = f"SP_Get_PMS_views{loc} {proc_id},'SLA','{role}','{opo_id}', ' ','{fdate}','{tdate}'"
    elif qrtype == '13':
        query = f"SP_Get_PMS_views{loc} {proc_id},'disposition','agent','Dispowiseavg','{opo_id}','{fdate}','{tdate}'"
    elif qrtype == '14':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','summary','DialerNC'"
    elif qrtype == '15':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','summary','CallDump'"
    elif qrtype == '16':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','Raw','DialerNC'"
    elif qrtype == '17':
        query = f"SP_Dialer_Call_Dump{loc} '{fdate}','{tdate}','{proc_id}','Raw','CallDump'"
    elif qrtype == '19':
        if role == 'TL':
            query = f"select Createdby,OPO_ID,Stdate,Feedback, CONVERT(varchar, Updateddate,105) Updateddate,Empname from PMS_Feedback where Createdby = '{opo_id}' and CONVERT(varchar,Updateddate,112) >= '{fdate}' and CONVERT(varchar, Updateddate,112) <= '{tdate}'"
            print(query)
        else:
            conn1 = connection_hrmis()

            tlinfo = pd.read_sql(f"SELECT EmpCode FROM [hrmis].[dbo].EmpMaster WHERE EMPCodeLM='{opo_id}' and activeEmp=1", conn1)
            print(tlinfo)
            #print(tuple(tlinfo['empcode']))
            tp=tuple(tlinfo['empcode'])
            # tp.add(f'{opo_id}')

            query = f"select Createdby,OPO_ID,Stdate,Feedback, CONVERT(varchar, Updateddate,105) Updateddate,Empname from PMS_Feedback where (Createdby in {tp} or Createdby = '{opo_id}') and CONVERT(varchar,Updateddate,112) >= '{fdate}' and CONVERT(varchar, Updateddate,112) <= '{tdate}'"        
    else:
        query = f"SP_Get_Waterfall_Report{loc} {proc_id},'{fdate}'"

    print(query)
    print(fdate)
    print(tdate)
    report_data = pd.read_sql(query, conn)

    if len(cols) != 0:
        cols = [i.lower() for i in cols]
        report_data = report_data[cols]

    report_data.fillna(0, inplace=True)
    if 'date' in report_data.columns.to_list():
        report_data['date'] = pd.to_datetime(report_data['date'])

    for col in report_data.columns.to_list():
        if col in time_cols:
            report_data[col] = pd.to_datetime(report_data[col], unit='s').dt.strftime("%H:%M:%S")
        elif col in int_cols:
            report_data[col] = report_data[col].astype('int')

        if 'disp' in col:
            report_data[col] = report_data[col].replace(0, 'None')


    report_data = report_data.to_html(index=False, classes="table table-hover table-dark datashow", border=0)

    return HttpResponse(report_data)

def footprintApi(request):
    conn = connection()
    opoid = request.GET.dict().get('opoid')
    ftype = request.GET.dict().get('ftype')
    proc = request.GET.dict().get('proc')
    kpi, role, _, role_desc, name, loc = get_access(conn, opoid)
    footprint(request, conn, opoid, role, name, proc, loc, ftype)
    return HttpResponse("Footprint Recorded")


def view_feedbacks(request):
    conn = connection()
    conn1 = connection_hrmis()
    opo_id = request.session['username']
    hrmis_proc = request.session['hrmis_proc']
    multi_proc = request.session['multi_proc']
    _, role, _, role_desc, name, loc = get_access(conn, opo_id)
    proc = request.session['proc']
    agent_data = pd.read_sql_query(f"SELECT * FROM PMS_Feedback WHERE OPO_ID='{opo_id}' order by Fid desc", conn)
    agent_data['createdby_name'] = ''  # Initialize the createdby_name column
    for index, row in agent_data.iterrows():
        createdby_opoid = row['createdby']
        ticket_createdby = pd.read_sql_query(f"SELECT (firstname+' '+lastname) as EmpNames FROM [hrmis].[dbo].EmpMaster WHERE EmpCode='{createdby_opoid}'", conn1)
        agent_data.at[index, 'createdby_name'] = ticket_createdby['empnames'].iloc[0] if not ticket_createdby.empty else None
    context  = {'feedbacks':agent_data.to_dict(orient='records'), 'role': role, 'proc': proc, 'role_desc': role_desc, 'name': name,}
    print(context)
   
    return render(request,'view_feedbacks.html',context)
   

def user_feedback(request):
    userid = request.POST.get('userid')
    actionid = request.POST.get('request_code')
    fid = int(userid)
    print('fid====>',fid)
    print('accept / reject=====>',actionid)
    conn = connection()
    print(conn)
 
    if(actionid=='1'):
        conn.cursor().execute(f"update PMS_Feedback set is_accept=1, accepted_time=GETDATE() where fid={userid}")
        conn.commit()
        return JsonResponse({'req_code':1,'msg':'Request Accept'},safe=False)
    else:
        conn.cursor().execute(f"update PMS_Feedback set is_accept=2, accepted_time=GETDATE() where fid={userid}")
        conn.commit()
        return JsonResponse({'req_code':2,'msg':'Request Reject'},safe=False)



def getemployeedetails(request):
	
	return render(request,'getempdetails.html')


def getempdata_2022(request):
    opoid = None
    if request.method == "POST":
        opoid = request.POST.get("opoid")
        date = request.POST.get("date")
        conn = connection_hrmis()
        data = pd.read_sql_query(f"SP_Getemployee_Detail '{opoid}','{date}'",conn)
        
    context ={'EmpCode':str(data['empcode'][0]),'FullName':str(data['fullname'][0]),'CurrentDesignation':str(data['currentdesignation'][0]),'Department':str(data['department'][0]),'SubDepartment':str(data['subdept'][0]),'Location':str(data['location'][0]),'Login':str(data['login'][0]),'Logout':str(data['logout'][0])}
    return render(request,'getempdetails.html', context)


# def getempdata_2022(request):
# 	opoid = None
# 	date=None
#     try:
#         if request.method == "POST":
#             opoid = request.POST.get("opoid")
#             date = request.POST.get("date")
#             conn = connection_hrmis()
#             x = pd.read_sql_query(f"SP_Getemployee_Detail '{opoid}','{date}' " ,conn)

#     except Exception as e:

#         return JsonResponse({'req_code':2,'msg':str(e)},safe=False)                                      
# 	# context ={'EmpCode':str(x['empcode'][0]),'FullName':str(x['fullname'][0]),'CurrentDesignation':str(x['currentdesignation'][0]),'Department':str(x['department'][0]),'SubDepartment':str(x['subdept'][0]),
# 	# 'Location':str(x['location'][0]),'Login':str(x['login'][0]),'Logout':str(x['logout'][0])}  
# 	# return (request,'getempdetails.html')



def authenticated_user(request):
    if request.method == "POST":
        active_opo = request.POST.get('active_id')
        who_active_opo = request.POST.get('who_activate')
        who_active_passwd = request.POST.get('passwd')
        
        # domain = request.session['domain']
        domain = request.session.get('domain')
        
        checkdt = userinfoacces(who_active_opo,who_active_passwd,domain)
        
        if checkdt == 1:
            print("----------")
            conn = connection_hrmis()
            cursor = conn.cursor()
            query = f"SP_InsertBio_Mannual {active_opo},{who_active_opo}"
            cursor.execute(query)
            cursor.commit()
            cursor.close()
            conn.close()

            #qry = pd.read_sql_query(f"SP_InsertBio_Mannual '{active_opo}', '{who_active_opo}'",conn)
            data ="1"
            return JsonResponse({'data':1,'msg':'Request Reject'},safe=False)
        else:
            data = '2'
            return JsonResponse({'data':2,'msg':'Request Reject'},safe=False)
    else:
        data="0"
        return JsonResponse({'data':0,'msg':'Request Reject'},safe=False)




def connectionicici():
    try:
        conn = pypyodbc.connect("Driver={SQL Server}; Server=192.168.0.57; Database=ICICI_Card_Collection; "
               "uid=opodba;pwd=opo@1234;")
    except pypyodbc.Error as e:
        print(e)
    return conn



def calculate_probability(mycode):
    conx=connectionicici()
    df=pd.read_sql('select Phonenumber from History_Attempt where mycode='+mycode, conx)
    numbers = df.get('phonenumber', [])
    frequency = defaultdict(int)
    for number in numbers:
        frequency[number] += 1
    total_calls = len(numbers)
    probability_scores = {}
    for number, count in frequency.items():
        probability_scores[number] = (count / total_calls)*100
    conx.close() 
    return probability_scores

@csrf_exempt
def calculateproba(request):
    if request.method == "POST":
        mycode = request.POST.get('mycode')
        prob=calculate_probability(mycode)
        return JsonResponse(prob,safe=False)   
    else:
        data="0"
        return JsonResponse({'data':0,'msg':'Request Reject'},safe=False)

