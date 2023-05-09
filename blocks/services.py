import library.copyimg

components = ["""
    
    <!-- SERVICES -->
    <section class="p-5">
        <div class="container">
            <div class="row text-center g-5">
                
                <!-- FIRST CARD -->
                <div class="col-md text-center">
                    <div class="card bg-dark text-light ">
                        <div class="card-body text-center">
                            <div class="h1 mb-3">
                                <i class="bi bi-laptop"></i>
                            </div>

                            <div class="card-title mb-3"> <h3> Virtual </h3> </div>
                            
                            <div class="card-text mb-4"> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore blanditiis fugit deserunt, sunt eaque soluta! </div>

                            <a href="#" class="btn btn-primary"> Read more </a>
                        </div>
                    </div>
                </div>
                
                <!-- SECOND CARD -->
                <div class="col-md text-center">
                    
                    <div class="card bg-secondary text-light ">
                        <div class="card-body text-center">
                            <div class="h1 mb-3">
                                <i class="bi bi-person-square"></i>
                            </div>

                            <div class="card-title mb-3"> <h3> Hybrid </h3> </div>
                            
                            <div class="card-text mb-4"> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore blanditiis fugit deserunt, sunt eaque soluta! </div>

                            <a href="#" class="btn btn-dark"> Read more </a>
                        </div>
                    </div>
                </div>


                <!-- THIRD CARD -->
                <div class="col-md text-center">
                    <div class="card bg-dark text-light ">
                        <div class="card-body text-center">
                            <div class="h1 mb-3">
                                <i class="bi bi-people"></i>
                            </div>

                            <div class="card-title mb-3"> <h3> In person </h3> </div>
                            
                            <div class="card-text mb-4"> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore blanditiis fugit deserunt, sunt eaque soluta! </div>

                            <a href="#" class="btn btn-primary"> Read more </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>
    <!--end-->

   """]

def services(location, variation):
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