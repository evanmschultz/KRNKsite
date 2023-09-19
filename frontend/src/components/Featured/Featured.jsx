import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import styles from "./Featured.module.css"
import axios from "axios";

function shuffleArray(array) {
    let shuffledArray = [...array];
    for (let i = shuffledArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
    }
    return shuffledArray;
}

const Featured = (props) => {
    const [articles, setArticles] = useState([]);
    const [shuffledArticles, setShuffledArticles] = useState([]);

    useEffect(() => {
        // Fetch articles when the component mounts
        axios.get("http://127.0.0.1:8000/api/papers/")
            .then(res => {
                setArticles(res.data);
            })
            .catch(err => {
                if (err.response) {
                    console.log(err.response.data);
                } else {
                    console.log('Error', err.message);
                }
                console.error(err);
            });
    }, []);

    useEffect(() => {
        // Shuffle the articles array when it changes
        const shuffled = shuffleArray(articles);
        // Slice the first 5 articles from the shuffled array
        const randomFive = shuffled.slice(0, 5);
        setShuffledArticles(randomFive);
    }, [articles]);

    return (
        <>
            {shuffledArticles.map((article, idx) => (
                <div className={styles.container} key={idx}>
                    <div className={styles.article}>
                    <h3>{article.title}</h3>
                    <Link to={`/article/${article.id}`} style={{ color: "black", flex: "2" }}>
                        Go to Article
                    </Link>
                    </div>
                </div>
            ))}
        </>
    )
}

export default Featured;
