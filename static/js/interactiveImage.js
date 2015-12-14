$(window).on("load", function () {
    $('.interactive-image').each(function () {
        optimizePointsBasedOnImageSize($(this));
    });

    var $interactivePointContainer = $('.interactive-point-container');
    $interactivePointContainer.on('mouseover click', function () {
        displayDetails($(this));
    });

    $interactivePointContainer.on('mouseleave', function () {
        hideDetails($(this));
    });
});

function optimizePointsBasedOnImageSize($elem){
    if (!$elem.data('points-optimized')) {
        $elem.data('points-optimized', true);
        var $img = $('.imgContainer img', $elem);
        var conversionFactor = 1 / getConversionFactor($img);
        $('.interactive-point-container', $elem).each(function () {
            var top = parseIntFromPx($(this).css('top')) * conversionFactor;
            var left = parseIntFromPx($(this).css('left')) * conversionFactor;
            $(this).css('top', top + 'px');
            $(this).css('left', left + 'px');
            $(this).data('top', top + 'px');
            $(this).data('left', left + 'px');
            $('.interactive-point', $(this)).css('background-size', (100 * conversionFactor) + '%')
        });
    }
}

function displayDetails($elem) {
    var $details = $('.interactive-point-detail', $elem);
    var $point = $('.interactive-point', $elem);
    $details.show();

    var maxLeft = parseIntFromPx($elem.parent().css('width'));
    var maxTop = parseIntFromPx($elem.parent().css('height'));
    var currentLeft = parseIntFromPx($elem.css('left'));
    var currentTop = parseIntFromPx($elem.css('top'));
    var margin = parseIntFromPx($details.css('margin-left'));
    var width = parseIntFromPx($elem.css('width'));
    var height = parseIntFromPx($elem.css('height'));

    if (currentLeft + width > maxLeft) {
        $elem.css('left', (currentLeft - (width - 2 * margin)) + 'px');
        $point.css('left', 'auto');
        $point.css('right', 0);
        $details.css('margin-left', '0px');
        $details.css('margin-right', margin + 'px');
    }

    if (currentTop + height > maxTop) {
        $elem.css('top', (currentTop - (height - 2 * margin)) + 'px');
        $point.css('top', 'auto');
        $point.css('bottom', 0);
        $details.css('margin-top', '0px');
        $details.css('margin-bottom', margin + 'px');
    }

    $elem.css('z-index', '100');
}

function hideDetails($elem) {
    var $details = $('.interactive-point-detail', $elem);
    $details.hide();

    $elem.css('left', $elem.data('left'));
    $elem.css('top', $elem.data('top'));

    $details.css('margin', '20px 0px 0px 20px');
    $elem.css('z-index', '0');
}

function parseIntFromPx(pixelValue) {
    if (pixelValue) {
        var value = pixelValue.substr(0, pixelValue.length - 2);
        return parseInt(value);
    } else {
        return 0;
    }
}

function getConversionFactor($img) {
    return $img[0].naturalWidth / $img[0].width;
}