print("sales report for 2022")
firstnumber = int(input("input the first amount for january"))
secondnumber = int(input("input the second amount for febuary")) 
thirdnumber = int(input("input the third amount for march"))
fourthnumber = int(input("input the fourth amount for april"))
fifthnumber = int(input("input the fifth amount for may"))
sixthnumber = int(input("input the sixth amount for june"))
seventhnumber = int(input("input the seventh amount for july"))
eighthnumber = int(input("input the eighth amount for august"))
ninthnumber = int(input("input the ninth amount for september"))
tenthnumber = int(input("input the tenth amount for october"))
eleventhnumber = int(input("input the eleventh for november"))
twelthnumber = int(input("input the twelth amount for december"))
totalsalesfor2022 = firstnumber + secondnumber + thirdnumber + fourthnumber + fifthnumber + sixthnumber + seventhnumber + eighthnumber + ninthnumber + tenthnumber + eleventhnumber + twelthnumber
averagesales = totalsalesfor2022/12
print ("The total sales for 2022 is:£",round(totalsalesfor2022,2))
print ("the average sales for 2022 is £",round(averagesales,2))