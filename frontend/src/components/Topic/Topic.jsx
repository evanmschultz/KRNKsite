import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../Navbar/Navbar";
import { useParams } from "react-router-dom";
import styles from "./Topic.module.css";

const Topic = (props) => {
    const {id} = useParams();
    const [papers, setPapers] = useState([]);
    useEffect(() => {
        // TODO: change this axios call to be one that gets a topic AND the papers for a given topic
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
                <h1>Articles on **Topic Name**</h1>
                {papers.map((paper, idx) => {
                    return (
                        <div key={idx}>
                            <h3>{paper.title}</h3>
                        </div>
                    )
                })}
            </div>
        </>
    );
};

export default Topic;