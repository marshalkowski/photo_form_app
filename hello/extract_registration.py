import vinlib
import requests
import json

# REG is the data taken from a google vision call
REG = """VALID ONLY AFTER\nRESOLVING ALL\nCOMPLIANCE\nISSUES\nR CONNECTICUT REGISTRATION CERTIFICATE ,VALID ONLY\nECEIVE
D BY\nAFTER PAYMENT\nKEEP THIS PORTION IN YOUR VEHICLE DO NOT MAIL\nINSURANCE SHALL BE MAINTAINED AS REQUIRED BY CT LAW\
nDMV\nPLATE NUMBER\nPLATE CLASS\nEXP. DATE VEHICLE IDENTIFICATION NUMBER YR\n12/28/207 JHMCG66572C00383302 HONDA\nLIGHT 
Wi | GVWR | DECLARED WTİ STAND | SEAT | AXLES\nMAKE\nMODEL\n641ZBB\nPASSENGER\nREGISTERED USAGE\nACCORD L\nVEHICLE TYPE\
nPASSENGER\nCOLOR\nTAN\nTYLE\n4D\nREGULAR\nREG FEE\n$80.00\n2\nHAZ MAT?| TITLE | EMISSIONS DUE |\nPLATE TYPE\nSTANDARD\n
TOWN\n142\nTAX TOWN\nTOLLAND\n10/25/2015\nY 12/07/2016\nCOMMISSIONER OF MOTOR VEHICLES\n\nVALID\nONLY\nAFTER\nRESOLVING\
nALL\nCOMPLIANCE\nISSUES\nR\nCONNECTICUT\nREGISTRATION\nCERTIFICATE\n,VALID\nONLY\nECEIVED\nBY\nAFTER\nPAYMENT\nKEEP\nTH
IS\nPORTION\nIN\nYOUR\nVEHICLE\nDO\nNOT\nMAIL\nINSURANCE\nSHALL\nBE\nMAINTAINED\nAS\nREQUIRED\nBY\nCT\nLAW\nDMV\nPLATE\n
NUMBER\nPLATE\nCLASS\nEXP.\nDATE\nVEHICLE\nIDENTIFICATION\nNUMBER\nYR\n12/28/207\nJHMCG66572C00383302\nHONDA\nLIGHT\nWi\
n|\nGVWR\n|\nDECLARED\nWTİ\nSTAND\n|\nSEAT\n|\nAXLES\nMAKE\nMODEL\n641ZBB\nPASSENGER\nREGISTERED\nUSAGE\nACCORD\nL\nVEHI
CLE\nTYPE\nPASSENGER\nCOLOR\nTAN\nTYLE\n4D\nREGULAR\nREG\nFEE\n$80.00\n2\nHAZ\nMAT\n?\n|\nTITLE\n|\nEMISSIONS\nDUE\n|\nP
LATE\nTYPE\nSTANDARD\nTOWN\n142\nTAX\nTOWN\nTOLLAND\n10/25/2015\nY\n12/07/2016\nCOMMISSIONER\nOF\nMOTOR\nVEHICLES"""


def parsevin():
    """ Returns the most probable vin value """
    reglist = REG.split('\n')
    possible_vins = []

    for a in reglist:
        if(len(a) == 17):
            possible_vins.append(a)
        elif(len(a) == 19):
            possible_vins.append(a[:-2])

    if len(possible_vins) == 1:
        return possible_vins[0]
    elif len(possible_vins) > 1:
        return narrow_vins(possible_vins)
    else:
        return ''


def narrow_vins(vin_list):
    """ Returns the first valid Vin, if none are valid, returns an empty string 
    """
    for i in vin_list:
        if (vinlib.check_vin(i)):
            return i
    return ''


print(parsevin())

myvin = parsevin()

def decodevin():
    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
    post_fields = {'format': 'json', 'data': parsevin()}
    r = requests.post(url, data=post_fields)
    json_obj = r.json()

    vin_info = {}
    vin_info['model'] = (json_obj['Results'][0]['Model'])
    vin_info['make'] = (json_obj['Results'][0]['Make'])
    vin_info['modelyear'] = (json_obj['Results'][0]['ModelYear'])
    return vin_info