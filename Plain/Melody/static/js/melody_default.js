
$("#subupload-btn").on('click', function() {
    document.all.commendInput.click();
});
var check = 0;
$("#playbutton").on('click', function() {
    wavesurfer.playPause();
    if (check == 0){
        check = 1;
        document.getElementById("playbutton").classList.replace("fa-play-circle", "fa-pause-circle");
    }
    else {
        check = 0;
        document.getElementById("playbutton").classList.replace("fa-pause-circle", "fa-play-circle");
    }
});

var comment_waveforms = []

const checking_button=document.querySelector("#checkedbutton");

function findout_checked()
{
    //console.log("hello")

    var obj_length = document.getElementsByName("checked").length;
  
        for (var i=0; i<obj_length; i++) {
            if (document.getElementsByName("checked")[i].checked == true) {
                console.log(document.getElementsByName("checked")[i].value)
   
            }
        }

    
}

checking_button.addEventListener("click",findout_checked);