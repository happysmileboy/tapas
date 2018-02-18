
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

$(document).ready(function(){
  function autocomplete(inp, arr) {
  var currentFocus;
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });

  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }

  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
      });
    }

/*An array containing all the country names in the world:*/
var tags = ["a김슬기", "a진선규","p대학로", "p강남", "p신림","p신도림","p사당","p마포"];

/*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
autocomplete(document.getElementById("myInput"), tags);
})


function tagaddfunction(){
  var tag_box, a, tagadd;
    tag_box = document.getElementById("tag_box")
    tagadd = document.getElementById("myInput").value
    a = document.createElement("DIV")
    tag_box.appendChild(a)
    a.setAttribute("onclick", "tagremovefunction(\""+tagadd+"\")");
    a.setAttribute("class", "tag_value");
    a.setAttribute("id", tagadd);
    a.innerHTML = tagadd
    document.getElementById("myInput").value = ""
}

function tagremovefunction(id){
  var parent = document.getElementById("tag_box")
  var child = document.getElementById(id)
  parent.removeChild(child)

}