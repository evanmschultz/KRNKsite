import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import { Button } from '@mui/material';

const listStyle = {
    display: "flex",
    flexDirection: "column",
    gap: "20px",
    margin: "20px 0px"
}

const buttonStyle = {
    color: "black",
    border: "1px solid black"
}

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
        <div style={listStyle}>
            {interests.map((interest, idx) => {
                return (
                    <div key={idx}>
                        <Button variant='outlined' style={buttonStyle} component={ Link } to={'/topic/' + interest.id}>
                            {interest.name}
                        </Button>
                    </div>
                )
            })}
        </div>
    )
}

export default InterestList