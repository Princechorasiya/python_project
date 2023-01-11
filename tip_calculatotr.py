print("Welcome to the tip calculator.")
total_bill=input("What was the total bill?$")
split_btw=input("How many people to split the bill?")
percentage_of_tip=input("What percentage tip would you like to give? 10,12, or 15?")
percentage_of_tip_1=int(percentage_of_tip)/100
tip=float(total_bill)*percentage_of_tip_1
tip_1=f"Tip tp pay is:${tip}"
print(tip_1)
total=eval(total_bill)+tip
total_per_person=round(float(total)/int(split_btw),2)
bill=f"Each person should pay:${total_per_person}"
print(bill)

