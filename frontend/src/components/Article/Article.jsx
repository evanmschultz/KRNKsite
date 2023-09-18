import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from '../Navbar/Navbar';
import styles from './Article.module.css';
import { useParams, Link } from 'react-router-dom';
import { Button } from '@mui/material';

const Article = (props) => {
    const { id } = useParams();
    const [paper, setPaper] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:8000/api/paper/get/' + id)
            .then(res => {
                setPaper(res.data)
                console.log(res.data)
            })
            .catch(err => console.log(err))
    }, [])

    return (
        <>
            <Navbar userId={1}></Navbar>
            <div className={styles.content}>
                <h1>Title</h1>
                <hr />
                <p>A summary of the article (abstract)</p>
                <hr />
                <Button variant="outlined" component={Link} to={paper.pdf_url} style={{color: "black", border: "1px solid black"}}>To Source</Button>
            </div>
        </>
    )
}

export default Article