#pizza order calc
#four family members
#total slices
#whole pizzas
#slices left over
#no loops or lists
#family members and how much they eat
member1 = int(input("How many slices will family member 1 eat? "))
member2 = int(input("How many slices will family member 2 eat? "))
member3 = int(input("How many slices will family member 3 eat? "))
member4 = int(input("How many slices will family member 4 eat? "))
#total slices eaten by the family
total_slices = member1 + member2 + member3 + member4
whole_pizzas = total_slices // 8
#if the number of slices divided by 8 isn't equal to zero, add another pizza
if total_slices / 8 != 0:
    whole_pizzas = whole_pizzas + 1
#slices left over
Slices_Left_Over = (whole_pizzas * 8) - total_slices
#add a space here just to make it look pretty
print()
print("Total slices needed:", total_slices)
print("Whole pizzas to order:", whole_pizzas)
print("Slices left over:", Slices_Left_Over)
