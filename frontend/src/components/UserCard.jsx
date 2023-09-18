import axios from 'axios';
import React, { useState, useEffect } from 'react';

function UserCard() {
	const [user, setUser] = useState({
		first_name: '',
		last_name: '',
		email: '',
		password: ''
	});

	useEffect(() => {
		axios
			.get('http://localhost:8000/v1/users/1') //Test case, will need to change to dynamic
			.then((res) => setUser(res.data))
			.then((res) => console.log(res))
			.catch((err) => console.log(err));
	}, []);

	return (
		<div>
			UserCard
			<h1>Test of {user.first_name} </h1>
			{user.last_name}
			{user.email}
		</div>
	);
}

export default UserCard;
