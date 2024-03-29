import library.copyimg

components = ["""
    
    <!-- NAVIGATION -->
    
    <style>
        body::before {
            display: block;
            content: "";
            height: 60px;
            }
    </style>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark py-4 fixed-top">
        <div class="container">
            <a href="#" class="navbar-brand"> Executive lawyer firm </a>

            <!-- HAMBURGER MENU BUTTON -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navmenu">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- COLLAPSABLE NAVIGATION -->
            <div class="collapse navbar-collapse" id="navmenu">
                <ul class="navbar-nav ms-auto">

                    <li class="nav-item">
                        <a href="#" class="nav-link"> Home </a>
                    </li>

                    <li class="nav-item">
                        <a href="#about" class="nav-link"> About </a>
                    </li>

                    <li class="nav-item">
                        <a href="#testimonials" class="nav-link"> Testimonials </a>
                    </li>

                    <li class="nav-item">
                        <a href="#contact-info" class="nav-link"> Contact info </a>
                    </li>
                </ul>
            </div>
        </div>

    </nav> 

    <!--end-->
    """,
]

def nav(location, variation, update=False):
    if(update == False):
        location = location + "/index.html" # Set the main page

    if((variation + 1) > len(components) or variation < 0):
        print("Component not available")
        return
    
    # Inserting the component

    else:
        with open(location, "r") as file:
            if(update == False):
                content = file.read().replace("<!--end-->", components[variation])

            # If there's an update going on we add the variation number to the component

            else:
                content = file.read().replace("<!--end-->", str(variation) + components[variation])

        with open(location, "w") as page:
            page.write(content)

        
        # Copying image over if there's one

        library.copyimg.copyimg("nav", variation, location)