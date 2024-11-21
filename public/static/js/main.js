document.addEventListener('DOMContentLoaded', function () {
  // Get references to the spinner and feedback form
  const spinner_ = document.getElementById('spinner');
  const generate_tour = document.getElementById('generate-tour');
  const Sub_btn = document.getElementById('Submit_btn');

  // Add event listener to the form submission
  if (generate_tour){
    generate_tour.addEventListener('submit', function (e) {
        // Show the spinner by adding the 'show' class
        spinner_.classList.add('show');
  
        // Disable the button to prevent multiple submissions
        Sub_btn.disabled = true;
    });
  }
});


document.addEventListener('DOMContentLoaded', function () {
  // Get references to the spinner and feedback form
  const spinner = document.getElementById('spinner');
  const Form_ = document.getElementById('Form');
  const Submit_btn = document.getElementById('Submit_btn');

  // Add event listener to the form submission
  if (Form_){
    Form_.addEventListener('submit', function (e) {
        // Show the spinner by adding the 'show' class
        spinner.classList.add('show');
  
        // Disable the button to prevent multiple submissions
        Submit_btn.disabled = true;
    });
  }
});


// For auto Scrolling in generate plan or forts found
document.addEventListener("DOMContentLoaded", function() {
  const forts_found = document.getElementById("forts_found"); 
  const generatedplan = document.getElementById("generatedplan");
  const alert_ = document.getElementById("alert");

  if (forts_found) {
    forts_found.scrollIntoView({ behavior: "smooth" });
  }

  if (generatedplan) {
    // generatedplan.scrollIntoView({ behavior: "smooth" });
    generatedplan.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  if (alert_){
    alert_.scrollIntoView({ behavior: "smooth" });
  }
});

function showDirections(button) {
  // Get the value of the data-item attribute
  var itemData = button.getAttribute('data-item');

  // Split the data-item attribute to extract latitude and longitude
  var coordinates = itemData.split(',');
  var latitude = coordinates[0].trim(); // Latitude
  var longitude = coordinates[1].trim(); // Longitude

  // Construct the Google Maps URL
  var mapsUrl = "https://www.google.com/maps?q=" + latitude + "," + longitude;

  // Open Google Maps in a new tab
  window.open(mapsUrl, "_blank");
}




(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();



    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });

})(jQuery);




$(document).ready(function() {
    $("#get-user-location").click(function() {
        navigator.geolocation.getCurrentPosition(function(position) {
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Show loading indicator
            // $('#user-loc-animation').show();
            $('#spinner').addClass('show');

            // Send coordinates to djabgo using AJAX 
            $.ajax({
                url: "send-coordinates/",
                type: "POST",
                headers: {
                  'X-CSRFToken': csrfToken  // Add the CSRF token here
                },
                data: {
                    latitude: latitude,
                    longitude: longitude,
                },
                dataType : "json",
                success: function(response) {
                      console.log(response.success_msg);

                      $('#spinner').removeClass('show');
                }
            });
        }, function(error) {
            console.error("Error getting geolocation:", error);
            alert("Error getting your location. Please check your browser settings.");
        });
    });
});





var multipleCardCarousel = document.querySelector("#carouselExampleControls");
if(multipleCardCarousel){
    if (window.matchMedia("(min-width: 768px)").matches) {
        var carousel = new bootstrap.Carousel(multipleCardCarousel, {
          interval: false,
        });
        var carouselWidth = $(".carousel-inner")[0].scrollWidth;
        var cardWidth = $(".carousel-item").width();
        var scrollPosition = 0;
        $("#carouselExampleControls .carousel-control-next").on("click", function () {
          if (scrollPosition < carouselWidth - cardWidth * 4) {
            scrollPosition += cardWidth;
            $("#carouselExampleControls .carousel-inner").animate(
              { scrollLeft: scrollPosition },
              600
            );
          }
        });
        $("#carouselExampleControls .carousel-control-prev").on("click", function () {
          if (scrollPosition > 0) {
            scrollPosition -= cardWidth;
            $("#carouselExampleControls .carousel-inner").animate(
              { scrollLeft: scrollPosition },
              600
            );
          }
        });
    } else {
        $(multipleCardCarousel).addClass("slide");
    }
}


