/**
 * Created by Benjamin on 2017/7/31.
 */

var istrue = true



//用户纪录列表展示
$(".userlist").append("序号&#8195;&#8195;最后更新时间&#8195;&#8195;用户名&#8195;次数&#8195;&#8195;用户操作&#8195;&#8195;");
var userlist = function () {
    $.getJSON("/alluserdata",function (data,textStatus,jqXHR) {
    $("div").remove('.log');
    $.each(data, function (n, value) {
                var trs = "";
                for (var key in value)
                {
                    // alert(key);
                    // alert(value[key]);
                    if (istrue){
                        var num = n+1
                        trs += "<div class='log'>"+ num +'&#8195;'+value.time+'&#8195;'+key+'&#8195;'+value[key]+'&#8195;'+"<a style='color:#2b542c;text-decoration:none;' href='javascript:;' onclick='GetCheck(this);' id='"+key+"'>查看</a> |<a style='color:green;text-decoration:none;' href='javascript:;' class='edit' onclick='Getid(this);' id='"+key+"'>编辑</a> | <a style='color: #ff0000;text-decoration:none;' href="+"'/deluser?user="+key+"'>删除</a>"+"</div>"
                        istrue = false;
                    }
                }
               var tbody = "";
               tbody += trs;
               $(".userlist").append(tbody);
               istrue = true
        });
    });
}

userlist();

function Getid(obj){
    var value=(obj.id);
    $('.formdata').fadeIn();
    $('#user').attr('value',value)
    $(".userdata").fadeOut();
}

$('.formdata  b i').click(function () {
    $(".formdata").fadeOut();
});

function GetCheck(obj) {
    var value=(obj.id);
    $('.username').html(value);
    $('.userdata').fadeIn();
    $(".formdata").fadeOut();
    $.getJSON("/mylucky",{user:value},function (data,textStatus,jqXHR) {
    $("div").remove('.userlog');
    $.each(data, function (n, value) {
               var trs = "";
               trs += "<div class='userlog'>" +value.time+'   '+value.idname+ "</div>";
               var tbody = "";
               tbody += trs;
               $(".datalist").append(tbody);
           });
    });
}

$('.userdata  b i').click(function () {
    $(".userdata").fadeOut();
    userlist();
});
