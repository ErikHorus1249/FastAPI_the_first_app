
function sendJSON(){
               
    // fetching data   
    let result = document.querySelector('.result');
    let receiver_email = document.querySelector('#receiver-ml');
    let subject_email  = document.querySelector('#subject-ml');
    let content_email  = document.querySelector('#mail-ct');
       
    // Creating a XHR object
    let xhr = new XMLHttpRequest();
    let url = "https://demoapp-pyhton.herokuapp.com/send_mail?";

    // put data to URL 
    url = url + "receiver="+ receiver_email.value + "&content=" + content_email.value + "&subject=" + content_email.value

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

            // Print received data from server
            result.innerHTML = this.responseText;

        }
    };


    xhr.send();
}