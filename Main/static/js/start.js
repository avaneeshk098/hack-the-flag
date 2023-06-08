function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.querySelector('#key-form').addEventListener('submit', (e) => {
e.preventDefault();
const csrftoken = getCookie('csrftoken');
let flag_val = document.querySelector("#key").value
console.log(flag_val)
let data = JSON.stringify({'flag': flag_val})
console.log(data)

const url = window.location.href;
const last = url.split("/")
const z_url = last[last.length-2];

let response = fetch("/" + z_url + "/", {method: "POST", mode: "same-origin", headers:{'X-CSRFToken': csrftoken}, body:data})
response.then((data) => {
    data.json().then(json_data => {
            if(json_data["works"])
            {
                window.location.href = "/dashboard"

                 // Logic for correct code
            }
            else if(json_data["already submitted"])
            {
                alert("you have already been awarded points for this challenge!") // Logic for Wrong Code
            }

            else
            {
                alert("Wrong Code") // Logic for Wrong Code
            }
    })
 })
})