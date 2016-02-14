function display_message(containerId, alertType, message, callback) {
    $("#" + containerId).html("<div class=\"alert alert-" + alertType + "\">" + message + "</div>");
    $("#" + containerId).hide().slideDown("fast", "swing", function() {
        window.setTimeout(function () {
            $("#" + containerId).slideUp("fast", "swing", callback);
        }, message.length * 50);
    });
};
