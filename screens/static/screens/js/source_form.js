/* global django */
django.jQuery(function($) {
  function frm_selected(){
    console.log("frm");
    $("#id_file").prop('disabled', true);
    $("#id_url").prop('disabled', false);
    $("#id_ytid").prop('disabled', true);
  }

  function ytv_selected(){
    console.log("ytv");
    $("#id_file").prop('disabled', true);
    $("#id_url").prop('disabled', true);
    $("#id_ytid").prop('disabled', false);
  }

  function img_vid_selected(){
    console.log("img_vid");
    $("#id_file").prop('disabled', false);
    $("#id_url").prop('disabled', true);
    $("#id_ytid").prop('disabled', true);
  }

  $("#id_type").change(function(event) {
    if (event.target.value == "FRM"){
      frm_selected()
    } 
    else if (event.target.value == "YTV"){
      ytv_selected()
    }
    else {
      img_vid_selected()
    }
  });
});
