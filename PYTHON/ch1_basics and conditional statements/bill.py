#a shop is selling three items phone 5000 ipad 20000 imac 50000
cp_phone=5000
cp_ipad=20000
cp_imac=50000
a=int(input("Enter no of units of phone :"))
b=int(input("Enter no of units of ipad : "))
c=int(input("Enter no of units if imac : "))
sp_phone=float(input("Enter Selling Price of phone ="))
sp_ipad=float(input("Enter Selling Price of ipad ="))
sp_imac=float(input("Enter Selling Price of imac ="))

total_cp=(a*cp_phone)+(b*cp_ipad)+(c*cp_imac)
total_sp=(a*sp_phone)+(b*sp_ipad)+(c*sp_imac)
profit=total_sp-total_cp
loss=total_cp-total_sp

print("Total Cost Prize=",total_cp)
print("Total Selling Price =",total_sp)

if total_sp>total_cp :
    print("You make profit of Rs:",profit )
elif total_sp==total_cp:
    print("You make no profit no loss ")
else :
    print("You make loss of Rs:",loss)

print("_________________________---BILL---____________________")
print(" ------- PHONE CONT <",a,"> --------" ,"TOTAL AMOUNT = ",sp_phone,"Rs")
print(" ------- IPad CONT <",a,"> --------" ,"TOTAL AMOUNT = ",sp_ipad,"Rs")
print(" ------- Imac CONT <",a,"> --------" ,"TOTAL AMOUNT = ",sp_imac,"Rs")
print("-------------------Total Amont =",total_sp,"--------------")

