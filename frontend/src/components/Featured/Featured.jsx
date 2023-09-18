import React, { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./Featured.module.css"
import axios from "axios";

const Featured = (props) => {
    // const { articles } = props;
    // Set up Featured to take in props determined by axios get request so it can be reused on the dashboard and the home page

    // const [articles, setArticles] = useState([]);

    // const getArticles = () => {
    //     axios.get("http://127.0.0.1:8000/api/papers/") <- The SQL database was filled with a sample cell, and it was working. Key takeaways: the DateTime needed to be filled to avoid the 411 error.
    //         .then(res => {
    //             setArticles(res.data);
    //         })
    //         .catch(err => {
    //             if (err.response) {
    //                 console.log(err.response.data);
    //             } else {
    //                 console.log('Error', err.message);
    //             }
    //             console.error(err);
    //         });
    // }


    return (
        <>
            {/* <h1> Test of Get of DB info.</h1>
            <button onClick={getArticles}>Get Articles</button>

            {articles.map((article, idx) => {  
                return (
                    <div key={idx}>
                        <h1>{article.id}</h1>

                    </div>
                )
            })} */}

            <div className={styles.container}>
                <div className={styles.article}>
                    <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture} />
                    <h3><Link to={"/article/0"} style={{ color: "black" }}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
                <div className={styles.article}>
                    <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture} />
                    <h3><Link to={"/article/0"} style={{ color: "black" }}>Headline</Link></h3>
                    <p>Breaking news! This article is a demonstration of a long description that features automatic cutoff when things get too big</p>
                </div>
                <div className={styles.article}>
                    <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture} />
                    <h3><Link to={"/article/0"} style={{ color: "black" }}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
                <div className={styles.article}>
                    <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture} />
                    <h3><Link to={"/article/0"} style={{ color: "black" }}>Headline</Link></h3>
                    <p>Breaking news! This article is a demonstration of a medium description</p>
                </div>
                <div className={styles.article}>
                    <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture} />
                    <h3><Link to={"/article/0"} style={{ color: "black" }}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
            </div>
        </>
    )
}

export default Featured