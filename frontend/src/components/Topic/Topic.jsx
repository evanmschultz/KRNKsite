import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../Navbar/Navbar";
import { useParams } from "react-router-dom";
import styles from "./Topic.module.css";

const Topic = (props) => {
    const {id} = useParams();
    const [papers, setPapers] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:8000/api/papers/')
            .then(res => {
                setPapers(res.data)
            })
            .catch(err => console.log(err))
    }, [])
    return (
        <>
            <Navbar></Navbar>
            <div className={styles.content}>
                {papers.map((paper, idx) => {
                    return (
                        <div key={idx}>
                            <p>{paper.pdf_url}</p>
                        </div>
                    )
                })}
            </div>
        </>
    );
};

export default Topic;