import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function InterestList() {

    const [interests, setInterests] = useState([])
    useEffect(() => {
        axios.get('http://localhost:8000/api/topics/')
            .then(res => {
                setInterests(res.data)
            })
            .catch(err => console.log(err))
    }, [])

    const handleTopicClick = (id) => {
        console.log(id)
    }
    // TODO: Add axios request to get user's interests for Featured

    return (
        <>
            <div>
                {interests.map((interest, idx) => {
                    return (
                        <div key={idx}>
                            <button onClick={() => handleTopicClick(interest.id)}>
                                {interest.name}
                            </button>
                        </div>
                    )
                })}
            </div>

        </>
    )
}

export default InterestList