import re

LIC= 'DL\nClass D\nOMMISSIONE\nUSA\nDRIVER LICENSE\n, Class: D\nRestr: NONE\nso Endors: NONE\n4d Lic #: 787878787\n3 DOB: 05-30-1978 S 1:Eyes BLU\n.Exairses: 05-30-2015 S& Sap\nSex F\n16 Ht: 61 in\nSAMPLE\n2SUSAN CATHERINE\n860 STATE ST, ROOM 145\nWETHERSFIELD CT 06109\na Issued: 06-30-2009\n\nDL\nClass\nD\nOMMISSIONE\nUSA\nDRIVER\nLICENSE\n,\nClass\n:\nD\nRestr\n:\nNONE\nso\nEndors\n:\nNONE\n4d\nLic\n#\n:\n787878787\n3\nDOB\n:\n05-30-1978\n▼\n1\n:\nEyes\nBLU\n.Exairses:\n05-30-2015\nS&\nSap\nSex\nF\n16\nHt:\n61\nin\nSAMPLE\n2SUSAN\nCATHERINE\n860\nSTATE\nST,\nROOM\n145\nWETHERSFIELD\nCT\n06109\na\nIssued:\n06-30-2009'
clean_lic = str(LIC.encode("ascii", "replace"))

def extractDOB():
    if 'DOB' in clean_lic:
        index = clean_lic.find('DOB') + 3
        print(index)
        dob_buffer = 15
        #dob should only be 10 chars long, give some extra space incase of inaccuracy
        temp = clean_lic[index:index+dob_buffer]
        split_index = temp.find('-')
        return temp[split_index-2:split_index+8]
    else:
        return ''

#print(extractDOB())

def extractPersonalInfo():
    """ Pull set of personal info based on position of the Issued value """
    if 'Issued' in clean_lic:
        index = clean_lic.find('Issued')
        new_lic = clean_lic[2:index]
        new_lic_list = new_lic.split('\\n')
        while len(new_lic_list[len(new_lic_list)-1]) < 5:
            new_lic_list.pop()
        return(new_lic_list[-4:])
    else:
        return ''

#print(extractPersonalInfo())

def extractAddress():
    info_list = extractPersonalInfo()
    if info_list != '':
        return ' '.join(info_list[-2:])
    else:
        return ''

#print(extractAddress())

def extractNames():
    info_list = extractPersonalInfo()
    if info_list != '':
        for _ in range(2):
            info_list.pop()
        names = [info_list[0]] + info_list[1].split(' ')
        return names
    else:
        return ''

#print(extractNames())

def extractinfo():
    names = extractNames()
    if names != '':
        info = {
            'firstname' : names[1],
            'lastname' : names[0],
            'middle_initial' : names[2][:1],
            'address' : extractAddress()
        }
        return info
    else:
        return ''

#print(extractinfo())