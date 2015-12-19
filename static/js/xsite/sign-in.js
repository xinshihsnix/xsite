/**
 * Created by xinshi on 15-12-19.
 */
function sign_in(){
    username = $('#username').val()
    password = $('#raw_password').val()

    $.post('/account/sign_in/', {'username': username, 'password': password}, function(data){
        //alert(data)
        //alert(data.is_success)
        if(data.is_success == true){
            $('#content_div').html('登录成功!')
        }else{
            $('#content_div').html('登录失败!')
        }
    })
}