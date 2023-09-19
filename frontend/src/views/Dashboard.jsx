import React from 'react';
import Navbar from '../components/Navbar/Navbar';
import Digest from '../components/Digest';
import InterestList from '../components/InterestList';
import { Link } from 'react-router-dom';
import styles from './Dashboard.module.css';
import {useAuth} from '../components/Context/AuthContext';

const Dashboard = () => {
    const {user} = useAuth();
    const userId = user.id;
    console.log("userId: " + userId);

    return (
        <>
            <Navbar userId={userId}></Navbar>
            <div className={styles.content}>
                <div className={styles.interests}>
                    <h1>Your Interests:</h1>

                    {/* {user && ( // Check if the user is logged in   <---- This is all pointless, because it's passed up from Login. 
                        <>
                            <Link style={{ color: "black" }} to={"/interests"}>
                                (Edit)
                            </Link>
                            <InterestList></InterestList>
                        </>
                    )} */}
                    
                    <Link style={{color: "black"}} to={"/interests"}>(Edit)</Link>
                    <InterestList></InterestList>
                </div>
                <div className={styles.digest}>
                    <Digest></Digest>
                </div>
            </div>
        </>
    )
}

export default Dashboard