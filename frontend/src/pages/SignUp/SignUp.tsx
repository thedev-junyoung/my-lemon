import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import InputField from '../../components/InputField/InputField';
import Button from '../../components/Button/Button';
import axiosInstance from '../../api/axiosInstance';
import Logo from '../../components/Logo/Logo';

const SignUp: React.FC = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    if (confirmPassword.length >= 5 && password !== confirmPassword) {
      setErrorMessage('비밀번호가 일치하지 않습니다.');
    } else if (errorMessage === '비밀번호가 일치하지 않습니다.') {
      setErrorMessage('');
    }
  }, [password, confirmPassword]);

  const validateEmail = (email: string): boolean => {
    const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return re.test(String(email).toLowerCase());
  };

  const validatePassword = (password: string): boolean => {
    const re = /^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$/;
    return re.test(password);
  };

  const validateName = (name: string): boolean => {
    return name.trim().length > 0;
  };

  const validateFields = (): string => {
    if (!validateName(name)) return '이름을 입력하세요.';
    if (!validateEmail(email) && email.length > 0) return '유효한 이메일을 입력하세요.';
    if (!validatePassword(password) && password.length > 0) return '비밀번호는 최소 8자 이상이며, 소문자, 숫자, 특수 문자를 포함해야 합니다.';
    if (password !== confirmPassword) return '비밀번호가 일치하지 않습니다.';
    return '';
  };

  const handleBlur = (field: string) => {
    let error = '';
    switch (field) {
      case 'name':
        if (!validateName(name) && name.length > 0) error = '이름을 입력하세요.';
        break;
      case 'email':
        if (!validateEmail(email) && email.length > 0) error = '유효한 이메일을 입력하세요.';
        break;
      case 'password':
        if (!validatePassword(password) && password.length > 0) error = '비밀번호는 최소 8자 이상이며, 소문자, 숫자, 특수 문자를 포함해야 합니다.';
        break;
      default:
        break;
    }
    setErrorMessage(error);
  };

  const handleSignUp = async (e: React.FormEvent) => {
    e.preventDefault();
    const validationMessage = validateFields();
    if (validationMessage) {
      setErrorMessage(validationMessage);
      return;
    }

    try {
      // const response = await axiosInstance.post('/auth/signup', { name, email, password });
      // 성공 처리 로직 추가
      // console.log(response.data);
      alert('회원가입 완료');
      // navigate('/login');
    } catch (error: any) {
      console.log('error.response:', error.response);
      setErrorMessage('회원가입에 실패했습니다. 다시 시도해 주세요.');
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-[#303030]">
      <div className="bg-[#202020] p-8 rounded shadow-md w-full max-w-md">
        <div className="flex justify-center mb-6">
          <Logo />
        </div>
        <h1 className="text-2xl font-bold text-center mb-6 text-white">Sign Up</h1>
        <div className="h-6 flex items-center justify-center mb-4">
          {errorMessage && <p className="text-red-500 text-center">{errorMessage}</p>}
        </div>
        <form onSubmit={handleSignUp}>
          <InputField
            label="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            onBlur={() => handleBlur('email')}
          />
          <InputField
            label="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onBlur={() => handleBlur('password')}
          />
          <InputField
            label="Confirm Password"
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
          <InputField
            label="Name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            onBlur={() => handleBlur('name')}
          />
          <Button type="submit" className="w-full py-2 px-4 bg-green-500 text-white rounded hover:bg-green-600 transition">
            Sign Up
          </Button>
        </form>
        <div className="text-center mt-4 text-white">
          <p>
            이미 계정이 있으신가요?{' '}
            <a href="/login" className="text-blue-500 hover:underline">
              로그인
            </a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
