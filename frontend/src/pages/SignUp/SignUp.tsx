import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import InputField from '../../components/InputField/InputField'; // 새로 만든 InputField 컴포넌트
import Button from '../../components/Button/Button';
import axiosInstance from '../../api/axiosInstance'; // Axios 인스턴스 가져오기
import Logo from '../../components/Logo/Logo';
const SignUp: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSignUp = async (e: React.FormEvent) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setErrorMessage('Passwords do not match');
      return;
    }
    try {
      const response = await axiosInstance.post('/auth/signup', { name, email, password });
      // 성공 처리 로직 추가
      console.log(response.data);
      alert('회원가입 완료')
      navigate('/login');
    } catch (error:any) {
      console.log('error.response:',error.response)
    }

  };

  return (
    <div className="flex justify-center items-center h-screen bg-[#303030]">
      <div className="bg-[#202020] p-8 rounded shadow-md w-full max-w-md">
        <div className="flex justify-center mb-6">
          <Logo />
        </div>
        <h1 className="text-2xl font-bold text-center mb-6 text-white">Sign Up</h1>
        {errorMessage && <p className="text-red-500 text-center">{errorMessage}</p>}
        <form onSubmit={handleSignUp}>
          <InputField label="Name" type="text" value={name} onChange={(e) => setName(e.target.value)} />
          <InputField label="Email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          <InputField label="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          <InputField
            label="Confirm Password"
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <Button type="submit" className="w-full py-2 px-4 bg-green-500 text-white rounded hover:bg-green-600 transition">
            Sign Up
          </Button>
        </form>
        <div className="text-center mt-4 text-white">
          <p>
            Already have an account?{' '}
            <a href="/login" className="text-blue-500 hover:underline">
              Log in
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
