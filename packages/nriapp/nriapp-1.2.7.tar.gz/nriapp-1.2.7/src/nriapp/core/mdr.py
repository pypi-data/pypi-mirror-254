import os 
import requests
import pickle

from loguru import logger
from urllib.parse import urlencode, unquote_plus
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path
import base64, json, re

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from helper import login_snyper as snypr

#dbgPrint = PyLog(__name__, level=logging.INFO)

logger.add(f"./logs/{__name__}.log", backtrace=True, diagnose=True, filter="MSGraphApi")
dbgPrint = logger

class ManagedDetection(object):

    def __init__(self, cookie=None):
        if cookie == None:
            self.load_session()
        else: 
            self._cookie = cookie
            self._session = requests.Session()
            self._session.cookies.update(cookie)
            self._session.headers.update({"org.codehaus.groovy.grails.synchronizer_token" : self._cookie["csrf_token"]})
            self.save_session()

    def save_session(self):
        session_path = os.path.abspath(os.path.dirname(__file__)) + "\..\session"
        session_file = session_path + "\\mdr.pkl"
        if not os.path.exists(session_path):
            os.makedirs(session_path)
        if not os.path.exists(session_file):
            with open(session_file, "wb") as f:
                pickle.dump(self._cookie, f)

    def delete_session(self):
        session_path = os.path.abspath(os.path.dirname(__file__)) + "\..\session"
        session_file = session_path + "\\mdr.pkl"
        for p in Path(session_path).glob("mdr.pkl"):
            os.remove(p)                

    def load_session(self):
        session_path = os.path.abspath(os.path.dirname(__file__)) + "\..\session"
        session_file = session_path + "\\mdr.pkl"
        if os.path.exists(session_file):
            with open(session_file, "rb") as f:
                cookies = pickle.load(f)
            self.__init__(cookies)
        else:
            snipe = snypr.Login()
            cookie = snipe.snyper()
            self.__init__(cookie)

        return self

    
    def list_incidents(self, unit='hours', range=24, max=50, timecasefilter="updated"):
        #timecasefilter: updated, opened, closed
        #units: hours, days, years
        
        headers = {
                "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
                "org.codehaus.groovy.grails.synchronizer_token": self._cookie["csrf_token"]
        }

        incident_management = "https://a1t1tdhq.apac.vzmdr.com/Snypr/configurableDashboards/displaywidgetdata"

        filters = {"-1":[[str(range)]],"timecasefilter":[[timecasefilter]],"-6":[["incidents"]]}

        filters = base64.b64encode(json.dumps(filters, separators=(",",":")).encode("utf-8")).decode("utf-8")

        data = {
        'checkToken': 'true',
        'max': str(max),
        'range': unit,
        'offset': '0',
        'widgetid': '67',
        'filters': filters,
        'escapeLoadingStart': 'true',
        'org.codehaus.groovy.grails.SYNCHRONIZER_TOKEN': self._cookie["csrf_token"],
        }

        response = self.tryrequest(incident_management, headers=headers, data=data)
        try:
            data = json.loads(response.text)[1]['data']['incidentItems']
            incidents = [{
            "incidentId"          :   int(i["incidentId"]), 
            "entity"              :   i["entity"],
            "incidentStatus"      :   i["incidentStatus"], 
            "incidentType"        :   i["incidentType"], 
            "caseEventStartTime"  :   i["caseEventStartTime"], 
            "caseEventEndTime"    :   i["caseEventEndTime"], 
            "lastUpdateTime"      :   i["lastUpdateDate"],  
            "name"                :   i["name"], 
            "reason"              :   i["reason"],
            "priority"            :   i["priority"],
            "reason"              :   i["reason"],
            "violatorId"          :   i["violatorId"]} 
            for i in json.loads(response.text)[1]['data']['incidentItems']]

            for i in incidents:
                info = self.get_incident_details(i['incidentId'])
                dbgPrint.info(i['incidentId'])
                i.update(
                {
                  "createdBy"   : info['createdBy'],
                  "createdOn"   : info['createdOn'],
                  "policyName"  : info['policyName'],
                  "policyId"    : info['policyId'], 
#                  "updatedOn"   : info['updatedOn'],
                  "sourceType"  : info['sourceType'],
                  "description" : info['description']
                })

            return incidents
        
        except json.decoder.JSONDecodeError:
            self.delete_session()
            self.load_session()
            return self.list_incidents(unit, range=range, max=max, timecasefilter=timecasefilter)



    def get_incident_activity_stream(self, incidentId):

        incident_info = "https://a1t1tdhq.apac.vzmdr.com/Snypr/drawable/getDrawableModuleData"

        headers = {
                "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
                "org.codehaus.groovy.grails.synchronizer_token": self._cookie["csrf_token"]
        }

        data = {
        'checkToken': 'true',
        'caseid': str(incidentId),
        'casetype': "",
        'modulename': 'IncidentActivityStream',
        'callablename': 'IncidentActivityStream',
        'preprocessor': '',
        'org.codehaus.groovy.grails.SYNCHRONIZER_TOKEN': self._cookie["csrf_token"]
        }

        response = self.tryrequest(incident_info, headers=headers, data=data)
        try:
            out = json.loads(response.text)
            return out[0]['activityDetails']
        except:
            self.delete_session()
            self.load_session()
            return self.get_incident_activity_stream(incidentId)            

    
    def get_incident_details(self, incidentId):

        incident_details = 'https://a1t1tdhq.apac.vzmdr.com/Snypr/drawable/getDrawableModuleData'
        data = {
            'checkToken': 'true',
            'caseid': str(incidentId),
            'modulename': 'IncidentDetailsView',
            'callablename': 'IncidentDetails',
            'preprocessor': '',
            'org.codehaus.groovy.grails.SYNCHRONIZER_TOKEN': self._cookie["csrf_token"],
        }
        headers = {
                "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
                "org.codehaus.groovy.grails.synchronizer_token": self._cookie["csrf_token"]
        }

        response = self.tryrequest(incident_details, headers=headers, data=data)   
        try:
            data = json.loads(response.text)[0]['details']
        except:
            dbgPrint.error("Error")

        return {
            "createdBy"         : data['createdBy'],
            "createdOn"         : data['createdOn'],
            "description"       : data['description'],
            "policyName"        : data['policyname'],
            "policyId"          : data['policyid'], 
            "updatedOn"         : data['updatedOn'],
            "incidentStatus"    : data['incidentStatus'],
            "sourceType"        : data['violatorDetails']['entity']['rg_type'] if data['violatorDetails'] != None and data['violatorDetails'].get('entity') and data['violatorDetails']['entity'].get('rg_type') else ''
            }


    def get_raw_event(self, incidentId):

        rawevent = ""
        stream = self.get_mdr_comment(incidentId)
        pattern = r'rawevent\s?=\s?(.+?)\n'
        pattern2 = r'(?=.{201,})[{\[]{1}([,:{}\[\]0-9.\-+Eaeflnr-u \n\r\t]|".*?")+[}\]]{1}'     # searches for a minimum of 200 characters
        items = {}
        raw_logs = []
        for i in stream:
            if i["comment"]:
                if re.search(pattern, i["comment"]) != None:
                    content = re.search(pattern, i["comment"]).group(1)
                    try:
                        items = json.loads(content)
                        raw_logs.append(items)
                    except json.decoder.JSONDecodeError:
                        split = content.split('|')
                        if len(split) < 20:
                            continue
                        for item in split:
                            key_value = item.split('=')
                            key = key_value[0]
                            value = key_value[1] if len(key_value) == 2 else ''
                            items[key] = value
                        raw_logs.append(items)
                elif re.search(pattern2, i["comment"]) != None:
                    content = re.search(pattern2, i["comment"]).group(0)
                    try: 
                        items = json.loads(content)
                        raw_logs.append(items)
                    except json.decoder.JSONDecodeError:
                        continue

        return raw_logs

    def get_top_violations(self, hours, day):
        pass

    def get_mdr_comment(self, incidentId):                      #Please fix 17821423234
        stream = self.get_incident_activity_stream(incidentId)
        comment = []
        def sort_key(item):
            return datetime.strptime(item['eventTime'], "%Y-%m-%dT%H:%M:%SZ")
        stream = sorted(stream, key=sort_key)
