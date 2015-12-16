/**
 * Created by xinshi on 15-12-15.
 */
function validate_sign_up(){
    username = $('#username').val()
    password = $('#password').val()
    confirm_password = $('#confirm_password').val()
    email = $('#email').val()
    $('#info').html('')

    // 判断是否为空
    xd=username.replace(/\ +/g,"");//去掉空格
    xd=xd.replace(/[ ]/g,"");    //去掉空格
    xd=xd.replace(/[\r\n]/g,"");//去掉回车换行
    if (username == null || username == undefined || username == '' || xd.length == 0){
      $('#info').html('用户名不能为空')
      return false
    }
    var reg = /^\s*$/g;
    //  如果是空，或者""
    if(password=="" || reg.test(password) || confirm_password=="" || reg.test(confirm_password) || email=="" || reg.test(email)){
      $('#info').html('不能有空项')
      return false
    }
    if (password != confirm_password){
        $('#info').html('两次输入的密码不一样')
        return false
    }
    var myreg = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
    if(myreg.test(email)){
    }else{
      $('#info').html('邮箱格式不对')
      return false
    }
    return true
}

function is_username_exists(){
    username = $('#username').val()
    $.get("/account/is_username_exists/",
    {'username': username},
    function(data,status){
        $('#info').html('')
        if(data == 'no'){
            $('#info').html('用户名已存在')
        }
    });
}
