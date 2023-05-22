document.getElementById("copy").onclick = function(event) {
    const result = document.getElementById("output_text");
    result.select();
    document.execCommand('copy');
};
