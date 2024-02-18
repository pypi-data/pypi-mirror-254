from os import listdir, mkdir
from os.path import isfile, join
import zipfile
import json
import pandas as pd
import sqlite3
import requests
import re

nvd_database = 'nvd_history.db'
cnx = sqlite3.connect(nvd_database)

def get_dataFeedCVEs():
    try:
        mkdir('nvd')
    except:
        pass
    r = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
    for filename in re.findall("nvdcve-1.1-[0-9]*\.json\.zip",r.text):
        print(filename)
        url = "https://nvd.nist.gov/feeds/json/cve/1.1/" + filename
        print(url)
        r_file = requests.get(url, stream=True)
        with open("nvd/" + filename, 'wb') as f:
            for chunk in r_file:
                f.write(chunk)

def get_Cvss(dataImpact):
    cvss = 0.0
    if dataImpact.get('baseMetricV3'):
        cvss = dataImpact.get('baseMetricV3').get('cvssV3').get('baseScore')
    elif dataImpact.get('baseMetricV2'):
        cvss = dataImpact.get('baseMetricV2').get('cvssV2').get('baseScore')
    
    return cvss
def get_CWEs(problemtype):
    problemtype.get('problemtype_data')

def get_Description(description):
    for desc in description.get('description_data'):
        if desc.get('lang') == 'en':
            return desc.get('value')
        
def run():
    get_dataFeedCVEs()
    files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
    files.sort()
    for file in files:
        archive = zipfile.ZipFile(join("nvd/", file), 'r')
        jsonfile = archive.open(archive.namelist()[0])
        nvd_data = json.loads(jsonfile.read())
        jsonfile.close()
        cves_all = []
        for num in range(0,len(nvd_data['CVE_Items'])):
            cve = nvd_data['CVE_Items'][num]['cve']['CVE_data_meta']['ID']
            cvss = get_Cvss(dataImpact=nvd_data['CVE_Items'][num]['impact'])
            pb_data = nvd_data['CVE_Items'][num]['publishedDate']
            lm_data = nvd_data['CVE_Items'][num]['lastModifiedDate']
            description = get_Description(description=nvd_data['CVE_Items'][num]['cve']['description'])
            model = {
                "cve": cve,
                "cvss": cvss,
                "publication_date": pb_data,
                "last_modified": lm_data,
                "description": description
            }
            cves_all.append(model)
        pd.DataFrame(cves_all).to_sql(name="NVD", con=cnx, if_exists='append', index=False)