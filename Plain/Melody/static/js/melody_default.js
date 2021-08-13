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

$("#comment_play").on('click', function() {
    if (check == 0){
        check = 1;
        document.getElementById("comment_playbutton").classList.replace("fa-play-circle", "fa-pause-circle");
    }
    else {
        check = 0;
        document.getElementById("comment_playbutton").classList.replace("fa-pause-circle", "fa-play-circle");
    }
});
