/**
 * Created by xinshi on 16-1-2.
 */
function fresh_content_when_click(url){
        $.get(url,
            {},
            function(data,status){
                 // alert(data);
                 $("#content_div").html(data);
            });
}