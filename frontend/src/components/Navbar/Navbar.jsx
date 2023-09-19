import React from 'react';
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';
import {
	Button,
	Accordion,
	AccordionSummary,
	AccordionDetails
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import styles from './Navbar.module.css';

const digestStyle = {
	color: 'black',
	backgroundColor: 'whitesmoke',
	border: '1px solid black',
	marginTop: '5px',
	textShadow: 'none'
};

const Navbar = (props) => {
	// TODO: Must pass in the prop wherever necessary
	const { userId } = props;
	const today = new Date().toLocaleDateString();
	const logoutUser = async (e) => {
		try {
			const res = await axios.post(
				'http://localhost:8000/users/logout',
				{},
				{ withCredentials: true }
			);
		} catch (err) {
			console.log(err);
		}
	};
	return (
		<>
			<div className={styles.header}>
				<div className={styles.info}>
					<p>Today: {today}</p>
					<Button
						variant='outlined'
						component={Link}
						to={'/dashboard'}
						style={digestStyle}
					>
						Daily Digest
					</Button>
				</div>
				<div className={styles.title}>
					<h1 style={{ fontSize: '2.5rem' }}>KRNKsite</h1>
					<p style={{ fontStyle: 'italic' }}>with the news</p>
				</div>
				<div className={styles.menu}>
					<Accordion style={{ border: '1px solid black' }}>
						<AccordionSummary
							expandIcon={<ExpandMoreIcon />}
							aria-controls='account-content'
						>
							<h3>Account</h3>
						</AccordionSummary>
						<AccordionDetails>
							<div>
								<Button component={Link} to={'/interests'}>
									Interests
								</Button>
							</div>
							<div>
								<Button component={Link} to={'/user/' + userId}>
									Settings
								</Button>
							</div>
							<div>
								<Button
									component={Link}
									to={'/'}
									onClick={logoutUser}
								>
									Logout
								</Button>
							</div>
						</AccordionDetails>
					</Accordion>
				</div>
			</div>
		</>
	);
};

export default Navbar;
