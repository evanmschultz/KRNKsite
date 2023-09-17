import React, { useState } from "react";
import axios from "axios";
import UserForm from "../components/UserForm/UserForm";
import Featured from "../components/Featured/Featured";
import styles from "./Home.module.css";

const Home = (props) => {
    const [registerErrors, setRegisterErrors] = useState([]);
    const [loginError, setLoginError] = useState("");
    const [newUser, setNewUser] = useState(true);
    const today = new Date().toLocaleDateString();

    // Methods for later registering/logging in, will need to be updated before they can work, especially for error handling

    const registerUser = async (userParam) => {
        try {
            console.log(userParam);
            const res = await axios.post('http://127.0.0.1:8000/api/register/', userParam);
            setRegisterErrors([]);
            console.log(res);
        } catch(err) {
            if (err.response.data.message == "User already exists") {
                setRegisterErrors(["This user already exists!"]);5
            } else{
                let errorArr = []
                for (var key in err.response.data.errors) {
                    errorArr.push(err.response.data.errors[key].message);
                };
                setRegisterErrors(errorArr);
            };
        };
    };

    const loginUser = async (userParam) => {
        try {
            const res = await axios.post('http://localhost:8000/api/users/login', userParam);
            setLoginError("");
        } catch(err) {
            if (err.response.data.message) {
                setLoginError("Invalid login attempt!");
            }
        };
    };

    const toggleForm = () => {
        setNewUser(prev => !prev);
        setRegisterErrors([]);
        setLoginError("");
    }

    

    return (
        <>
        <div className={styles.container}>
            <div className={styles.header}>
                <img src={"../src/assets/logo-placeholder-image.png"} alt="logo" id={styles.logo}/>
                <div className={styles.title}>
                    <h1 style={{fontSize: "2.5rem"}}>KRNKsite</h1>
                    <p style={{fontStyle: "italic"}}>with the news</p>
                </div>
                <div className={styles.info}>
                    <h3>"And that's the way it is"</h3>
                    <p>Today: {today}</p>
                </div>
            </div>
            <div className={styles.content}>
                <Featured></Featured>
                <div className={styles.forms}>
                    {
                        newUser && <div className={styles.userform} id={styles.register}>
                            <h1>Sign Up</h1>
                            <UserForm onSubmitProp={registerUser} type="register"/>
                            <div className={styles.errors}>
                                {registerErrors.map((err, index) => (
                                        <p key={index}>{err}</p>
                                    ))}
                            </div>
                        </div>
                    }
                    {
                        !newUser && <div className={styles.userform} id={styles.login}>
                            <h1>Login</h1>
                            <UserForm onSubmitProp={loginUser} type="login"/>
                            <div className={styles.errors}>
                                <p>{loginError}</p>
                            </div>
                        </div>
                    }
                    <p className={styles.changeform} onClick={toggleForm}>
                        {
                            !newUser ?
                            "Need an account? Sign up!" :
                            "Already have an account? Log in here"
                        }
                    </p>
                </div>
            </div>
        </div>
        </>
    )
}

export default Home
