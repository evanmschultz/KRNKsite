// AuthContext.js (create a context for authentication)
import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState({ id: null, username: null }); // Initialize user state with id and username

    // Function to set user data when the user logs in
    const login = (userData) => {
        setUser({
            ...userData,
            id: userData.id, // Assuming the ID is available in userData
        });
    };

    // Function to log the user out
    const logout = () => {
        setUser({ id: null, username: null }); // Clear user data
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};
