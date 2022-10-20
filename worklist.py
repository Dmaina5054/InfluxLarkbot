import re
def splitdata(data):

    r = re.compile('.*G44-FIBER')
    G44list1 = list(filter(r.match, data)) # Read Note below
    pattern = r'G44-FIBER:'
    G44list = [re.sub(r'G44-FIBER:', '', s) for s in G44list1]
    if G44list != []:
        G44 = f"G44 REGION:\n {G44list}\n\n"
    else:
        G44 = ""

    r = re.compile('.*G45-FIBER')
    G45list1 = list(filter(r.match, data)) # Read Note below
    pattern = r'G45-FIBER:'
    G45list = [re.sub(r'G45-FIBER:', '', s) for s in G45list1]
    if G45list != []:
        G45 = f"G45 REGION:\n {G45list}\n\n"
    else:
        G45 = ""

    r = re.compile('.*KWT-FIBER')
    KWTlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'KWT-FIBER:'
    KWTlist = [re.sub(r'KWT-FIBER:', '', s) for s in KWTlist1]
    if KWTlist != []:
        KWT = f"KWT REGION:\n {KWTlist}\n\n"
    else:
        KWT = ""

    r = re.compile('.*ZMM-FIBER')
    ZMMlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'ZMM-FIBER:'
    ZMMlist = [re.sub(r'ZMM-FIBER:', '', s) for s in ZMMlist1]
    if ZMMlist != []:
        ZMM = f"ZMM REGION:\n {ZMMlist}\n\n"
    else:
        ZMM = ""

    r = re.compile('.*ROY-FIBER')
    ROYlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'ROY-FIBER:'
    ROYlist = [re.sub(r'ROY-FIBER:', '', s) for s in ROYlist1]
    if ROYlist != []:
        ROY = f"R&M REGION:\n {ROYlist}\n\n"
    else:
        ROY = ""

    r = re.compile('.*LSM-FIBER')
    LSMlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'LSM-FIBER:'
    LSMlist = [re.sub(r'LSM-FIBER:', '', s) for s in LSMlist1]
    if LSMlist != []:
        LSM = f"LSM REGION:\n {LSMlist}\n\n"
    else:
        LSM = ""

    r = re.compile('.*HTR-FIBER')
    HTRlist1 = list(filter(r.match, data)) # Read Note below
    pattern = r'HTR-FIBER:'
    HTRlist = [re.sub(r'HTR-FIBER:', '', s) for s in HTRlist1]
    if HTRlist != []:
        HTR = f"HTR REGION:\n {HTRlist}\n\n"
    else:
        HTR = ""

    #This will only send data from regions with offline buildings
    compressed = f"{G44}{ZMM}{G45}{ROY}{KWT}{LSM}{HTR}"
    print(compressed)
    return compressed

def main():

    #data = ['G44-FIBER:Chalo', 'G44-FIBER:Classic_Apt', 'G44-FIBER:Elgon_[R]', 'G44-FIBER:Glory', 'G44-FIBER:Helpers', 'G44-FIBER:Imani', 'G44-FIBER:Kwa_Guka', 'G44-FIBER:Lynn', 'G44-FIBER:Magnet', 'G44-FIBER:Mamba_Village', 'G44-FIBER:Ngugi', 'G44-FIBER:PK_Hse', 'G44-FIBER:Uncle_Blue', 'G44-FIBER:Wa_Ruth', 'G44-FIBER:Witu_hse_2', 'G45-FIBER:Counter', 'G45-FIBER:Heri_Points', 'G45-FIBER:Kapkoi_Hse', 'G45-FIBER:Little_Leaders', 'G45-FIBER:Mammy_Wairimu', 'G45-FIBER:Miracle', 'G45-FIBER:Miracle_House', 'G45-FIBER:Mushae', 'G45-FIBER:Suntex', 'G45-FIBER:Zara', 'KWT-FIBER:Jura', 'KWT-FIBER:Wasonga', 'KWT-FIBER:Westham', 'LSM-FIBER:Aeneah', 'LSM-FIBER:Michigan', 'LSM-FIBER:NJ', 'LSM-FIBER:Nike', 'LSM-FIBER:Phonex', 'LSM-FIBER:Rwanda', 'LSM-FIBER:Simba', 'ROY-FIBER:By', 'ROY-FIBER:Deograts', 'ROY-FIBER:Digo', 'ROY-FIBER:Patma', 'ROY-FIBER:Pinkerton', 'ROY-FIBER:Rowan', 'ROY-FIBER:Tallic', 'ZMM-FIBER:Alsina', 'ZMM-FIBER:Hay_Hse', 'ZMM-FIBER:Helsinki', 'ZMM-FIBER:Mt._Nebo', 'ZMM-FIBER:Ring_Ting', 'ZMM-FIBER:Tosheka', 'ZMM-FIBER:Wadosi', 'ZMM-FIBER:Wahome']
    splitdata(data)

if __name__ == "__main__":
    main()