const manzil = document.querySelector('#manzil');
const viloyat = document.querySelector('#viloyat');
const tuman = document.querySelector('#tuman');

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

manzil.addEventListener("change", pickState)

function pickState(e){   
    const val=e.target.value;
    const csrftoken = getCookie('csrftoken');   

    let url = "/davlatadd"

    fetch(url, {
            method: 'POST', // or 'PUT'            
            body: JSON.stringify({ val: val }), 
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
              },           
          })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data[0]['viloyat_nomi']);
           
            viloyat.innerHTML = `<option value = "" selescted>---------------</option>`
            for(let i = 0; i<data.length; i++){
                viloyat.innerHTML += `<option value = "${data[i]["id"]}" selescted>${data[i]["viloyat_nomi"]}</option>`
          
            }
          })
          viloyat.addEventListener("change", pickState)

          function pickState(e){   
              const vil=e.target.value;
              const csrftoken = getCookie('csrftoken');
              console.log("value", vil)
          
              let url = "/viladd"
          
              fetch(url, {
                      method: 'POST', // or 'PUT'            
                      body: JSON.stringify({ val: vil }), 
                      headers: {
                          'Content-Type': 'application/json',
                          'X-CSRFToken': csrftoken
                        },           
                    })
                    .then(response => response.json())
                    .then(data => {
                      console.log('Success:', data[0]['tuman_nomi']);
                     
                      tuman.innerHTML = `<option value = "" selescted>---------------</option>`
                      for(let i = 0; i<data.length; i++){
                          tuman.innerHTML += `<option value = "${data[i]["id"]}" selescted>${data[i]["tuman_nomi"]}</option>`
                    
                      }
                    })
          };
          
};
