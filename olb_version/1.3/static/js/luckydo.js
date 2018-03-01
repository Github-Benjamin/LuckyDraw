/**
 * Created by Anonymous on 2017/7/17.
 */
var istrue = false;

// 刷新页面每次获取用户最新抽奖次数
$.getJSON("/luckynumber",function (data,textStatus,jqXHR) {
    $('.playnumber').html(data.luckynnumber);
});

//用户输入数据获取提交数据username
var $username = $('.submit');
$username.click(function () {
    var username=document.getElementById("username").value;
    alert(username);
})

//点击旋转按钮开始抽奖，并请求数据
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

//抽奖轮盘动画效果
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
