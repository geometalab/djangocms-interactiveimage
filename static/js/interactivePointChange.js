$(document).ready(function () {
    document.getElementById("interactive_image").src = getUrlParameter("image");
    document.getElementById("id_interactiveimage").value = getUrlParameter("_interactive_image_id");
    document.getElementById("id_interactiveimage").parentNode.style.display = 'none';
    if (document.getElementsByClassName('deletelink')[0]) {
        document.getElementsByClassName('deletelink')[0].style.display = 'none';
    }

    var $interactiveImage = $("#interactive_image");
    $interactiveImage.load(function () {
        var x = $('#id_xCoordinate').val();
        var y = $('#id_yCoordinate').val();
        if (x && y) {
            var conversionFactor = 1 / getConversionFactor($(this));
            displayPoint(x * conversionFactor, y * conversionFactor, $(this));
        }
    });

    $interactiveImage.click(function (e) {
        var offset = $(this).offset();
        var xCoordinate = (e.pageX - offset.left);
        var yCoordinate = (e.pageY - offset.top);
        setPoint(xCoordinate, yCoordinate, $(this));
        displayPoint(xCoordinate, yCoordinate, $(this));
    });
});

function getConversionFactor($img) {
    return $img[0].naturalWidth / $img[0].width;
}

function setPoint(xCoordinate, yCoordinate, $img) {
    if ($img) {
        var conversionFactor = getConversionFactor($img);
        $('#id_xCoordinate').val(parseInt(xCoordinate * conversionFactor));
        $('#id_yCoordinate').val(parseInt(yCoordinate * conversionFactor));
    }
}

function displayPoint(xCoordinate, yCoordinate, $img) {
    if ($img) {
        var conversionFactor = 1 / getConversionFactor($img);
        var $interactivePoint = $('.interactive-point');
        var width = parseInt($interactivePoint.css('width'), 10);
        var height = parseInt($interactivePoint.css('height'), 10);

        $interactivePoint.css('top', (yCoordinate - (width / 2)) + "px");
        $interactivePoint.css('left', (xCoordinate - (height / 2)) + "px");
        $interactivePoint.css('display', "block");
        $interactivePoint.css('background-size', (100 * conversionFactor) + '%')
    }
}

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1));
    var sURLVariables = sPageURL.split('&');
    var sParameterName;
    var i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};