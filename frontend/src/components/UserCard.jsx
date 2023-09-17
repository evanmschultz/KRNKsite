import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import { Button, Table, TableBody, TableRow, TableCell, TableContainer } from "@mui/material";

const UserCard = (props) => {
    const {id} = useParams();
    const [user, setUser] = useState({
		first_name: "",
		last_name: "",
		email: "",
		topics: [],
		created_at: new Date().toLocaleDateString()
	});

    const navigate = useNavigate();
    useEffect(() => {
        const fetchUser = async () => {
            const res = await axios.get('http://localhost:8000/users/' + id);
            const data = await res.data;
            setUser(data);
        }
        fetchUser().catch((err) => console.log(err));
		console.log(user)
    }, []);

    return (
        <>
            <h1>{user.first_name + " " + user.last_name}</h1>
			<p>Member since: {user.created_at}</p>
            <TableContainer>
                <Table>
                    <TableBody> 
                        <TableRow>
                            <TableCell style={{textAlign: "left"}}>Test</TableCell>
                            <TableCell style={{textAlign: "right"}}>Test</TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>
        </>
    );
};

export default UserCard;