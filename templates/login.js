const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://127.0.0.1:8000/user"
// http://127.0.0.1:8000/user/login/

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint =`${baseEndpoint}/login/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    
    console.log(loginObjectData['username'], bodyStr)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr,
        redirect: follow
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        window.location.reload()
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