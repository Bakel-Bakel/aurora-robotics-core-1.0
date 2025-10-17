#tipping
# if the service is good lets give then 15% tip.
# if the service is mehhh lets give them 10% tip.

bill = float(input("Enter the total bill amount: $"))
service = input("How was the service? (good/mehhh): ").lower()

if service == "good":
    tip = bill * 0.15
elif service == "mehhh":
    tip = bill * 0.10
else:
    tip = 0

print(f"Based on the {service} service, a {tip} tip is suggested.")


#TASK 3
#Implement this bill but with star ratings