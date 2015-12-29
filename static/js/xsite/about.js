/**
 * Created by xinshi on 15-12-19.
 */
function click_terminal(){
    $.get("/about/terminal/",
        {},
        function(data,status){
             $("#content_div").html(data);
        });
}

function enter_terminal_cmd(event){
    if(event.keyCode == 13){
        cmd = $('#cmd').val();
        $.post('/about/terminal/', {'cmd': cmd}, function (data) {
            data = '>  ' + cmd + '\n\n' + data
            $('#terminal').val(data);
            $("input[id='cmd']").val("").focus();
        })
    }
}

function click_leavemessage(){
    $.get("/about/leavemessage/",
        {},
        function(data,status){
             $("#content_div").html(data);
        });
}

function submit_leavemessage(){
    message_content = $('#message_content').val();
    $.post('/about/leavemessage/', {'message_content': message_content}, function (data) {
        alert(data)
        if(data == 'ok'){
            click_leavemessage();
        }
    })
}