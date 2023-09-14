import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import LogAndReg from './components/LogAndReg';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import InterestCard from './components/InterestCard';
import InterestList from './components/InterestList';
import UserCard from './components/UserCard';

function App() {

  return (
    <Router>
      <Navbar />

      <Routes>
        <Route path="/" element={<LogAndReg />} />
        <Route path="/TESTROUTE/Dashboard" element={<Dashboard />} />
        <Route path="/TESTROUTE/InterestCard" element={<InterestCard />} />
        <Route path="/TESTROUTE/InterestList" element={<InterestList />} />
        <Route path="/TESTROUTE/EditUser" element={<UserCard />} />
      </Routes>
    </Router>
  );
}

export default App;
