import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './views/Home';
import Dashboard from './views/Dashboard';
import { AuthProvider } from './components/Context/AuthContext';
import InterestCard from './components/InterestCard';
import Article from './components/Article/Article';
import UserCard from './components/UserCard/UserCard';
import Topic from './components/Topic/Topic';
import Navbar from './components/Navbar/Navbar';

function App() {

  return (
    <Router>
      <Routes>
        {/* <!-- Unprotected routes --> */}
        <Route path="/" element={<Home />} />
        {/* <!-- Protected routes --> */}
        <Route
          path="/dashboard"
          element={
            <AuthProvider>
              <Dashboard />
            </AuthProvider>
          }
        />
        <Route
          path="/interests"
          element={
            <AuthProvider>
              <InterestCard />
            </AuthProvider>
          }
        />
        <Route
          path="/user/:id"
          element={
            <AuthProvider>
              <UserCard />
            </AuthProvider>} />
        <Route path="/topic/:id" element={<Topic />} />
        <Route path="/article/:id" element={<Article />} />
      </Routes>
    </Router>

  );
}

export default App;
