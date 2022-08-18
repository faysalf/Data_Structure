def rate(total_khoroch,total_meal,name,joma,meal_number):
    
    meal_rate = total_khoroch/total_meal
    
    persional_khoroch = meal_number * meal_rate
    pabe_dibe = joma - persional_khoroch
    
    pabe_lite = ""
    if pabe_dibe==0:
        pabe_lite += "OK"
    elif pabe_dibe>0:
        pabe_lite += "%d Tk pabe"%pabe_dibe
    else:
        pabe_lite += "%d Tk dibe"%abs(pabe_dibe)
        
    return ("Meal Rate: %d \nName: %s \nTotal Khoroch %d \n%s"%(meal_rate,name,persional_khoroch,pabe_lite))

b = list(map(int,input("Enter Bazar Cost: ").split()))
total_khoroch = sum(b)
c = list(map(int,input("Enter number of total meal: ").split()))
total_meal = sum(c)
mass_member = int(input("Enter the number of mass member's: "))
for i in range(mass_member):
    name = input("Please enter a member's name: ")
    joma = int(input("%s's joma: "%name))
    d = list(map(int,input("Enter number of %s's meals: "%name).split()))
    meal_number = sum(d)
    print(rate(total_khoroch,total_meal,name,joma,meal_number))
