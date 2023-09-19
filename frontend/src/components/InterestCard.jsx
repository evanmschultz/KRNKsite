import React from 'react';
import { useAuth } from '../components/Context/AuthContext';
import Navbar from '../components/Navbar/Navbar';

const InterestCard = (props) => {
    const { user } = useAuth(); // Access user data from the context

    // Use the user data for your API call
    // ...

    return (
        <>
        <Navbar />
        <div>
            <p>Hi</p>
        </div>
        </>
    );
};

export default InterestCard;