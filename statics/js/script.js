<<<<<<< HEAD
/**
 * Created by westos on 17/1/16.
 */

=======
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                alert(data);
            },
            error:function(){
                alert("error!");
            },
        });
    });
<<<<<<< HEAD
});
=======
});
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
