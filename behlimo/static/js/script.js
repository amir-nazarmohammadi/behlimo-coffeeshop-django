jQuery(function ($) {

    'use strict';

    // Mean menu
    jQuery('.mean-menu').meanmenu({
        meanScreenWidth: "1059"
    });
    // Sticky navbar
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 500) {
            $('.navbar-area').addClass('is-sticky');
        } else {
            $('.navbar-area').removeClass('is-sticky');
        }
    });

    // Preloader
    $('body').addClass('pre-loaded');

    // Scrolltop
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 300) {
            $("#scrolltop").fadeIn();
        }
        else {
            $("#scrolltop").fadeOut();
        }
    });

    $("#scrolltop").on('click', function () {
        $("html").animate({
            scrollTop: 0
        }, 2000);
        return false;
    });

    // Timer countdown
    function comingSoon() {
        var countDate = new Date("15 October 2022 9:56:00");
        var sec = 1000;
        var min = sec * 60;
        var hr = min * 60;
        var day = hr * 24;
        var today = new Date();
        var distance = countDate - today;
        var days = Math.floor(distance / day);
        var hours = Math.floor((distance % day) / hr);
        var mins = Math.floor((distance % hr) / min);
        var secs = Math.floor((distance % min) / sec);
        $(".day1").html(days + "<span>Days :</span>")
        $(".hr1").html(hours + "<span>Hrs :</span>")
        $(".min1").html(mins + "<span>Mins :</span>")
        $(".sec1").html(secs + "<span>Sec</span>")
        if (distance < 0) {
            clearInterval(comingSoon);
            $(".coming-soon-counter").html("Session Expired");
        }
    }
    setInterval(function () {
        comingSoon();
    }, 1000)

    // Tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Index page revolution slider
    $('#rev_slider_1').show().revolution({
        sliderLayout: 'auto',
        delay: 3000,
        onHoverStop: 'off',
        // stopAfterLoops:0,
        // stopAtSlide:1,
        responsiveLevels: [1240, 1024, 778, 480],
        gridwidth: [1170, 1170, 778, 480],
        gridheight: [800, 1050, 1000, 885],
        navigation: {
            arrows: {
                enable: false,
            },
            bullets: {
                enable: true,
                style: "ares",
                hide_onleave: false,
                v_align: "bottom",
                h_offset: 0,
                space: 5,
                tmp: ''
            }
        }
    });

    // Index page 2 revolution slider
    $('#rev_slider_2').show().revolution({
        sliderLayout: 'auto',
        delay: 3000,
        onHoverStop: 'off',
        responsiveLevels: [1240, 1024, 778, 480],
        gridwidth: [1170, 1170, 778, 480],
        gridheight: [800, 1050, 1000, 900],
        navigation: {

            arrows: {
                enable: false,
            },
            bullets: {
                enable: false,
                style: "ares",
                hide_onleave: false,
                v_align: "bottom",
                h_offset: 0,
                space: 5,
                tmp: ''
            }
        }
    });

    // Index page 3 revolution slider
    $('#rev_slider_3').show().revolution({
        sliderLayout: 'auto',
        delay: 3000,
        onHoverStop: 'off',
        responsiveLevels: [1240, 1024, 778, 480],
        gridwidth: [1170, 1170, 778, 480],
        gridheight: [800, 1280, 1250, 950],
        navigation: {

            arrows: {
                enable: false,
            },
            bullets: {
                enable: true,
                style: "ares",
                hide_onleave: false,
                v_align: "bottom",
                h_offset: 0,
                space: 5,
                tmp: ''
            }
        }
    });

    // Header-carousel
    $('.header-carousel').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: true,
        dotsEach: 1,
        items: 1,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 4500,
        smartSpeed: 1500,
        rtl: true
    })

    // Header-carousel-two
    $('.header-carousel-two').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        dots: false,
        items: 1,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 4500,
        smartSpeed: 1500,
        autoHeight: true,
        rtl: true
    })

    // Header-carousel-three
    var headerCarouselThree = $(".header-carousel-three")
    headerCarouselThree.owlCarousel({
        loop: true,
        margin: 20,
        nav: false,
        dots: true,
        dotsEach: 1,
        items: 1,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 4500,
        smartSpeed: 1500,
        rtl: true
    })
    $(".header-control-next").click(function () {
        headerCarouselThree.trigger('next.owl.carousel', [1500]);
    })
    $(".header-control-prev").click(function () {
        headerCarouselThree.trigger('prev.owl.carousel', [1500]);
    })

    // Language-switcher
    $(".language-option").each(function () {
        var each = $(this)
        each.find(".lang-compo").html(each.find(".language-dropdown-menu a:nth-child(1)").html());
        var allOptions = $(".language-dropdown-menu").children('a');
        each.find(".language-dropdown-menu").on("click", "a", function () {
            allOptions.removeClass('selected');
            $(this).addClass('selected');
            $(this).closest(".language-option").find(".lang-compo").html($(this).html());
        });
    })

    // Menu-main-carousel-area
    $('.menu-main-details-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        infinite: false,
        draggable: false,
        asNavFor: '',
        speed: 1500,
        rtl: true
    });
    $('.menu-main-thumb-nav').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        asNavFor: '',
        dots: false,
        focusOnSelect: true,
        arrows: false,
        infinite: false,
        draggable: false,
        rtl: true,
        responsive: [
            {
                breakpoint: 991,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    arrows: true,
                    draggable: true,
                    infinite: true,
                    prevArrow: '<i class="flaticon-left-arrow-2 prev-arrow"></i>',
                    nextArrow: '<i class="flaticon-right-arrow-3 next-arrow"></i>',
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    arrows: true,
                    draggable: true,
                    infinite: true,
                    prevArrow: '<i class="flaticon-left-arrow-2 prev-arrow"></i>',
                    nextArrow: '<i class="flaticon-right-arrow-3 next-arrow"></i>',
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    arrows: true,
                    draggable: true,
                    infinite: true,
                    prevArrow: '<i class="flaticon-left-arrow-2 prev-arrow"></i>',
                    nextArrow: '<i class="flaticon-right-arrow-3 next-arrow"></i>',
                }
            },
        ]
    });
    $('.menu-details-carousel').slick({
        centerMode: true,
        centerPadding: '0',
        slidesToShow: 3,
        infinite: true,
        autoplay: false,
        autoplaySpeed: 3000,
        speed: 1300,
        rtl: true,
        prevArrow: '<i class="flaticon-left-arrow-2 prev-arrow"></i>',
        nextArrow: '<i class="flaticon-right-arrow-3 next-arrow"></i>',
        responsive: [
            {
                breakpoint: 991,
                settings: {
                    centerPadding: '180px',
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    centerPadding: '0px',
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
    });

    // Testimonial-carousel
    $('.testimonial-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: true,
        dotsEach: 3,
        items: 3,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 3000,
        smartSpeed: 1500,
        rtl: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    })

    // Magnific-popup
    $("#video-popup").magnificPopup({
        disableOn: 0,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });

    // Team-carousel
    $('.team-carousel').owlCarousel({
        loop: true,
        margin: 30,
        nav: false,
        dots: true,
        items: 4,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 3000,
        smartSpeed: 1500,
        dotsEach: 4,
        rtl: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 4
            }
        }
    })

    // Datepicker
    $("#datepicker").datepicker({
        isRTL: true
    });

    // Timepicker
    $('.timepicker').timepicker({});

    // Change password view
    $(".input-group-text").on('click', function () {
        var $password = $(this).parent().siblings(".password");
        $(this).toggleClass("active");
        if ($password.attr('type') === 'password') {
            $password.attr('type', 'text');
        } else {
            $password.attr('type', 'password');
        }
    })

    // Billing-address-input
    $(".billing-title p").on("click", function () {
        $(".billing-address").addClass("none");
        $(".billing-address-input").addClass("active");
    })

    // Gallery-grid
    $('.gallery-grid').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
            titleSrc: function (item) {
                return item.el.attr('title') + '<small>by Fafo</small>';
            }
        }
    });

    // Faq-accordion
    $(".faq-accordion-header").on("click", function () {
        $(this).parent(".faq-accordion-item").toggleClass("faq-accordion-item-active").siblings().removeClass("faq-accordion-item-active")
    })

    // Range slider
    $("#range-slider").slider({
        range: true,
        min: 40,
        max: 400,
        values: [40, 400],
        slide: function (event, ui) {
            $("#price-amount").val("$" + ui.values[0] + " â€• $" + ui.values[1]);
        }
    });
    $("#price-amount").val("$" + $("#range-slider").slider("values", 0) +
    " - $" + $("#range-slider").slider("values", 1));

    // Product-details-slider
    $('.product-details-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.product-details-nav',
        speed: 1200,
        infinite: false,
        rtl: true
    });
    $('.product-details-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.product-details-for',
        dots: false,
        arrows: false,
        focusOnSelect: true,
        speed: 1200,
        margin: 30,
        rtl: true,
        responsive: [
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            }
        ]
    });

    // Popup gallery
    $('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
        }
    });

    // Product-size
    $(".product-size-list li").on("click", function () {
        $(this).addClass("active").siblings().removeClass("active");
    })

    // Product +/- button
    $(".qu-btn").on("click", function (e) {
        var btn = $(this),
        inp = btn.siblings(".qu-input").val();
        if (btn.hasClass("inc")) {
            var i = parseFloat(inp) + 1;
        }
        else {
            if (inp > 1) (i = parseFloat(inp) - 1) < 2 && $(".dec").addClass("deact");
            else i = 1;
        }
        btn.addClass("deact").siblings("input").val(i)
    })

    // // Product details tab
    // $(".product-details-tab-list li").on("click", function () {
    //     var tab = $(this).attr('data-product-tab-list');
    //     $(this).addClass("active").siblings().removeClass("active");
    //     $(".product-tab-information-item[data-product-details-tab=" + tab + "]").addClass("active").siblings().removeClass("active");
    // })
    // var tab = $('.product-details-tab-list li').attr('data-product-tab-list');
    $(this).addClass("active").siblings().removeClass("active");
    // tab = 2
    $(".product-tab-information-item[data-product-details-tab=" + 2 + "]").addClass("active").siblings().removeClass("active");

    // ProductCart
    $(".productCart").on("click", function (e) {
        e.preventDefault();
        $(".cart-modal-wrapper").addClass("active");
        $(".cart-modal").addClass("active");
    })
    $(".cart-modal-close").on('click', function () {
        $(".cart-modal-wrapper").removeClass("active");
        $(".cart-modal").removeClass("active");
        $(".wish-modal").removeClass("active");
    })

    // Product details tab
    $(".authentication-tab-item").on("click", function () {
        var tab = $(this).attr('data-authentication-tab');
        $(this).addClass("active").siblings().removeClass("active");
        $(".authentication-details-item[data-authentication-details=" + tab + "]").addClass("active").siblings().removeClass("active");
    })
    $(".authentication-box").on("click", function (e) {
        e.stopPropagation();
    })
    $(".authentication-close").on("click", function () {
        $(this).parent(".dropdown-menu").removeClass("show");
    })
    $(".navbar-option-dots .dropdown-menu").on("click", function (e) {
        e.stopPropagation();
    })

    // Wow
    new WOW().init();

    // Blog-carousel
    $('.blog-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dots: true,
        dotsEach: 2,
        items: 3,
        autoplay: false,
        autoplayHoverPause: true,
        autoplayTimeout: 3000,
        smartSpeed: 1500,
        rtl: true,
        navText: ["<i class='flaticon-left-arrow-2'></i>", "<i class='flaticon-right-arrow-3'></i>"],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    })

    // Show blog
    $(".blog-grid-item").slice(0, 6).show();
    $(".load-more-btn").on("click", function (e) {
        e.preventDefault();
        $(this).closest(".blog-section").find(".blog-grid-item:hidden").slice(0, 3).slideDown();
    })
    $(".blog-list-item").slice(0, 3).show();
    $(".load-more-btn").on("click", function (e) {
        e.preventDefault();
        $(this).closest(".blog-section").find(".blog-list-item:hidden").slice(0, 3).slideDown();
    })

    // Show receipe
    $(".receipe-grid").each(function () {
        $(this).children(".receipe-grid-item").slice(0, 9).show();
        $(".load-more-btn").on("click", function (e) {
            e.preventDefault();
            $(this).closest(".menu-main-details-item").find(".receipe-grid-item:hidden").slice(0, 3).slideDown();
        })
    })

    // Subscribe form
    $("#contactForm, .newsletter-form").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formErrorSub();
            submitMSGSub(false, "Please enter ایمیل correctly.");
        } else {
            // everything looks good!
            event.preventDefault();
        }
    });
    function callbackFunction(resp) {
        if (resp.result === "success") {
            formSuccessSub();
        } else {
            formErrorSub();
        }
    }
    function formSuccessSub() {
        $(".newsletter-form")[0].reset();
        submitMSGSub(true, "Thank you for subscribing!");
        setTimeout(function () {
            $("#validator-newsletter").addClass('hide');
        }, 4000)
    }
    function formErrorSub() {
        $(".newsletter-form").addClass("animate__animated animate__shakeX");
        setTimeout(function () {
            $(".newsletter-form").removeClass("animate__animated animate__shakeX");
        }, 1000)
    }
    function submitMSGSub(valid, msg) {
        if (valid) {
            var msgClasses = "validation-success";
        } else {
            var msgClasses = "validation-danger";
        }
        $("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
    }
    // Ajax mailchimp
    $(".newsletter-form").ajaxChimp({
        url: "https://hibootstrap.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
        callback: callbackFunction
    });
});