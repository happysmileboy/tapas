
// 왼쪽 상단 menu bar//
  $(document).ready(function(){
      $("#nav_mobile_menu").click(function(){
        $(".nav_mobile_menu_content").addClass("nav_mobile_menu_content_expend");
        $(".menu_wrap").addClass("dropdown_content_display");
        $(".menu").animate({left: '0',right:'56px'});
      });
  });

  $(document).ready(function(){
    $(".nav_mobile_menu_content").click(function(){
      $(".nav_mobile_menu_content").removeClass("nav_mobile_menu_content_expend");
      $(".menu_wrap").removeClass("dropdown_content_display")
      $(".menu").animate({left: '-1000',right:'1000'});
    });
  });

  $(document).ready(function(){
      $(".nav_profile_photo").click(function(){
        $(".dropdown_content").toggleClass("dropdown_content_display")
      });
  });

//우측 상단 search기능
$(document).ready(function(){
  $(".search_box").click(function(){
    $(".search_bar").addClass("display_block")
    $(".recommend_list").addClass("display_block")
  })
})
$(document).ready(function(){
  $(".search_close_btn").click(function(){
    $(".search_bar").removeClass("display_block")
    $(".recommend_list").removeClass("display_block")
  })
})