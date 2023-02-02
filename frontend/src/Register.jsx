import React, {useState} from "react";

export const Register = (props) => {

    const [username, setUsername] = useState('');
    const [first_name, setFirst_name] = useState('');
    const [last_name, setLast_name] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(username);
    }
    
    return(
        <div className="auth-form-container">
            <form className="register-form" onSubmit={handleSubmit}>
                <label htmlFor="username">username</label>
                <input value={username} onChange={(e)=> setUsername(e.target.value)} type="text" id="username" name="username"/>

                <label htmlFor="first_name">first name</label>
                <input value={first_name} onChange={(e)=> setFirst_name(e.target.value)} type="text" id="first_name" name="first_name"/>

                <label htmlFor="last_name">last name</label>
                <input value={last_name} onChange={(e)=> setLast_name(e.target.value)} type="text" id="last_name" name="last_name"/>

                <label htmlFor="email">email</label>
                <input value={email} type="email" onChange={(e)=> setEmail(e.target.value)} placeholder="youremail@email.com" id="email" name="email"/>

                <label htmlFor="password">password</label> 
                <input value={password} onChange={(e)=> setPassword(e.target.value)} type="password" placeholder="********" id="password" name="password"/>

                <button type="submit">Sign Up</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('login')}>Log In</button>
        </div>
    )
}