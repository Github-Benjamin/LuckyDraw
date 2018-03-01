/**
 * Created by Anonymous on 2017/7/17.
 */
var istrue = false;

var playnumber = 3;
$('.playnumber').html(playnumber);

var $btn = $('.playbtn');
$btn.click(function () {
    $.getJSON("/lucky",function (data,textStatus,jqXHR) {
        rotateFunc(data.angles,data.name);
});
    // rotateFunc(60,'谢谢参与！');
});


    var rotateFunc = function (angles,text) {
        if (istrue) return;
        istrue = true;
        if (playnumber>0){
            playnumber = playnumber -1;
            $('.playnumber').html(playnumber);
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
        }else {
            istrue = false;
            alert('抽奖次数不足！');
        }
        }
