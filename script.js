
document.getElementById("copy").onclick = function(){
    const result = document.getElementById("output_text");
    result.select();
    document.execCommand('copy');
};