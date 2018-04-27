
//Show detailed description
$(window).load(function() {
  $('.post-module').hover(function() {
    $(this).find('.description').stop().animate({
      height: "toggle",
      opacity: "toggle"
    }, 100);
  });
});


// When the user scrolls down 70px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 70 || document.documentElement.scrollTop > 70) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

/*Carousel*/
// Instantiate the Bootstrap carousel
$('.multi-item-carousel').carousel({
  interval: false
});

// for every slide in carousel, copy the next slide's item in the slide.
// Do the same for the next, next item.
$('.multi-item-carousel .item').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));

  if (next.next().length>0) {
    next.next().children(':first-child').clone().appendTo($(this));
  } else {
  	$(this).siblings(':first').children(':first-child').clone().appendTo($(this));
  }
});

/** Save button **/
$(document).ready(function(){
  function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb)
  }

  $(".save-btn").click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var saveUrl = this_.attr("data-href")
    var saveCount = parseInt(this_.attr("data-saves")) | 0
    var addSave = saveCount + 1
    var removeSave = saveCount
    var str = ""
    if(saveUrl) {
      $.ajax({
        url: saveUrl,
        method: "GET",
        data: {},
        success: function(data){
          if (data.saved) {
            $(".save-btn").text('Save/ Unsave');
            location.reload();
            
          } else {
            $(".save-btn").text('Save/ Unsave');
            location.reload();
          }
        },
        error: function(error){
          console.log(error)
          console.log("error")
        }
      })
    }


  })
})



