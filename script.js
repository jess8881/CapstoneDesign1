document.getElementById("copy").onclick = function(event) {
    const result = document.getElementById("output_text");
    result.select();
    document.execCommand('copy');
};

/* 예시 문장 번호 붙이기 */

document.addEventListener('DOMContentLoaded', function() {
  var recommendationsList = document.getElementById('list');
  var listItems = recommendationsList.getElementsByTagName('li');

  for (var i = 0; i < listItems.length; i++) {
    var listItem = listItems[i];
    listItem.innerText = (i + 1) + '. ' + listItem.innerText;
  }
});

