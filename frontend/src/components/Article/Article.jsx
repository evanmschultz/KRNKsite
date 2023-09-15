import React from 'react';
import Navbar from '../Navbar/Navbar';
import styles from './Article.module.css';

const Article = (props) => {
    return (
        <>
            <Navbar></Navbar>
            <div className={styles.content}>
                <h1>Article</h1>
            </div>
        </>
    )
}

export default Article