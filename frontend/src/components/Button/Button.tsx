import React from 'react';
import './Button.css';
import { ButtonProps } from '../../types'

const Button: React.FC<ButtonProps> = ({ label, onClick }) => {
  return (
    <button className="custom-button" onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;
