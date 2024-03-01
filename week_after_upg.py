from datetime import datetime,timedelta
def week_after(input_date):
    data = "%d/%m/%Y"
    try:
        input_date = datetime.strptime(input_date,data)
    except ValueError:
        return None
    # 7 kun qo'shib olamiz 
    # timedelta o'zi hisoblab beradi
    result_date = input_date + timedelta(days=7)
    return result_date.strftime(data)
date = input("Pls enter the date (day/month/year) : ")
result = week_after(date)
#check result
if result:
    print(f"After a week : {result}")
else:
    print("There is a mistake! Try again")
# agar result da qiymat bo'lsa ishlaydi aks holda ishlamidi