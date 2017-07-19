/**
 * Created by Anonymous on 2017/7/17.
 */
var istrue = false;
$.getJSON("/luckynumber",function (data,textStatus,jqXHR) {
    $('.playnumber').html(data.luckynnumber);
});

var $btn = $('.playbtn');
$btn.click(function () {
    if (istrue) return;
    istrue = true;
    $.getJSON("/lucky",function (data,textStatus,jqXHR) {
        if (data.playnum>=0){
            rotateFunc(data.angles,data.name,data.playnum);
         }else {
            alert(data.name);
            istrue = false;
        }
    });
});

var rotateFunc = function (angles,text,playnum) {
        $('.playnumber').html(playnum);
        $btn.stopRotate();
        $btn.rotate({
            angle:0,
            duration:3000,
            animateTo:angles + 1440,
            callback:function () {
                istrue = false;
                alert(text);
            }
        });
    }

