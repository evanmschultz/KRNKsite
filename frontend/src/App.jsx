import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './views/Home';
import Dashboard from './views/Dashboard';
import InterestCard from './components/InterestCard/InterestCard';
import Article from './components/Article/Article';
import UserCard from './components/UserCard/UserCard';
import Topic from './components/Topic/Topic';
import AuthContext from './components/Context/AuthContext';
import { useState } from 'react';

function App() {
  const [currentUser, setCurrentUser] = useState({});
  return (
    <AuthContext.Provider value={{currentUser, setCurrentUser}}>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/interests" element={ <InterestCard /> } />
          <Route path="/user/:id" element={ <UserCard /> } />
          <Route path="/topic/:id" element={<Topic />} />
          <Route path="/article/:id" element={<Article />} />
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
}

export default App;
