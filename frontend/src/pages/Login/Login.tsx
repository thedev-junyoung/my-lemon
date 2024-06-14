import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import KakaoLogin from 'react-kakao-login';
import InputField from '../../components/InputField/InputField'; // 새로 만든 InputField 컴포넌트
import Button from '../../components/Button/Button';
import axiosInstance from '../../api/axiosInstance'; // Axios 인스턴스 가져오기
import { login, kakaoLogin } from '../../api/auth';
import Logo from '../../components/Logo/Logo';
import { ToastContainer, toast } from 'react-toastify';

const Login: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await login(email, password);
            console.log(response);
             // CSRF 토큰을 localStorage에 저장
            const csrfToken = response.headers['X-CSRF-Token'];
            if (csrfToken) {
            localStorage.setItem('X-CSRF-Token', csrfToken);

            console.log('CSRF Token stored:', csrfToken);
            }
            console.log('X-CSRF-Token:',csrfToken)
            //debugger;
            //navigate('/');
        } catch (error: any) {
            console.log('error:',error)
            toast.error(error.message); // Toast로 에러 메시지를 표시
        }
    };


    const handleKakaoLoginSuccess = (response: any) => {
        console.log(response);
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
                    <Logo/>
                </div>
                <h1 className="text-2xl font-bold text-center mb-6 text-white">Login</h1>
                {errorMessage && <p className="text-red-500 text-center">{errorMessage}</p>}
                <form onSubmit={handleLogin}>
                    <InputField label="Email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                    <InputField label="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                    <Button type="submit" className="w-full py-2 px-4 bg-blue-500 text-white rounded hover:bg-blue-600 transition">
                        Log in
                    </Button>
                </form>
                <div className="text-center mt-4 text-white">Or</div>
                <div className="mt-3 mb-3 flex justify-center">
                    <KakaoLogin
                        token="YOUR_KAKAO_APP_KEY"
                        onSuccess={handleKakaoLoginSuccess}
                        onFail={handleKakaoLoginFailure}
                        className="w-full"
                    >
                        <img src="/kakao/kakao_login_medium_narrow.png" alt="Kakao Login" className="w-full h-full" />
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
