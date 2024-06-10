import React from 'react';
import { ButtonProps } from '../../types'; // ButtonProps를 정의해주세요

// Button 컴포넌트
const Button: React.FC<ButtonProps> = ({ onClick, className, children, type = 'button', disabled = false }) => {
    return (
        <button
            type={type}
            className={`p-2 rounded-full focus:outline-none ${className}`}
            onClick={onClick}
            disabled={disabled}
        >
            {children}
        </button>
    );
};

export default Button;