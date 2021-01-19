import re

def checkID(idnumber):
    idchk = "0123456789ABCDEFGHJKLMNPQRSTUVXYWZIO"
    pattern = '^[A-Z]{1}(1|2)\\d{8}$'
    idnumber = idnumber.upper()

    if re.match(pattern, idnumber):
        n1 = idchk.find(idnumber[0])
        total = int(n1/10+(n1%10)*9)

        for i in range(1,9):
            total += idchk.find(idnumber[i])*(9-i)

        total += idchk.find(idnumber[9])

        if total%10 == 0:
            return True
        else:
            return False
    else:
        return False