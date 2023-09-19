import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import AuthContext from "../Context/AuthContext";
import styles from "./UserCard.module.css";
import { Button, Table, TableBody, TableRow, TableCell, TableContainer } from "@mui/material";

const UserCard = (props) => {
    const {id} = useParams();
    const [user, setUser] = useState({
        id: id,
		first_name: "",
		last_name: "",
		email: "",
		topics: [],
		created_at: new Date().toDateString()
	});

    const navigate = useNavigate();
    useEffect(() => {
        const fetchUser = async () => {
            const res = await axios.get('http://localhost:8000/api/user/' + id);
            const data = await res.data;
            data.created_at = new Date(data.created_at).toLocaleDateString()
            setUser(data);
        }
        fetchUser().catch((err) => console.log(err));
    }, []);

    return (
        <>
        <Navbar />
            <div className={styles.content}>
                <h1>{user.first_name + " " + user.last_name}</h1>
                <p>Member since: {user.created_at}</p>
                {/* <TableContainer>
                    <Table>
                        <TableBody> 
                            <TableRow>
                                <TableCell style={{textAlign: "center"}}>Test</TableCell>
                                <TableCell style={{textAlign: "center"}}>Test</TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer> */}
            </div>
        </>
    );
};

export default UserCard;