def print_weekly():
    x = []
    y = []
    days = ['01', '03', '05', '07', '09', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29']
    days_end = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28']

    for month in range(1,7):
        if month<10:
            start = "2024-0"
        else:
            start = "2024-"
        for i in range(len(days)):
            created_date_from = start+str(month)+'-'+days[i]
            if month==2 and days[i]=='29':
                created_date_to = start+str(month)+'-29'
            elif ((month<8 and month%2==1) or (month>=8 and month%2==0)) and days[i]=='29':
                created_date_to = start+str(month)+'-31'
            elif ((month<8 and month%2==0) or (month>=8 and month%2==1)) and days[i]=='29':
                created_date_to = start+str(month)+'-30'
            else:
                created_date_to = start+str(month)+'-'+days_end[i]
            
            x.append(created_date_from)
            y.append(created_date_to)
    print(x)
    print(y)

#print_weekly()

def print_daily():
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30','31']
    x = []
    for month in range(1,13):
        if month<10:
            start = "2023-0"
        else:
            start = "2023-"
        for i in range(len(days)):
            if month==2 and days[i]=='28':
                created_date_from = start+str(month)+'-28'
                x.append(created_date_from)
                break
            elif ((month<8 and month%2==0) or (month>=8 and month%2==1)) and days[i]=='30':
                created_date_from = start+str(month)+'-30'
                x.append(created_date_from)
                break
            else:
                created_date_from = start+str(month)+'-'+days[i]
                x.append(created_date_from)
    
    print(x)

print_daily()
days = ['01', '03', '05', '07', '09', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29']
days_end = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28','30']


#print(all_days)   
#["2023-12-16","2023-12-17","2023-12-18","2023-12-19","2023-12-20","2023-12-21","2023-12-22",,"2023-12-23"]
#["2023-12-17","2023-12-19","2023-12-21","2023-12-23"]