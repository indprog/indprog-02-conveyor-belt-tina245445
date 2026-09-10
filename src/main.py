motors = int(input("How many motors are carrying the packages? "))
package_weight = int(input("How many kg of packages do we expect? "))

if package_weight / motors <= 12:
    print("Yes! The conveyor belt can carry the packages.")
else:
    print("No. The conveyor belt cannot carry the packages.")
print("hello!")
