# finds missing coins for collection in tip.cc

# gets all crypto
with open("check_all.txt") as all:
    all_currencies = []
    for line in all:
        x = line[line.index(":", 1)+1: line.index("(")].strip()
        all_currencies.append(x)

# gets all owned crypto
with open("check_mine.txt") as mine:
    all_mine = []
    for line in mine:
        x = line.split(":")[0]
        if "(" in x:
            x = x.split("(")[0].strip()
        all_mine.append(x)

missing = []

# filters out owned and keeps missing
for x in all_currencies:
    if x not in all_mine:
        if x == "Name Change Token":
            x = "NCT"
        elif x == "DexKit":
            x = "DexKit (BSC)"
        missing.append(x)

missing.sort()

# displays result to check_missing.txt
with open("check_missing.txt", "w") as donthave:
    donthave.write("Result: \n")
    donthave.write("----------------------------------------------------------------------------------------------------\n")
    if len(missing) > 1:
        donthave.write("$bals ")
        for i in range(len(missing)):
            if i == len(missing)-1:
                donthave.write(missing[i])
            else:
                donthave.write(missing[i] + ", ")
    elif len(missing) == 1:
        donthave.write("$bal " + missing[0])
    else:
        donthave.write("Congrats you got them all!")
    donthave.write("\n----------------------------------------------------------------------------------------------------\n")

    donthave.write("\n\n\n" + "Total Currencies: " +
                   str(len(all_currencies)) + "\n")
    donthave.write("Total Owned: " + str(len(all_mine)) + "\n")
    donthave.write("Total Missing: " + str(len(missing)) + "\n")

print(("----------------------------------------------------------------------------------------------------"))
print("Success!!!")
print(("----------------------------------------------------------------------------------------------------"))