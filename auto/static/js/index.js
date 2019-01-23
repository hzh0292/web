window.onload = function(){
    var timer = setInterval(function(){
        $("time").innerText -= 1;
        //判断
        if($("time").innerText === "0"){
            clearInterval(timer);
            $('time').style.display = 'none';
            $('cat').style.display = 'block';
            $('welcome').style.display = 'block';
        }
    },1000);
}
function $(id){
    return typeof id === "string"? document.getElementById(id):null
}