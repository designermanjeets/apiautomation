"use strict";

// Class definition
var KTMSAUTO = function () {

    // automationAiSubmit
    var initAutomationAiSubmit = function() {
        var automationAiSubmit = document.querySelector('#automationAiSubmit');
        if (automationAiSubmit) {
            automationAiSubmit.addEventListener('click', function() {
                 console.log('automationAiSubmit');
                 var that = this;
                 var progressHandling = function (event) {
                    console.log(event);
                    var percent = 0;
                    var position = event.loaded || event.position;
                    var total = event.total;
                };

                var formData = new FormData();
                // add assoc key values, this will be posts values
                formData.append("file", new File([""], "filename.txt", {type: "text/plain", lastModified: new Date(Date.now())}), 'myFile');
                formData.append("upload_file", true);
                $.ajax({
                    type:"POST",
                    url: "https://ihrms-api.azurewebsites.net",
//                    data: { "operationName":"login","variables":{"username":"amit_k","email":"amit_k","password":"11"},"query":"mutation login($username: String, $email: String!, $password: String!) {\n  login(username: $username, email: $email, password: $password) {\n    user {\n      username\n      _id\n      tenantid\n      eCode\n    }\n    role {\n      _id\n      role_name\n    }\n    tenants {\n      _id\n      name\n      printName\n    }\n    token\n    refresh_token\n    tokenExpiration\n    designation {\n      name\n    }\n  }\n}"},
//                    success: function( data ) {
//                        console.log(data)
//                    }

                    xhr: function () {
                        var myXhr = $.ajaxSettings.xhr();
                        if (myXhr.upload) {
                            myXhr.upload.addEventListener('progress', that.progressHandling, false);
                        }
                        return myXhr;
                    },
                    success: function (data) {
                        // your callback here
                        console.log(data);
                    },
                    error: function (error) {
                        console.log(error);
                        // handle error
                    },
                    async: true,
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false,
                    timeout: 60000
                 })//
            });
        }
    }

    // Public methods
    return {
        init: function () {
            initAutomationAiSubmit();
        }
    }
}();

// Webpack support
if (typeof module !== 'undefined' && typeof module.exports !== 'undefined') {
    module.exports = KTMSAUTO;
}

//// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTMSAUTO.init();
});
