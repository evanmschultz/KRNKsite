import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

function InterestList() {
    const [interests, setInterests] = useState([])
    const navigate = useNavigate();
    useEffect(() => {
        axios.get('http://localhost:8000/api/topics/')
            .then(res => {
                setInterests(res.data)
            })
            .catch(err => console.log(err))
    }, [])

    const handleTopicClick = (id) => {
        navigate('/topic/' + id)
    }
    // TODO: Add axios request to get user's interests for Featured

    return (
        <>
            {interests.map((interest, idx) => {
                return (
                    <div key={idx}>
                        <button onClick={() => handleTopicClick(interest.id)}>
                            {interest.name}
                        </button>
                    </div>
                )
            })}
        </>
    )
}

export default InterestList