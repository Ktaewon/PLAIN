$("#subupload-btn").on('click', function() {
    document.all.commendInput.click();
});
var check = 0;
$("#playbutton").on('click', function() {
    wavesurfer.playPause();
    if (check == 0) {
        check = 1;
        document.getElementById("playbutton").classList.replace("fa-play-circle", "fa-pause-circle");
    } else {
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
function findout_checked() {
    //console.log("hello")

    var obj_length = document.getElementsByName("checked").length;
    let checked_list = []

    for (var i = 0; i < obj_length; i++) {
        if (document.getElementsByName("checked")[i].checked == true) {
            console.log("안녕", document.getElementsByName("checked")[i].value)
            checked_list.push(document.getElementsByName("checked")[i].value)

        }
    }
    console.log(checked_list)

    //Play button 들 다 가져오기
    let elementList = document.querySelectorAll(".cm_play");
    console.dir(elementList)
    console.dir(elementList[0].attributes[3].nodeValue) //이걸로 가져올 수 있음 ㅠㅠ

    for (var i = 0; i < elementList.length; i++) {
        for (var j = 0; j < checked_list.length; j++) {
            if (elementList[i].attributes[3].value == parseInt(checked_list[j])) {
                console.log("이걸 클릭해!!")
                elementList[i].click();
                if (i == (elementList.length - 1) || checked_list.length == 1) //순서가 마지막이면
                {
                    $("#playbutton").click()
                }
            }
        }

    }



}

const checking_button = document.querySelector("#checkedbutton");
checking_button.addEventListener("click", findout_checked);

