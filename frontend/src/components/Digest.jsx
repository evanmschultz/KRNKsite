import React from 'react';
import Featured from './Featured/Featured';

const Digest = (props) => {
    const today = new Date().toLocaleDateString();

    // TODO: Add axios request to get user's articles for Featured

    return (
        <>
            <h1>Daily Digest</h1>
            <p>{today}</p>
            {/* TODO: add prop so Featured can take in correct articles */}
            <Featured></Featured>
        </>
    )
}

export default Digest