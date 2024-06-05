import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar';
import ChatContent from '../../components/ChatContent/ChatContent';

const Home: React.FC = () => {
  return (
    <div id="home-page" className="flex h-screen">
    
      <Sidebar />
      <ChatContent />
    </div>
  );
};

export default Home;