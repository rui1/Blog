$(document).ready(function(){
  $('#login-trigger').click(function(){
    $(this).next('#login-content').slideToggle();
    $(this).toggleClass('active');          
    
    if ($(this).hasClass('active'))
    {$(this).find('span').html('&#x25B2;');}
      else $(this).find('span').html('&#x25BC;')
    })
});
$(document).ready(function() {
  $('.toggle_comment').click(function() {
    $(".comment-box").toggle();        
    $(this).toggleClass('active'); 
    if ($(this).hasClass('active'))
    {$(this).find('span').html('&#x25B2;');}
      else $(this).find('span').html('&#x25BC;')
    })
});

$(document).ready(function() {
  $('.toggle_codes').click(function() {
      $("#" + $(this).attr("id") + ".codes").toggle();
      if($(this).html().search("Hide") > 0) {
        $(this).html($(this).html().replace("Hide", "Reveal"));
      } else {
        $(this).html($(this).html().replace("Reveal", "Hide"));
      }
  });
});
