// src/pages/Login/Login.tsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import KakaoLogin from 'react-kakao-login';

const Login: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleLogin = (e: React.FormEvent) => {
        e.preventDefault();
        // 간단한 인증 로직 예제
        if (email === 'user@example.com' && password === 'password') {
            navigate('/');
        } else {
            setErrorMessage('Invalid email or password');
        }
    };

    const handleKakaoLoginSuccess = (response: any) => {
        console.log(response);
        // 카카오 로그인 성공 시 처리 로직
        navigate('/');
    };

    const handleKakaoLoginFailure = (error: any) => {
        console.log(error);
        setErrorMessage('Kakao login failed');
    };

    return (
        <div className="flex justify-center items-center h-screen bg-[#303030]">
            <div className="bg-[#202020] p-8 rounded shadow-md w-full max-w-md">
                <div className="flex justify-center mb-6">
                    <img src="/logo/logo200x100.png" alt="logo" className="h-auto" />
                </div>
                <h1 className="text-2xl font-bold text-center mb-6 text-white">Login</h1>
                {errorMessage && <p className="text-red-500 text-center">{errorMessage}</p>}
                <form onSubmit={handleLogin}>
                    <div className="mb-4">
                        <label className="block text-white">Email</label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-white">Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
                    >
                        Log in
                    </button>
                </form>
                <div className="text-center mt-4 text-white">Or</div>
                <div className="mt-3 mb-3 flex justify-center">
                    <KakaoLogin
                        token="YOUR_KAKAO_APP_KEY"
                        onSuccess={handleKakaoLoginSuccess}
                        onFail={handleKakaoLoginFailure}
                        className="kakao-login-button"
                    >
                        <img
                            src="kakao/kakao_login_medium_narrow.png"
                            alt="Kakao Login"
                            className="w-full h-full"
                        />
                    </KakaoLogin>
                </div>
                <div className="text-center mt-4 text-white">
                    <p>
                        Don't have an account?{' '}
                        <a href="/signup" className="text-blue-500 hover:underline">
                            Sign up
                        </a>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Login;
