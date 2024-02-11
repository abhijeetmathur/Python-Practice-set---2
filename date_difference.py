from datetime import datetime

def difference_in_days(date1, date2):
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')
    difference = abs((date2_obj - date1_obj).days)
    
    return difference

date1 = '2022-01-15'
date2 = '2024-02-10'
print("Difference in days:", difference_in_days(date1, date2))