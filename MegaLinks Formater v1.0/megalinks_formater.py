print("MegaLinks Formater v1.0")

megaLinkOrg = input("Paste the link to convert: ")
if "/file/" in megaLinkOrg:
    megaReplace1 = megaLinkOrg.replace("#", "!")
    megaReplace2 = megaReplace1.replace("file/", "#f!")
    print("Your link has been formatted: " + megaReplace2)

elif "/folder/" in megaLinkOrg:
    megaReplace1 = megaLinkOrg.replace("#", "!")
    megaReplace2 = megaReplace1.replace("folder/", "#F!")
    print("Your link has been formatted: " + megaReplace2)

else:
    print("You put it a invalid link or your link no need convertion. Try again!!")

input('Press ENTER to exit')
