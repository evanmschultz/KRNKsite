import React from 'react';
import Navbar from '../components/Navbar/Navbar';
import Digest from '../components/Digest';
import styles from './Dashboard.module.css';

const Dashboard = () => {
    return (
        <>
            <Navbar userId={0}></Navbar>
            <div className={styles.content}>
                <Digest></Digest>
            </div>
        </>
    )
}

export default Dashboard