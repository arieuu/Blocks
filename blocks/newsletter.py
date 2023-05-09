import library.copyimg

components = ["""
    
    <!-- NEWSLETTER -->
    <section class="bg-primary text-light p-5">
        <div class="container ">
            <div class="d-md-flex justify-content-between align-items-center">
                <h3 class="mb-3 mb-md-0"> Sign Up For Our Newsletter </h3>

                <div class="input-group news-input">
                    <input type="text" class="form-control" placeholder="Enter Email" />
                    <button class="btn btn-dark btn-lg" type="button"> Submit </button>
                </div>

            </div>
        </div>
    </section>
    <!--end-->
    """,
    ]

def newsletter(location, variation):
    if((variation + 1) > len(components) or variation < 0):
        print("Component not available")
        return
    
    # Inserting the component

    else:
        with open(location + "/index.html", "r") as file:
            content = file.read().replace("<!--end-->", components[variation])

        with open(location + "/index.html", "w") as page:
            page.write(content)

        
        # Copying image over if there's one

        library.copyimg.copyimg("nav", variation, location)