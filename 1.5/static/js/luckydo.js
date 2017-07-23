/**
 * Created by Anonymous on 2017/7/23.
 */
var istrue = false;

var getuser =  (function(){
    //返回当前 URL 的查询部分（问号 ? 之后的部分）。
    var urlParameters = location.search;
    //声明并初始化接收请求参数的对象
    var requestParameters = new Object();
    //如果该求青中有请求的参数，则获取请求的参数，否则打印提示此请求没有请求的参数
    if (urlParameters.indexOf('?') != -1)
    {
        //获取请求参数的字符串
        var parameters = decodeURI(urlParameters.substr(1));
        //将请求的参数以&分割中字符串数组
        parameterArray = parameters.split('&');
        //循环遍历，将请求的参数封装到请求参数的对象之中
        for (var i = 0; i < parameterArray.length; i++) {
            requestParameters[parameterArray[i].split('=')[0]] = (parameterArray[i].split('=')[1]);
        }
        // console.info('theRequest is =====',requestParameters);
    }
    else
    {
        // console.info('There is no request parameters');
    }
    var user = requestParameters.user;
    return user;
})();

var getdata = function () {
    // 刷新页面每次获取用户最新抽奖次数
    if (getuser){
    $.getJSON("/luckynumber",{user:getuser},function (data,textStatus,jqXHR) {
        $('.playnumber').html(data);
    });}
}

getdata();

//点击旋转按钮开始抽奖，并请求数据
var $btn = $('.playbtn');
$btn.click(function () {
    if (istrue) return;
    istrue = true;
    if (getuser) {
        $.getJSON("/lucky", {user: getuser}, function (data, textStatus, jqXHR) {
            if (data.playnum == 0) {
                istrue = false;
                alert(data.idname);
            } else {
                getdata();
                rotateFunc(data.angles, data.idname, data.playnum);
            }
        });
    }else {
        istrue = false;
        alert("请输入用户名开始抽奖！");
    }
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
               trs += "<div>" + "恭喜用户：" + value.user+ "，" + value.idname.substring(3,) + "</div>";
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
roll.stoptime = 1000; //停留时间
roll();  //执行
