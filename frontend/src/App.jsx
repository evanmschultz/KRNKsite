import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './views/Home';
import Dashboard from './views/Dashboard';
import Digest from './components/Digest';
import InterestCard from './components/InterestCard';
import InterestList from './components/InterestList';
import UserCard from './components/UserCard';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/digest" element={<Digest />} />
        <Route path="/InterestCard" element={<InterestCard />} />
        <Route path="/interests" element={<InterestList />} />
        <Route path="/edit/:id" element={<UserCard />} />
      </Routes>
    </Router>
  );
}

export default App;
