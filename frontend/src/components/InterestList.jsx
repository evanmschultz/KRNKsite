import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

function InterestList() {

    const [interests, setInterests] = useState([])
    useEffect(() => {
        axios.get('http://localhost:8000/api/topics/')
            .then(res => {
                setInterests(res.data)
            })
            .catch(err => console.log(err))
    }, [])

    // TODO: Add axios request to get user's interests for Featured

    return (
        <>
            <p>List of Interest Buttons</p>
            <p>These could link to articles about the specific interest??</p>
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