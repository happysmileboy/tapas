$(document).ready(function(){
    $(".drama_card").click(function(){
      $('.gsc-results-wrapper-overlay').css({"opacity": "1", "visibility":"visible"});
      $('.gsc-results-close-btn').css({"opacity": "1", "display":"block"});
      $(".gsc-modal-background-image").addClass("gsc-modal-background-image-visible");

   });
});

$(document).ready(function(){
    $(".gsc-results-close-btn").click(function(){
         $('.gsc-results-close-btn').css({"opacity": "0", "display":"none"});
         $('.gsc-results-wrapper-overlay').css({"opacity": "0", "visibility":"hidden"});
         $(".gsc-modal-background-image").removeClass("gsc-modal-background-image-visible");
   });
});

$(document).ready(function(){
    $(".gsc-modal-background-image").click(function(){
         $('.gsc-results-close-btn').css({"opacity": "0", "display":"none"});
         $('.gsc-results-wrapper-overlay').css({"opacity": "0", "visibility":"hidden"});
         $(".gsc-modal-background-image").removeClass("gsc-modal-background-image-visible");
   });
});

$(document).ready(function(){
   $('.drama_card a').click(function(event){
      event.preventDefault();

   });
});

function myfunction(url){
         $('.detail').load(url);
      }