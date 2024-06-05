import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';

import Home from './pages/Home/Home';
import Login from './pages/Login/Login';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/" element={<Login />} />
        {/* 다른 페이지 경로들도 여기에 추가할 수 있습니다 */}
      </Routes>
    </Router>
  );
};

export default App;
