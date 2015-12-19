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