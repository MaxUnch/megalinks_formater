# Title:
print("""

___  ___                 _    _____      _         ______                         _                     __    __
|  \/  |                | |  |_   _|    | |        |  ___|                       | |                   /  |  /  |
| .  . | ___  __ _  __ _| |    | | _ __ | | _____  | |_ ___  _ __ _ __ ___   __ _| |_ ___ _ __  __   __`| |  `| |
| |\/| |/ _ \/ _` |/ _` | |    | || '_ \| |/ / __| |  _/ _ \| '__| '_ ` _ \ / _` | __/ _ \ '__| \ \ / / | |   | |
| |  | |  __/ (_| | (_| | |____| || | | |   <\__ \ | || (_) | |  | | | | | | (_| | ||  __/ |     \ V / _| |___| |_
\_|  |_/\___|\__, |\__,_\_____|___/_| |_|_|\_\___/ \_| \___/|_|  |_| |_| |_|\__,_|\__\___|_|      \_/  \___(_)___/
              __/ |
             |___/

""")

print("                                             Created with love by MaxUnch\n")

input("                                       |--[Press Enter to begin the process]--|")


# Opening the file in only-read mode:
try:
    fileR = open("NewMegaLinks.txt", "r")
    # Save the content readed line by line:
    txtReaded = fileR.readlines()
finally:
    fileR.close()
# -----------------------------------------------------------------------------
# OlD Links:
print("\n                                             [NEW MEGA LINKS FORMAT]\n")
# Read line by line to format:
x = 0
s = 0
for link in txtReaded:
    if "/file/" in link:
        print(link)
        x += 1
    elif "/folder/" in link:
        print(link)
        x += 1
    else:
        print("*-Invalid Format-*\n")
        s += 1
# Count the number of links found:
print(f"\n### {s} invalid link/s and {x} valid link/s have been found ###")
# -----------------------------------------------------------------------------
# NEW Links:
print("\n                                             [OLD MEGA LINKS FORMAT]\n")
# Formating link by link:
y = 0
z = 0
saveLines = []
for line in txtReaded:
    if "/file/" in line:
        megaReplace1 = line.replace("#", "!")
        megaReplace2 = megaReplace1.replace("/file/", "/#f!")
        print(megaReplace2)
        saveLines.insert(y, megaReplace2)
        y += 1
    elif "/folder/" in line:
        megaReplace1 = line.replace("#", "!")
        megaReplace2 = megaReplace1.replace("/folder/", "/#F!")
        print(megaReplace2)
        saveLines.insert(y, megaReplace2)
        y += 1
    else:
        print("*-Invalid Format-*\n")
        z += 1
# Count the number of links formatted:
print(f"\n### {z} invalid link/s and {y} valid link/s have been formatted ###\n")
# -----------------------------------------------------------------------------
# Verify the txt. file to write results:
try:
    fileW = open("OldMegaLinks.txt", "w")
    for writeLine in saveLines:
        fileW.write(writeLine + "\n")
finally:
    fileW.close()
print("### ALL DONE ###")
input("\n                                             |--[Press Enter to Finish]--|")
