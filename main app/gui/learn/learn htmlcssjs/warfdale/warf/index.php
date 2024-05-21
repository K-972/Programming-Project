<?php


include 'config.php';
include DOCROOT.'/_template/metahead.php';
include DOCROOT.'/_template/header.php';


?>


<div class="bg-beige">
    <div class="container">
        <div class="row">
            <div class="offset-1 col-3">
                <p>check:in</p>
                <input type="text" class="form-control" value="<?php echo date('d/m/Y'); ?>"/>
            </div>
            <div class="col-3">
                <p>
                    check out:
                </p>
                <input type="text" class="form-control" value="<?php echo date('d/m/Y'); ?>"/>


            </div>
            <div class="col-4">
                <input type="submit" class="btn btn-primary form-control" value="avalibility and book">
            </div>
        </div>
    </div>
</div>


<div class="container exclusive-text">
    <h1>
        Exclusive hire character accommodation for between 4 to 20 people in the very heart of the yorkshire dales
        national park.
    </h1>
    <p>
        Wharfedale Lodge is a beautifully converted Yorkshire Dales barn, set in a stunning location between the
        picturesque villages of Grassington and Kettlewell. Surrounded by green pastures, rivers, waterfalls, springs
        and wild flower meadows, Wharfedale Lodge & Wharfedale View serves as the perfect base to relax with friends and
        family, or an exciting adventure weekend with colleagues.
    </p>
</div>
<div class="text-center">
    <img src="images/Group 46.png" alt="Image underheader" width="100" height="30">
</div>
<div class="bg-beige">
    <div class="container">
        <div class="row image-with-text-row image-left">
            <div class="col-6">
                <div class="image image-one"></div>
            </div>
            <div class="col-6">
                <div class="padded-text">
                    <h2>
                        Wharfedale Lodge
                    </h2>
                    <p>
                        Wharfedale Lodge is a beautifully converted Yorkshire Dales barn providing quality group
                        accommodation for families, friends and businesses. It sleeps up to 20 people in 8 comfortable
                        twin bedrooms and one 2 bunk-bed family room. A spacious cosy lounge, large dining table for 20,
                        extensive commercial kitchen with all equipment provided, games room and generous 2 acre grounds
                        with stunning views across the Wharfedale Valley.
                    </p>
                    <a href="#" class="btn btn-primary">
                        view wharfedale lodge
                    </a>
                </div>
            </div>

        </div>
        <div class="row image-with-text-row image-right">
            <div class="col-6">
                <div class="text-one text-end">
                    <div class="padded-text">
                        <h2>
                            Wharfedale View
                        </h2>
                        <p>Wharfedale View offers the very best smaller group getaway for upto 4 people. A spacious self
                            contained private suite, with ground floor lounge area and dining/kitchen leading to a twin
                            bedroom and further bathroom/shower. A spiral staircase leads to a mezzanine floor bedroom with
                            double bed and a spare single bed.</p>
                        <a href="#" class="btn btn-primary d-inline-block">
                            view wharfedale view
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="image image-two"></div>
            </div>
        </div>
        <div class="row image-with-text-row image-left">
            <div class="col-6">
                <div class="image image-three"></div>
            </div>
            <div class="col-6">
                <div class="padded-text">
                    <h2>
                        Adventures in the Yorkshire Dales
                    </h2>
                    <p>
                        With access to the whole of the Yorkshire Dales National Park right from the doorstep, the lodge is
                        perfectly situated for walking, cycling or just relaxing in the amazing backdrop views of the
                        Wharfedale valley. A 10 min walk to the pub, or short drives to Kettlewell or Skipton villages.
                    </p>
                    <a href="#" class="btn btn-primary">
                        thing to see and do
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
<section class="comfort-bar">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 offset-lg-2">
                <h4>Experience all that Yorkshire has to offer, in a stunning space that can easily accommodate the
                    whole gang.</h4>
            </div>
        </div>
        <a href="#" class="btn btn-primary offset-5">
            availability and booking
        </a>
    </div>
</section>


<?php

include DOCROOT.'/_template/footer.php';


?>


