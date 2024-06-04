import React, { useState } from 'react';
import Sidebar from '../../components/Sidebar/Sidebar';
import ChatContent from '../../components/ChatContent/ChatContent';

import './Home.css';

const Home: React.FC = () => {
    return (
        <div id="home-page">
            {/* <Header /> */}
            <div className="layout-body">
                <Sidebar />
                <ChatContent />
            </div>
        </div>
    );
};

export default Home;
