import React from 'react';
import Navbar from '../Navbar/Navbar';
import styles from './Article.module.css';
import { useParams, Link } from 'react-router-dom';
import { Button } from '@mui/material';

const Article = (props) => {
    const { id } = useParams();

    // TODO: make axios get request for article information

    return (
        <>
            <Navbar userId={1}></Navbar>
            <div className={styles.content}>
                <h1>Title</h1>
                <hr />
                <p>A brief summary of the article</p>
                <hr />
                <p>Start of article or article as a pdf?</p>
                <hr />
                <Button variant="outlined" component={Link} to={"/"} style={{color: "black", border: "1px solid black"}}>To Source</Button>
            </div>
        </>
    )
}

export default Article