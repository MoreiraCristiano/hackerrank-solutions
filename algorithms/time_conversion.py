def timeConversion(s):
    conversion_table = {
        '01': ['01', '13'],
        '02': ['02', '14'],
        '03': ['03', '15'],
        '04': ['04', '16'],
        '05': ['05', '17'],
        '06': ['06', '18'],
        '07': ['07', '19'],
        '08': ['08', '20'],
        '09': ['09', '21'],
        '10': ['10', '22'],
        '11': ['11', '23'],
        '12': ['00', '12'],
    }

    if s.find('PM') != -1:
        # Horario PM para Militar
        pm_time = s[0:2]
        min_sec = s[2:8]

        converted = conversion_table[pm_time][1] + min_sec
        return converted

    if s.find('AM') != -1:
        # Horario AM para Militar
        am_time = s[0:2]
        min_sec = s[2:8]

        converted = conversion_table[am_time][0] + min_sec
        return converted


s = '12:05:45AM'
print(timeConversion(s))
