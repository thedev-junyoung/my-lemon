import React from 'react';

import { InputFieldProps } from '../../types'
const InputField: React.FC<InputFieldProps> = ({ label, type, value, onChange, onBlur, required = true }) => {
  return (
    <div className="mb-4">
      <label className="block text-white">{label}</label>
      <input
        type={type}
        value={value}
        onChange={onChange}
        onBlur={onBlur}
        className="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        required={required}
      />
    </div>
  );
};

export default InputField;
