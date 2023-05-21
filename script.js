document.getElementById("copy").onclick = function(){
    const result = document.getElementById("result");
    result.select();
    document.execCommand('copy');
};