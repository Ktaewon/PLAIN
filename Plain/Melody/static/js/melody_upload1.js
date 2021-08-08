function imgSize(which){
    img = document.getElementById(which)
    var width = img.width;
    var height = img.height;
    var max_width= 300;   // 이미지의 가로 최대 크기    
    var max_height = 300; // 이미지의 세로 최대 크기
    img.width = 300;
    img.height = 300;
    /*
    if ( width > max_width ) {  // 이미지가 300보다 크다면 너비를 300으로 맞우고 비율에 맞춰 세로값을 변경한다. 
        height = height/(width / max_width);
        img.width = max_width;
        img.height = height;
        //eval("document."+which+".width = max_width");     
        //eval("document."+which+".height = height");
        width = max_width;     
    }

    if( height > max_height ) {
        width = width/(height / max_height);
        eval(img.width = width);
        eval(img.height = max_height);
    }*/
}


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('#image_section').attr('src', e.target.result);
            //var width = document.getElementById('image_section').width;
            //var height = document.getElementById('image_section').height;
            //alert("width : " + width);
            //alert("height : " + height);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function readAudio(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('#audio_section').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
    
   // 이벤트를 바인딩해서 input에 파일이 올라올때 위의 함수를 this context로 실행합니다.

$(function() {
    $("#imgInput").on('change', function(){
        readURL(this);
        //imgSize("image_section");
    });
});
$(document).ready(function() {
    $("#image_section").load(function() {
        imgSize("image_section");
    });
});

$("#image_section").on('click', function() {
    document.all.imgInput.click();
})
$(function() {
    $("#melodyInput").on('change', function(){
        readAudio(this);
    });
});