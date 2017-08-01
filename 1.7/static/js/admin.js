/**
 * Created by Benjamin on 2017/7/31.
 */

var istrue = true

//用户纪录列表展示
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
                        trs += "<div class='log'>"+ num +'&#8195;'+value.time+'&#8195;'+key+'&#8195;'+value[key]+'&#8195;'+"<a style='color:green;text-decoration:none;' href='javascript:;' class='edit' onclick='GetHref(this);' id='"+key+"'>编辑</a> | <a style='color: #ff0000;text-decoration:none;' href="+"'/deluser?user="+key+"'>删除</a>"+"</div>"
                        $('#user').attr('value',key);
                        istrue = false;
                    }
                }
               var tbody = "";
               tbody += trs;
               $(".userlist").append(tbody);
               istrue = true
    });
});

function GetHref(obj){
    var value=(obj.id);
    $('.formdata').fadeIn();
    $('#user').attr('value',value)
}

$('.formdata  b i').click(function () {
    $(".formdata").fadeOut();
});
