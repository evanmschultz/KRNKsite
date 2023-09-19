import React, { useContext, useEffect, useState } from 'react';
import Navbar from '../Navbar/Navbar';
import AuthContext from '../Context/AuthContext';
import axios from 'axios';
import styles from './InterestCard.module.css';
import { Button } from '@mui/material';

const InterestCard = (props) => {
    const {currentUser, setCurrentUser} = useContext(AuthContext);
    const [topics, setTopics] = useState([]);
    const [userTopics, setUserTopics] = useState([]);
    const [loaded, setLoaded] = useState(false);
    useEffect(() => {
        axios.get('http://localhost:8000/api/topics/')
            .then(res => {
                setTopics(res.data);
            })
            .catch(err => console.log(err));
    }, []);
    useEffect(() => {
        axios.get('http://localhost:8000/api/user-interests/' + currentUser.id)
            .then(res => {
                setUserTopics(res.data.map(topic => topic.id));
                setLoaded(true);
            })
            .catch(err => console.log(err));
    }, [loaded]);

    const toggleInterest = (topicId) => {
        if (userTopics.includes(topicId)) {
            axios.delete(`http://localhost:8000/api/remove-interest/${currentUser.id}/${topicId}`)
        } else {
            axios.post(`http://localhost:8000/api/add-interest/${currentUser.id}/${topicId}`)
        }
        setLoaded(false);
    }

    return (
        <>
            <Navbar></Navbar>
            <div className={styles.content}>
                <h1>All Topics:</h1>
                <div style={{margin: "20px", textAlign: "left"}}>
                    {topics.map((topic) => {
                        return (
                            <div key={topic.id} className={styles.topic}>
                                <h3>{topic.name}</h3>
                                <Button variant='outlined' className={styles.buttonStyle} onClick={() => toggleInterest(topic.id)}>
                                    {
                                        userTopics.includes(topic.id) ?
                                        "Remove from Your Interests" :
                                        "Add to Your Interests"
                                    }
                                </Button>
                            </div>
                        )
                    })}
                </div>
            </div>
        </>
    )
}

export default InterestCard;