import library.copyimg

components = ["""
    
    <!-- Footer -->
    <section class="bg-dark p-5 text-white text-center position-relative">
        <div class="container">
            <p class="lead"> Copyright &copy; Yellow Pages Cabo Verde 2023 </p>

            <a href="#" class="position-absolute bottom-0 end-0 p-5">
                <i class="bi bi-arrow-up-circle h1"></i>
            </a>
        </div>
    </section>
    <!--end-->
    """,
    ]

def footer(location, variation):
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