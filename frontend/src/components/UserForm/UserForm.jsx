import React, { useState } from "react";
import styles from './UserForm.module.css';
import { Button, FormControl, Input, InputLabel, InputAdornment} from "@mui/material";

const UserForm = (props) => {
    const {onSubmitProp, type} = props;
    // Added first and last names because that's what the model expects.
    const [user, setUser] = useState({
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        confirm_password: ""
    })
    const [showPassword, setShowPassword] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        let submitData = {...user};
        onSubmitProp(submitData);
        setUser({
            first_name: "",
            last_name: "",
            email: "",
            password: "",
            confirm_password: ""
        });
    };
    

    return (
        <>
            <form onSubmit={handleSubmit}>
                    <div className={styles.container}>
                        <FormControl>
                            <InputLabel htmlFor={"first_name" + type} style={{color: 'white', marginTop: "5px"}}>First Name: </InputLabel>
                            <Input type="text" className={styles.field} id={"first_name" + type} value={user.first_name} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, first_name: e.target.value}))}/>
                        </FormControl>

                        <FormControl>
                            <InputLabel htmlFor={"last_name" + type} style={{color: 'white', marginTop: "5px"}}>Last Name: </InputLabel>
                            <Input type="text" className={styles.field} id={"last_name" + type} value={user.last_name} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, last_name: e.target.value}))}/>
                        </FormControl>

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
                                <InputLabel htmlFor={"confirm_password" + type} style={{color: 'white', marginTop: "5px"}}>Confirm Password: </InputLabel>
                                <Input type={showPassword ? "text" : "password"} className={styles.field} id={"confirm_password" + type} value={user.confirm_password} style={{color: 'white'}} onChange={(e) => setUser((prev) => ({...prev, confirm_password: e.target.value}))}/>
                            </FormControl> :
                            ""
                        }
                    </div>
                    {
                        type == "register" ?
                        <Button variant="outlined" type="submit" style={{color: "white", border: "1px solid white"}}>Sign Up</Button> :
                        <Button variant="outlined" type="submit" style={{color: "white", border: "1px solid white"}}>Log In</Button>
                    }
            </form>
        </>
    );
};

export default UserForm;