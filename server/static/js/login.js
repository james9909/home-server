$("#login-form").on("submit", function(e) {
    e.preventDefault();
    var email = $("#email").val();
    var password = $("#password").val();
    login(email, password);
})

function login(email, password) {
    $("#login").prop("disabled", "disabled");
    $.post("/api/users/login", {
        email: email,
        password: password
    }, function(data) {
        if (data["success"] == 1) {
            display_message("login-status", "success", data["message"], function() {
                $("#login").removeAttr("disabled");
            });
        } else {
            display_message("login-status", "danger", data["message"], function() {
                $("#login").removeAttr("disabled");
            });
        }
    });
}
