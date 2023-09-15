import React from 'react';
import Navbar from '../Navbar/Navbar';
import styles from './Article.module.css';
import { useParams } from 'react-router-dom';

const Article = (props) => {
    const { id } = useParams();

    // TODO: make axios get request for article information

    return (
        <>
            <Navbar></Navbar>
            <div className={styles.content}>
                <h1>Title</h1>
                <hr />
                <p>A brief summary of the article</p>
                <hr />
                <p>Start of article or article as a pdf?</p>
            </div>
        </>
    )
}

export default Article