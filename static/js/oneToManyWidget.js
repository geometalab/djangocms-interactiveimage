function showIdPopup(_this) {
    var select = document.getElementById("id_temp_points");
    var pointId = select.options[select.selectedIndex].value;
    var originalHref = _this.href;
    var originalId = _this.id;
    _this.href = _this.href.replace('%7Bid%7D', pointId);
    _this.href = _this.href + '&_point_id=' + pointId;
    _this.id = _this.id.replace(/^change_/, '');
    _this.id = _this.id.replace(/^delete_/, '');

    showAddAnotherPopup(_this);

    _this.href = originalHref;
    _this.id = originalId;
    return false;
}

function dismissPopup(win, id, value, action) {
    id = html_unescape(id);
    value = html_unescape(value);
    action = html_unescape(action);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if ('add' == action) {
        var option = new Option(value, id);
        elem.options[elem.options.length] = option;
        option.selected = true;
    } else if ('change' == action) {
        for(var i = 0; i < elem.options.length; i++) {
            if (elem.options[i].value == id) {
                elem.options[i].text = value;
            }
        }
    } else if ('delete' == action) {
        var indexToDelete = -1;
        for(var i = 0; i < elem.options.length; i++) {
            if (elem.options[i].value == id) {
                indexToDelete = i;
            }
        }
        if (indexToDelete >= 0) {
            elem.options[indexToDelete].parentNode.removeChild(elem.options[indexToDelete]);
        }
    }
    elem.onchange();
    win.close();
}

function toggleEditLinks() {
    var select = document.getElementById("id_temp_points");
    if (select) {
        if (select.selectedIndex >= 0) {
            document.getElementById('change_id_temp_points').style.display = 'inline';
            document.getElementById('delete_id_temp_points').style.display = 'inline';
        } else {
            document.getElementById('change_id_temp_points').style.display = 'none';
            document.getElementById('delete_id_temp_points').style.display = 'none';
        }
    }
}