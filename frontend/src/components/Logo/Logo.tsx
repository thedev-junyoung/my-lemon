import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { LogoProps } from '../../types';

const Logo: React.FC<LogoProps> = ({ isResponsive = false, isCentered = false }) => {
    const [logoSrc, setLogoSrc] = useState<string>('/logo/logo150x75.png');
    const navigate = useNavigate();

    const updateLogoSrc = () => {
        if (window.innerWidth <= 768) {
            setLogoSrc('/logo/logo100x50.png');
        } else {
            setLogoSrc('/logo/logo150x75.png');
        }
    };

    useEffect(() => {
        if (isResponsive) {
            updateLogoSrc();
            window.addEventListener('resize', updateLogoSrc);

            return () => {
                window.removeEventListener('resize', updateLogoSrc);
            };
        }
    }, [isResponsive]);

    return (
        <div
            className={`logo ${isCentered ? 'mx-auto' : ''}`}
            onClick={() => navigate('/')}
            style={{ cursor: 'pointer' }}
        >
            <img src={logoSrc} alt="LEMON Logo" className="h-auto" />
        </div>
    );
};

export default Logo;
