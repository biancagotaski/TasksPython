from datetime import datetime

age = input("Insira a data de nascimento: \n")

def parseAge(age):
    datetime.strptime(age, '%d-%b-%Y')
    time.struct_time(time_year = 1970, time_month = 6, time_mday = 1,
                     time_wday = 2, time_yday = 152, time_isdst = -1)
    print(age)
    
parseAge(age)