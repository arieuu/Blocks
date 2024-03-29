import library.copyimg

components = ["""
    
    <!-- HERO -->

    <style>

        @media (min-width: 768px) {
            .news-input {
                width: 50%;
            }

            .hero {
                background-image: url(img/hero0.jpeg);
                height: 560px;
            }
        }

        .hero {
            background-image: url(img/hero0.jpeg);
        }

    </style>

        <section class="hero bg-dark text-light p-5 text-center text-sm-start p-lg-0 pt-lg-5 d-sm-flex align-items-center justify-content-center">
            <div class="container" style="background-color: rgba(0, 0, 0, 0.6)">
                <div class="d-sm-flex align-items-center justify-content-center text-center p-lg-5">
                    <div>
                        <h1> One of the top <span class="text-warning"> IT consulting firms </span> around </h1>

                        <p class="lead my-4">
                            We deliver fast, specialized services for the best prices around.
                            We promise and we never fail on our word!
                        </p>

                        <div class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#enroll"> Contact us </div>
                    </div>

                </div>
            </div>
        </section>
        <!--end-->
    """,

   """
    <!-- HERO -->
        <section class="bg-dark text-light p-5 text-center text-sm-start p-lg-0 pt-lg-5">
            <div class="container">
                <div class="d-sm-flex align-items-center justify-content-between">
                    <div>
                        <h1> One of the top <span class="text-warning"> IT consulting firms </span> around </h1>

                        <p class="lead my-4">
                            We deliver fast, specialized services for the best prices around.
                            We promise and we never fail on our word!
                        </p>

                        <div class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#enroll"> Contact us </div>
                    </div>

                    <img class="img-fluid w-50 d-none d-sm-block" src="img/hero1.svg" alt="">
                </div>
            </div>
        </section>
        <!--end-->
   """
    
    ]

def hero(location, variation, update=False):
    
    # If update is false then it's just a component placement. The user is generating a component.

    if(update == False):
        imgLocation = location # If we're generating we will need to create an img folder in the base dir
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

        if(update == False):
            library.copyimg.copyimg("hero", variation, imgLocation)