#        if stream[0]['type'] == 'CUSTOM_CASE':
#            for i in stream:
#                if i['actiontaken'] == 'COMMENTS_ADDED' and ("Dear customer" in i['comment'][0]['Comments'] or i['username'] != "Service Account"):
#                    print(BeautifulSoup(i['comment'][0]['Comments'], features='html.parser').get_text().replace('\n\n\n', '\n'))
#                    break
#        elif stream[0]['type'] == None:
        assignee = ""
        for i in stream:
            if (i['actiontaken']).upper() == 'CLAIM' and (i['lastStatus']).lower() == 'open':
                assignee = i['currentassignee']
            elif i['actiontaken'].upper() == 'ASSIGN TO CLIENT' and i['currentassignee']== 'NRI_DEFAULT':
                for a in i['comment']:
                    if a.get('Comments'):
#                        print(a['Comments'])
                        comment.append({
                            'incidentId': int(i['caseid']),
                            'actionTaken' : i['actiontaken'].upper(),
                            "comment" : a['Comments'],
                            'assignee' : i['currentassignee'],
                            'timestamp' : i['eventTime'],
                            'lastStatus': i['lastStatus'],
                            'status' : i['status'],
                            'username' : i['username'],
                            'workflow' : 'mdr'
                        })                        
            elif (i['actiontaken']).upper() == 'COMMENTS_ADDED' and i['creator'] == assignee and (i['status']).lower() == 'claimed':
                out = BeautifulSoup(i['comment'][0]['Comments'], features='html.parser').get_text().replace('\n\n\n', '\n')
