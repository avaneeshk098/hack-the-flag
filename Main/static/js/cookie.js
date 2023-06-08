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


function submit(e){
const csrftoken = getCookie('csrftoken');
e.preventDefault();
const val = document.getElementById('code').value;
const props = {
method: "POST", credentials: "include",
headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken

},
body: JSON.stringify({code: val})
}
console.log(val);
fetch("/verynoice",props).then(response=>response.json()).then(data=>{
console.log(data);
if(data.success)
{
    let context = JSON.stringify({'time_completed': Date.now().toString()})
            fetch("/pointer", {method: "POST", mode: "same-origin", headers:{'X-CSRFToken': csrftoken}, body:context})
            .then(response => {
                window.location.href = "dashboard/" 
            })
            .catch(e => console.error(e))
            // Logic for Correct Code
}
else{
    alert("Wrong Code!")
}
});
}
// document.getElementById('form').addEventListener("submit", submit);