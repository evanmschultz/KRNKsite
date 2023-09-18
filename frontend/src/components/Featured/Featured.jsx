import React from "react";
import { Link } from "react-router-dom";
import styles from "./Featured.module.css"

const Featured = (props) => {
    // const { articles } = props;
    // Set up Featured to take in props determined by axios get request so it can be reused on the dashboard and the home page

    return (
        <>
            <div className={styles.container}>
                <div className={styles.article}>
                    {/* <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture}/> */}
                    <h3><Link to={"/article/0"} style={{color: "black"}}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
                <div className={styles.article}>
                    {/* <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture}/> */}
                    <h3><Link to={"/article/0"} style={{color: "black"}}>Headline</Link></h3>
                    <p>Breaking news! This article is a demonstration of a long description that features automatic cutoff when things get too big. Like way, way, way, way, way, way, way, way, way too big.</p>
                </div>
                <div className={styles.article}>
                    {/* <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture}/> */}
                    <h3><Link to={"/article/0"} style={{color: "black"}}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
                <div className={styles.article}>
                    {/* <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture}/> */}
                    <h3><Link to={"/article/0"} style={{color: "black"}}>Headline</Link></h3>
                    <p>Breaking news! This article is a demonstration of a medium description</p>
                </div>
                <div className={styles.article}>
                    {/* <img src="../src/assets/test-image.png" alt="article picture" className={styles.articlePicture}/> */}
                    <h3><Link to={"/article/0"} style={{color: "black"}}>Headline</Link></h3>
                    <p>Brief Description</p>
                </div>
            </div>
        </>
    )
}

export default Featured