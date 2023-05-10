import pathlib
import blocks.nav
import blocks.hero
import blocks.newsletter
import blocks.services
import blocks.footer

def listComponents():
    print("")
    print("Components:")
    print("Nav: " + str(len(blocks.nav.components)))
    print("Hero: " + str(len(blocks.hero.components)))
    print("Newsletter: " + str(len(blocks.newsletter.components)))
    print("Services: " + str(len(blocks.services.components)))
    print("Footer: " + str(len(blocks.footer.components)))
    print("")


print("""
        ================================
        ========== BLOCKS 1.0 ==========
        ================================
""")
print("? for help")

while True:
    try:
        option = str(input("> "))

    except KeyboardInterrupt:
        print("Finished")
        exit()

    if (option == "?"):
        print()
        print("Usage: [blocks.py] [component]#[variation]")
        print("Example: [blocks.py] hero#1")
        print()
        print("Commands:")
        print()
        print("init: Change to generate mode")
        print("list: List total available components")
        print("?: Display this help message")
        print()

    elif(option == "list"):
        listComponents()
    
    elif(option == "init"):
        print("Start building with blocks:")
        print("Insert the dir path including the new dir name")
        location = str(input("Location: "))
        pathlib.Path(location).mkdir(parents=True, exist_ok=True)
        pathlib.Path(location + "/img").mkdir(parents=True, exist_ok=True)

        with open("./base/index.html", "r") as file:
            base = file.read()

        with open(location + "/index.html", "w") as page:
            page.write(base)

        print("[Base site generated]")
        print()

        while True:
            try:
                generate = str(input("(Generate) > ")).split("#")
            
            except KeyboardInterrupt:
                print("Finished")
                exit()

            if (generate[0] == "nav"):
                blocks.nav.nav(location, int(generate[1]))
            
            elif (generate[0] == "hero"):
                blocks.hero.hero(location, int(generate[1]))

            elif (generate[0] == "newsletter"):
                blocks.newsletter.newsletter(location, int(generate[1]))

            elif (generate[0] == "services"):
                blocks.services.services(location, int(generate[1]))

            elif (generate[0] == "footer"):
                blocks.footer.footer(location, int(generate[1]))

            elif (generate[0] == "list"):
                listComponents()
    
    elif("#" in option):
        print("[init] to turn on generate mode")
        print()