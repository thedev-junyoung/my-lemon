import React from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import ChatInterface from './components/ChatInterface/ChatInterface';
//import Login from './components/Login/Login';
import './App.css'; // 스타일 시트 임포트
const App: React.FC = () => {
  return (
    <div id="app-container">
      <Sidebar />
      <ChatInterface />
    </div>
  );
};

export default App;
