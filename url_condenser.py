

def monthly_condense(query, year):
    all_urls = []
    for i in range(1,13):
        if i<10:
            month = '0'+str(i)
        else:
            month = str(i)
        filename = query+"_"+year+"/"+query+"_"+year+"-"+month+"-01.txt"
        f = open(filename, "r") 
        # "lamda_2022/lamda_2022-01-01.txt"
        urls = f.read()
        f.close()
        urls_list = urls.replace("\n",' ').split()
        print(len(urls_list))
        all_urls+=urls_list
        all_urls = list(set(all_urls))
        print("count")
        print(len(all_urls))
    f = open(query+"_"+year+"/"+query+"_"+year+"_total.txt", "w+") 
    for url in all_urls:
        f.write(url+"\n")
    f.close()

def biweekly_condense(query, year):
    all_urls = []
    days = ['01','16']
    for i in range(1,7):
        if i<10:
            month = '0'+str(i)
        else:
            month = str(i)
        for day in days:
            filename = query+"_"+year+"/"+query+"_"+year+"-"+month+"-"+day+".txt"
            f = open(filename, "r") 
            # "lamda_2022/lamda_2022-01-01.txt"
            urls = f.read()
            f.close()
            urls_list = urls.replace("\n",' ').split()
            print(len(urls_list))
            all_urls+=urls_list
            all_urls = list(set(all_urls))
            print("count")
            print(len(all_urls))
    f = open(query+"_"+year+"/"+query+"_"+year+"_total.txt", "w+") 
    for url in all_urls:
        f.write(url+"\n")
    f.close()


def weekly_condense(query, year):
    all_urls = []
    days = ['01','08','16','24']
    for i in range(1,7):
        if i<10:
            month = '0'+str(i)
        else:
            month = str(i)
        for day in days:
            filename = query+"_"+year+"/"+query+"_"+year+"-"+month+"-"+day+".txt"
            f = open(filename, "r") 
            # "lamda_2022/lamda_2022-01-01.txt"
            urls = f.read()
            f.close()
            urls_list = urls.replace("\n",' ').split()
            print(len(urls_list))
            all_urls+=urls_list
            all_urls = list(set(all_urls))
            print("count")
            print(len(all_urls))
    f = open(query+"_"+year+"/"+query+"_"+year+"_total.txt", "w+") 
    for url in all_urls:
        f.write(url+"\n")
    f.close()          

#weekly_condense("Vicuna", "2023")

def check_dec20():
    all_urls = []
    filename = "mixtral_2023-12-20.txt"
    f = open(filename, "r") 
    urls = f.read()
    f.close()
    urls_list = urls.replace("\n",' ').split()
    all_urls+=urls_list
    all_urls = list(set(all_urls))
    print("count")
    print(len(all_urls))
    filename = "mistral_2023-12-20.txt"
    f = open(filename, "r") 
    urls = f.read()
    f.close()
    urls_list = urls.replace("\n",' ').split()
    all_urls+=urls_list
    all_urls = list(set(all_urls))
    print("count")
    print(len(all_urls))
    filename = "Vicuna_2023-12-20.txt"
    f = open(filename, "r") 
    urls = f.read()
    f.close()
    urls_list = urls.replace("\n",' ').split()
    all_urls+=urls_list
    all_urls = list(set(all_urls))
    print("count")
    print(len(all_urls))

check_dec20()