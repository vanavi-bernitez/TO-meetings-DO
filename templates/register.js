const registerForm = document.getElementById('register-form')
const baseEndpoint = "http://127.0.0.1:8000/user"
// http://127.0.0.1:8000/user/register/

if (registerForm) {
    registerForm.addEventListener('submit', handleRegister)
}

function handleRegister(event) {
    console.log(event)
    event.preventDefault()
    const registerEndpoint =`${baseEndpoint}/register/`
    let registerFormData = new FormData(registerForm)
    let registerObjectData = Object.fromEntries(registerFormData)
    let bodyStr = JSON.stringify(registerObjectData)
    
    console.log(registerObjectData['username'], bodyStr)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(registerEndpoint, options)
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(x=>{
        console.log(x)
    })
    .catch(err=> {
        console.log('err', err)
    })
}