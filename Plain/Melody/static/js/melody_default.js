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


comment_plays = document.getElementsByClassName("cm-play");

function change_play(event) {
    button = this.getElementsByClassName("button")[0];
    if (button.classList.contains("fa-play-circle")) {
        button.classList.replace("fa-play-circle", "fa-pause-circle");
    }
    else {
        button.classList.replace("fa-pause-circle", "fa-play-circle");
    }
}

for (i = 0; i < comment_plays.length; i++) {
    comment_plays[i].addEventListener("click" , change_play);
}