import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from './pages/Home/Home';
import Login from './pages/Login/Login';
import SignUp from './pages/SignUp/SignUp';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex flex-col h-screen">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/SignUp" element={<SignUp />} />

          {/* 다른 페이지 경로들도 여기에 추가할 수 있습니다 */}
        </Routes>
        <ToastContainer
          position="top-center" // 화면 오른쪽 상단에 메시지 표시
          autoClose={5000} // 5초 후 자동 닫힘
          hideProgressBar={false} // 진행 바 숨기기
          newestOnTop={false} // 새 메시지를 위에 표시
          closeOnClick // 클릭으로 닫기 가능
          //rtl={false} // 오른쪽에서 왼쪽으로 읽기 모드 비활성화
          //pauseOnFocusLoss // 포커스를 잃었을 때 일시 정지
          draggable // 드래그로 이동 가능
          pauseOnHover // 마우스를 올리면 일시 정지
          className="w-full max-w-xl" // Tailwind CSS를 사용해 크기 조정
          toastClassName="relative flex p-1 min-h-10 rounded-md justify-between overflow-hidden cursor-pointer bg-blue-500 text-white shadow-lg" // 커스텀 스타일 적용
          bodyClassName="text-sm font-medium p-3 flex items-center justify-center w-20" // 내부 텍스트 스타일

        /> {/* 여기에 추가 */}
      </div>
    </Router>
  );
};

export default App;
