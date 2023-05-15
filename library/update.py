import pathlib
import blocks.nav
import blocks.hero

def update():
    location = "display/"
    navs = len(blocks.nav.components)
    heroes = len(blocks.hero.components)

    # Here we update every group of components.
    # When the command is issued we will go through all the variations available and paste
    # them into their respective pages.

    # We first copy the base bootstrap template to the correct display file. Then we use
    # the already existing code to place components on a page, except this time we do a loop
    # to go through the complete length of the list of available components.

    # Update navs

    with open("./base/index.html", "r") as file:
        base = file.read()

    with open(location + "/navs.html", "w") as page:
        page.write(base)
    
    for variation in range(navs):
        
        # We call the component placement function and pass it a location, the current variation
        # and True to let it know we are doing an update.

        blocks.nav.nav(location + "/navs.html", variation, True)


    # Update heroes

    with open("./base/index.html", "r") as file:
        base = file.read()

    with open(location + "/heroes.html", "w") as page:
        page.write(base)
    
    for variation in range(heroes):
        blocks.hero.hero(location + "/heroes.html", variation, True)