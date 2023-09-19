import React from 'react';
import Navbar from '../Navbar/Navbar';
import styles from './InterestCard.module.css';

const InterestCard = (props) => {
    return (
        <>
            <Navbar></Navbar>
            <div className={styles.content}>
                <h1>Interest Form</h1>
            </div>
        </>
    )
}

export default InterestCard