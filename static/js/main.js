function turnPage(url){
    $.ajax({
      type:"post",
      url:url,
      success:function(html){
        $("#content").html(html);
      }
    })
  }

   GRANT ALL ON *.* TO root@'%' IDENTIFIED BY 'xinshi' WITH GRANT OPTION;