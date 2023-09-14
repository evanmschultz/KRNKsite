import React, { useState } from "react";
import styles from './UserForm.module.css';
import { Button, FormControl, Input, InputLabel, InputAdornment} from "@mui/material";

const UserForm = (props) => {
    const {onSubmitProp, type} = props;
    const [user, setUser] = useState({
        email: "",
        password: "",
        confirmPassword: ""
    })
    const [showPassword, setShowPassword] = useState(false);
    const handleSubmit = (e) => {
        e.preventDefault();
        // onSubmitProp(user); MAKE SURE TO UNCOMMENT LATER
        setUser({
            email: "",
            password: "",
            confirmPassword: ""
        });
    };

    return (
        <>
            <form onSubmit={handleSubmit}>
                    <div className={styles.container}>
                        <FormControl>
                            <InputLabel htmlFor={"Email" + type} style={{color: 'white', marginTop: "5px"}}>Email: </InputLabel>
                            <Input type="email" className={styles.field} id={"Email" + type} value={user.email} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, email: e.target.value}))}/>
                        </FormControl>
                        <FormControl>
                            <InputLabel htmlFor={"password" + type} style={{color: 'white', marginTop: "5px"}}>Password: </InputLabel>
                            <Input type={showPassword ? "text" : "password"} className={styles.field} id={"password" + type} value={user.password} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, password: e.target.value}))}
                            endAdornment={
                                    <InputAdornment className={styles.eye} position="end">
                                        <i className={showPassword ? `far fa-eye-slash ${styles.eye}`: `far fa-eye ${styles.eye}`} id="toggleShowPassword" onClick={() => setShowPassword(prev => !prev)}></i>
                                    </InputAdornment>
                                }/>
                            
                        </FormControl>
                        {
                            type == "register" ?
                            <FormControl>
                                <InputLabel htmlFor={"confirmPassword" + type} style={{color: 'white', marginTop: "5px"}}>Confirm Password: </InputLabel>
                                <Input type={showPassword ? "text" : "password"} className={styles.field} id={"confirmPassword" + type} value={user.confirmPassword} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, confirmPassword: e.target.value}))}/>
                            </FormControl> :
                            ""
                        }
                    </div>
                    {
                        type == "register" ?
                        <Button variant="outlined" type="submit">Sign Up</Button> :
                        <Button variant="outlined" type="submit">Log In</Button>
                    }
            </form>
        </>
    );
};

export default UserForm;