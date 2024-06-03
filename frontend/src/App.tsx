import React from 'react';
import Sidebar from './Sidebar';
import ChatInterface from './ChatInterface';
import Login from './Login';
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
