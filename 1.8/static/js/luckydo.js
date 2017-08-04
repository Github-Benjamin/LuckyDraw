/**
 * Created by Anonymous on 2017/7/23.
 **/
var istrue = false;

var getdata = function () {
    // 刷新页面每次获取用户最新抽奖次数
    $.getJSON("/luckynumber",function (data,textStatus,jqXHR) {
            $('.playnumber').html(data);
    });
};

getdata();

//我的中奖记录
$('.mylucky').click(function () {
 $.getJSON("/mylucky",function (data,textStatus,jqXHR) {
    $("div").remove('.log');
    $.each(data, function (n, value) {
               var trs = "";
               trs += "<div class='log'>" +value.time+'   '+value.idname+ "</div>";
               var tbody = "";
               tbody += trs;
               $("#mylucky").append(tbody);
           });
    });
});

//点击旋转按钮开始抽奖，并请求数据
var $btn = $('.playbtn');
$btn.click(function () {
    if (istrue) return;
    istrue = true;
    $.getJSON("/lucky", function (data, textStatus, jqXHR) {
        if (data.playnum == 0) {
            istrue = false;
            alert(data.idname);
        } else {
            getdata();
            rotateFunc(data.angles, data.idname, data.playnum);
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

$.getJSON("/luckylog",function (data,textStatus,jqXHR) {
    $.each(data, function (n, value) {
               var trs = "";
               trs += "<div>" + "恭喜用户：" + value.user+ "，" + value.idname.substring(3) + "</div>";
               var tbody = "";
               tbody += trs;
               $("#container").append(tbody);
           });
});

//获取第一个子元素
function get_firstchild(obj)
{
      var child=obj.firstChild;
     while (child.nodeType!=1)
      {
          child=child.nextSibling;
      }
         return child;
}

 function roll()
 {
     var container=document.getElementById('container');
    var child = get_firstchild(container);

    if(child.style.marginTop=='')
     {
        child.style.marginTop='0px';
     }

 if(parseInt(child.style.marginTop)==-child.offsetHeight)
    {
      child.style.marginTop = "0px";
       container.appendChild(child);
      setTimeout("roll()",roll.stoptime)
  }
   else
   {
       if(parseInt(child.style.marginTop) - roll.step < -child.offsetHeight)
       {
           child.style.marginTop = - child.offsetHeight + "px";
       }     else
       {
             child.style.marginTop = parseInt(child.style.marginTop) - roll.step + "px";
           setTimeout("roll()",roll.timeout)
       }
    }
}

roll.timeout = 20;    //时长
roll.step = 1;        //步伐
roll.stoptime = 3000; //停留时间
roll();  //执行