#                print(out)
                comment.append({
                    'incidentId': int(i['caseid']), 
                    'actionTaken' : i['actiontaken'].upper(),
                    "comment" : out,
                    'assignee' : i['currentassignee'],
                    'timestamp' : i['eventTime'],
                    'lastStatus': i['lastStatus'],
                    'status' : i['status'],
                    'username' : i['username'],
                    'workflow' : 'mdr'
                })
        return comment

    def get_nri_comment(self, incidentId):
        stream = self.get_incident_activity_stream(incidentId) 
        comment = []       
        def sort_key(item):
            return datetime.strptime(item['eventTime'], "%Y-%m-%dT%H:%M:%SZ")
        stream = sorted(stream, key=sort_key)   
        assignee = ""
        for i in stream:
            if (i['actiontaken']).upper() == 'CLAIM CASE' and (i['status']).lower() == 'Claimed-Customer'.lower() and i['currentassignee'] == 'NRI_DEFAULT':
                assignee = i['creator']
                for a in i['comment']:
                    if a.get('Comments'):
                        print(a['Comments'])
                        comment.append({
                            'incidentId': int(i['caseid']),
                            'actionTaken' : i['actiontaken'].upper(),
                            "comment" : a['Comments'],
                            'assignee' : i['currentassignee'],
                            'timestamp' : i['eventTime'],
                            'lastStatus': i['lastStatus'],
                            'status' : i['status'],
                            'username' : i['username'],
                            'workflow' : 'client'
                        })
            elif (i['actiontaken']).upper() == 'COMMENTS_ADDED' and i['currentassignee'] == assignee:
                for a in i['comment']:
                    if a.get('Comments'):
                        lines = []
                        out = BeautifulSoup(a['Comments'], features='html.parser').get_text(strip=True, separator='\n')
                        print(out)
                        comment.append({
                            'incidentId': int(i['caseid']),
                            'actionTaken' : i['actiontaken'].upper(),
                            "comment" : out,
                            'assignee' : i['currentassignee'],
                            'timestamp' : i['eventTime'],
                            'lastStatus': i['lastStatus'],
                            'status' : i['status'],
                            'username' : i['username'],
                            'workflow' : 'client'
                        })                    
            elif (i['actiontaken']).upper() == 'CLOSE CASE' and i['creator'] == assignee:
                for a in i['comment']:
                    if a.get('Comments'):
                        print(a['Comments'])                                
                        comment.append({
                            'incidentId': int(i['caseid']),  
                            'actionTaken' : i['actiontaken'].upper(),
                            "comment" : a['Comments'],
                            'assignee' : i['currentassignee'],
                            'timestamp' : i['eventTime'],
                            'lastStatus': i['lastStatus'],
                            'status' : i['status'],
                            'username' : i['username'],
                            'workflow' : 'client'
                        })   
            elif (i['actiontaken']).lower() == 'Return to Verizon'.lower() and i['creator'] == assignee:
                for a in i['comment']:
                    if a.get('Comments'):
                        print(a['Comments'])                                
                        comment.append({
                            'incidentId': int(i['caseid']),  
                            'actionTaken' : i['actiontaken'].upper(),
                            "comment" : a['Comments'],
                            'assignee' : i['currentassignee'],
                            'timestamp' : i['eventTime'],
                            'lastStatus': i['lastStatus'],
                            'status' : i['status'],
                            'username' : i['username'],
                            'workflow' : 'client'
                        })   
        return comment

    def get_nri_mdr_comments(self, incidentId):
        mdr_comment = self.get_mdr_comment(incidentId)
        nri_comment = self.get_nri_comment(incidentId)
        return mdr_comment + nri_comment

    def get_policies_threat(self, objectId):

        other_policies_for_entity = 'https://a1t1tdhq.apac.vzmdr.com/Snypr/violationDetails/getOtherPoliciesForEntity'
        
        if not objectId:
            return []

        data = {
            'checkToken' : 'true',
            'entityId' : base64.b64encode(bytes(objectId, "utf-8")).decode("utf-8"),
            'modelid' : '-1',
            'objecttype' : 'RTActivityAccount',
            'objectid' : objectId,
            'risktypeids' : '0',
            'excludePolicyId' : '0',
#            'policycategoryid' : '-1',
            'loadVerbose' : 'true',
            'tenantid' : '10',
            'org.codehaus.groovy.grails.SYNCHRONIZER_TOKEN' : self._cookie["csrf_token"],
            'actionable_tenant_id' : '10'
        }
        headers = {
                "content-type" : "application/x-www-form-urlencoded; charset=UTF-8",
                "org.codehaus.groovy.grails.synchronizer_token": self._cookie["csrf_token"]
        }

        response = self.tryrequest(other_policies_for_entity, headers=headers, data=data)
        policies = []
        try:
            data = json.loads(response.text)['highRiskPoliciesList']
            if data:
                caseid = ""
                for i in data:
                    alert = {'solrQuery' : unquote_plus(i['solrQuery']),
                            'caseId'            : str(caseid),
                            'policyName'        : i['policyname'],
                            'score'             : i['score'],
                            'triggerStartDate'  : i['triggerStartDate'],
                            'triggerEndDate'    : i['triggerEndDate'],
                            'timelong'          : i['timelong'],
                            'severity'          : i['criticality'],
                            'rsrcGroupName'     : i['resourcegroupname'],
                            'entityName'        : i['entityname'],
                            'riskThreatId'      : i['riskthreatid'],
                            'policyId'          : i['policyid'],
                            'categoryId'        : i['categoryid'],
                            'checkName'         : i['checkname'],
                            'comments'          : i['comments'],
                            'violator'          : i['violator'],
                            'actionTime'        : i['actiontime'],
                            'threatName'        : i['threatname'],
                            'userName'          : i['secusername'],
                            'userGroup'         : i['secusergroup'],
                            'policyDescription' : i['policydescription'],
                            'category'          : i['category'],
                            'source'            : i['source']}
                    policies.append(alert)

        except:
            self.delete_session()
            self.load_session()
            return self.get_policies_threat(objectId)  

        return policies


    def tryrequest(self, arg, **kwargs):
        headers = kwargs.pop('headers', {})  
        params = kwargs.pop('params', {})
        json_data = kwargs.pop('json', {})
        form_data = kwargs.pop('data', {})
        if kwargs:
            dbgPrint.error("Unexpected argument")


        response = self._session.post(arg, headers=headers, data=form_data, json=json_data)
        return response



