var colorSelector = document.getElementById('id_color');
var textarea = document.getElementById('id_content');

colorSelector.addEventListener('change', function() {
    changeColor();
});

function changeColor() {
    var selectedColor = colorSelector.value;
    switch (selectedColor) {
        case '1':
            textarea.style.backgroundColor = '#FDFD96';
            break;
        case '2':
            textarea.style.backgroundColor = '#BDECB6';
            break;
        case '3':
            textarea.style.backgroundColor = '#FF6961';
            break;
        case '4':
            textarea.style.backgroundColor = '#F7BD56';
            break;
        case '5':
            textarea.style.backgroundColor = '#ABC4FF';
            break;
        case '6':
            textarea.style.backgroundColor = '#ECC9DD';
            break;
        default:
            textarea.style.backgroundColor = '#FDFD96';
            break;
    }
  }