import React, { useState } from 'react';
import axios from 'axios';
import UserForm from '../components/UserForm/UserForm';
import Featured from '../components/Featured/Featured';
import styles from './Home.module.css';
import { useNavigate } from 'react-router-dom';

const Home = (props) => {
	const [errors, setErrors] = useState({
		firstNameError: "",
		lastNameError: "",
		emailError: "",
		passwordError: "",
		confirmError: "",
		loginError: ""
	});
	const [newUser, setNewUser] = useState(true);
	const navigate = useNavigate();
	const today = new Date().toLocaleDateString();

	// TODO: Add axios request to get random articles for Featured

<<<<<<< HEAD
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
=======
	const registerUser = async (userParam) => {
		try {
			const res = await axios.post(
				'http://localhost:8000/users/register/',
				userParam,
				{ withCredentials: true }
			);
			setErrors({
				firstNameError: "",
				lastNameError: "",
				emailError: "",
				passwordError: "",
				confirmError: "",
				loginError: ""
			});
			navigate("/dashboard")
		} catch (err) {
			if (err.response.data.detail == "Email already registered") {
			    setErrors((prev) => ({...prev, emailError: "This email is already in the system!"}));
			} else{
			    for (const error of err.response.data.detail) {
			        if (error.msg.includes("Password")) {
						if (error.msg.includes("8")) {
							setErrors((prev) => ({...prev, passwordError: "Password must be at least 8 characters long!"}));
						} else if (error.msg.includes("1")) {
							setErrors((prev) => ({...prev, passwordError: "Password must contain at least: 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character."}));
						} else {
							setErrors((prev) => ({...prev, passwordError: "", confirmError: "Passwords do not match!"}));
						}
					}
					if (error.msg.includes("email")) {
						setErrors((prev) => ({...prev, emailError: "Invalid email address!"}));
					}
			    };
			};
		};
	};

	const loginUser = async (userParam) => {
		try {
			const res = await axios.post(
				'http://localhost:8000/users/login',
				userParam,
				{ withCredentials: true }
			);
			setErrors({
				firstNameError: "",
				lastNameError: "",
				emailError: "",
				passwordError: "",
				confirmError: "",
				loginError: ""
			});
			navigate("/dashboard")
		} catch (err) {
			setErrors((prev) => ({...prev, loginError: "Invalid login attempt!"}));
		}
	};

	const toggleForm = () => {
		setNewUser((prev) => !prev);
		setErrors({
			firstNameError: "",
			lastNameError: "",
			emailError: "",
			passwordError: "",
			confirmError: "",
			loginError: ""
		})
	};
	return (
		<>
			<div className={styles.container}>
				<div className={styles.header}>
					<img
						src={'../src/assets/logo-placeholder-image.png'}
						alt='logo'
						id={styles.logo}
					/>
					<div className={styles.title}>
						<h1 style={{ fontSize: '2.5rem' }}>KRNKsite</h1>
						<p style={{ fontStyle: 'italic' }}>with the news</p>
					</div>
					<div className={styles.info}>
						<h3>"And that's the way it is"</h3>
						<p>Today: {today}</p>
					</div>
				</div>
				<div className={styles.content}>
					{/* TODO: Add articles prop to featured later */}
					<div className={styles.featured}>
						<h1>Featured Articles</h1>
						<Featured></Featured>
					</div>
					<div className={styles.forms}>
						{newUser && (
							<div
								className={styles.userform}
								id={styles.register}
							>
								<h1>Sign Up</h1>
								<UserForm
									onSubmitProp={registerUser}
									type='register'
									errors={errors}
								/>
							</div>
						)}
						{!newUser && (
							<div className={styles.userform} id={styles.login}>
								<h1>Login</h1>
								<UserForm
									onSubmitProp={loginUser}
									type='login'
									errors={errors}
								/>
							</div>
						)}
						<p className={styles.changeform} onClick={toggleForm}>
							{!newUser
								? 'Need an account? Sign up!'
								: 'Already have an account? Log in here'}
						</p>
					</div>
				</div>
			</div>
		</>
	);
};
>>>>>>> main

export default Home;
