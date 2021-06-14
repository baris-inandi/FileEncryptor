/*
 * FileEncrytor
 * @baris-inandi, 2021
 * licensed under the MPL-2.0 license. 
 */

// important constants
const appName = "FileEncryptor";
const version = "v1.0.0-beta";
const repo = "https://www.github.com/baris-inandi/fileencryptor";
const dev = "@baris-inandi"
const lastUpdateYear = "2021"

function updateAvailable() {
    return true
}

function goToURL(url) {
    var win = window.open(url, "_blank");
    if (win) {
        win.focus();
    } else {
        alert("Please allow popups");
    }
}

// fill in the html contents
function fillAppInfo() {
    $(".logo").html(appName);
    $("#gh-alert-title-1").html(dev + "'s " + appName);
    $("#version").html(`${appName} ${version}`);
    $("#last-update-info").html(dev + ", " + lastUpdateYear);
    if (window.navigator.onLine) {
        if (updateAvailable()) {
            $(".warn-area").html("Updates Available. Click here to download the latest version").addClass("pointer");
            $(".warn-area").click(function () {
                goToURL(repo + "/releases/latest")
            });
        } else {
            $(".warn-area").html(`You are using the latest version of ${appName}!`).removeClass("warning-color").addClass("success-color");

            setTimeout(function () {
                $(".warn-area").remove()
            }, 3000);

        }
    } else {
        $(".warn-area").html("No internet connection");
    }
}

// initialize window properties
$(document).ready(function () {
    window.resizeTo(500, 500);
    window.focus();
    fillAppInfo()
    $("#app").css({
        "opacity": "1",
        "transform": "unset"
    });
    $("footer").css({
        "opacity": "1"
    });
    $("body").css({
        "overflow": "unset"
    });
    document.body.style.zoom = "100%";
});

// make the esc key remove popups
$(document).on("keydown", function (event) {
    if (event.key == "Escape") {
        removePopups();
    }
});

function enc() {
    // call python function to open a file dialog and get the filepath here
    function passMatch() {
        var pass = $("#enc-pass-input").val();
        var passConfirmation = $("#enc-pass-input-confirmation").val();
        if (pass == passConfirmation && /\S/.test(pass)) {
            // passwords match
            $("#enc-pass-btn").prop("disabled", false).removeClass("disabled").html("Encrypt!");
        } else {
            // passwords do not match
            $("#enc-pass-btn").prop("disabled", true).addClass("disabled").html("Enter matching passwords to proceed.");
        }
    }
    showPopup("enc-pass")
    window.passIntervalEnc = setInterval(passMatch, 50);
}

function dec() {
    // call python function to open a file dialog and get the filepath here
    // TODO: check if dec password is empty and prompt user to select one.
    function isPassEmpty() {
        var passdec = $("#dec-pass-input").val();
        if (/\S/.test(passdec)) {
            // password valid and not just whitespace
            $("#dec-pass-btn").prop("disabled", false).removeClass("disabled").html("Decrypt!");
        } else {
            // passwords just whitespace
            $("#dec-pass-btn").prop("disabled", true).addClass("disabled").html("Enter a password to proceed.");
        }
    }
    showPopup("dec-pass")
    window.passIntervalDec = setInterval(isPassEmpty, 50);
}

function removePopups() {
    // stop intervals when removing popups
    clearInterval(window.passIntervalEnc);
    clearInterval(window.passIntervalDec);
    // clear all input fields on popups
    $(".password-field").val("");
    // hide all pop-ups and the overlay
    $("#overlay").prop("hidden", true);
    $(".popup").prop("hidden", true);
}

function showPopup(id) {
    // remove all pre-existing popups since they might overlap
    removePopups();
    // remove hidden attribute from the popup with the specified id
    $("#overlay").prop("hidden", false);
    $("#" + id).prop("hidden", false);
}