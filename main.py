import pathlib
import blocks.nav
import blocks.hero

print("Start building with blocks")
print("? for help")

while True:
    try:
        option = str(input("> "))

    except KeyboardInterrupt:
        print("Finished")
        exit()

    if (option == "?"):
        print("Usage: [blocks.py] footer#[1,2,3,4,5]")
        print("Example: [blocks.py] footer#1")
        print("===========")
        print("""Available:
            nav
            hero
            newsletter
            footer""")
    
    elif(option == "init"):
        print("Insert the dir path including the new dir name")
        location = str(input("Insert a location: "))
        pathlib.Path(location).mkdir(parents=True, exist_ok=True)

        with open("./base/index.html", "r") as file:
            base = file.read()

        with open(location + "/index.html", "w") as page:
            page.write(base)

        print("[Base site generated]")

        while True:
            try:
                generate = str(input("(Generate) => ")).split("#")
            
            except KeyboardInterrupt:
                print("Finished")
                exit()

            if (generate[0] == "nav"):
                blocks.nav.nav(location, int(generate[1]))
            
            elif (generate[0] == "hero"):
                blocks.hero.hero(location, int(generate[1]))

    elif (option == "nav#1"):
        print(blocks.nav.navigations(1))
    
    elif (option == "hero#1"):
        print(blocks.hero.hero(1))