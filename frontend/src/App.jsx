import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './views/Home';
import Dashboard from './views/Dashboard';
import InterestCard from './components/InterestCard';
import Article from './components/Article/Article';
import UserCard from './components/UserCard/UserCard';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/interests" element={<InterestCard />} />
        <Route path="/article/:id" element={<Article />} />
        <Route path="/edit/:id" element={<UserCard />} />
      </Routes>
    </Router>
  );
}

export default App;
