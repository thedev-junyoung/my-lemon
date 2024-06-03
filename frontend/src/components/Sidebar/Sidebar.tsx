/* 
React 컴포넌트: Sidebar 함수는 React 컴포넌트를 정의합니다.
Hooks: useState 훅을 사용하여 컴포넌트의 상태를 관리합니다.
이벤트 처리: 클릭 이벤트에 반응하여 상태를 업데이트합니다.
조건부 렌더링: JSX 내에서 JavaScript 로직을 사용하여 UI의 특정 부분을 조건부로 렌더링합니다.
리스트 렌더링: JavaScript의 map 함수를 사용하여 데이터 배열을 UI 요소 리스트로 변환합니다.
키: 리스트 아이템에 고유 key를 할당하여 효율적인 업데이트를 가능하게 합니다.
*/

import React, { useState } from 'react';
import './Sidebar.css';
import { Categories } from '../../types';

// React 함수형 컴포넌트 정의
// 컴포넌트는 독립적인 UI 부분을 캡슐화하며 재사용이 가능합니다.
const Sidebar: React.FC = () => {

    // 상태를 선언하고 초기값을 null로 설정합니다. 상태는 컴포넌트의 데이터를 관리합니다.
    const [activeCategory, setActiveCategory] = useState<string | null>(null);

    // 카테고리와 그에 속하는 하위 항목들을 저장하는 객체입니다.
    const categories: Categories = {
        '카테고리1': ['가', '나', '다'],
        '카테고리2': ['라', '마', '바'],
        // 나머지 카테고리...
    };
    // 카테고리 버튼을 클릭했을 때 호출되는 이벤트 핸들러 함수입니다.
    // 클릭된 카테고리명을 상태에 저장하거나, 이미 활성화된 카테고리를 다시 클릭하면 상태를 초기화합니다.
    const handleCategoryClick = (categoryName: string) => {

        console.log(`${categoryName} clicked`); // 콘솔 로그로 클릭 이벤트 확인
        // 여기에 상태 업데이트 또는 다른 로직 추가
        setActiveCategory(activeCategory === categoryName ? null : categoryName);

    };
    // 하위 카테고리 항목을 클릭했을 때 호출되는 이벤트 핸들러 함수입니다.
    const handleSubCategoryClick = (subcategory: string) => {
        console.log(`${subcategory} clicked`); // 콘솔 로그로 클릭 이벤트 확인       
        // 여기에 클릭된 하위 카테고리에 대한 추가 로직을 구현할 수 있습니다.


    };
    // UI를 렌더링하는 JSX 부분입니다.
    return (
        <aside id="sidebar">
            <ul className="category-list">
                {/* Object.keys와 map을 사용하여 카테고리 리스트를 동적으로 생성합니다. */}
                {Object.keys(categories).map((categoryName) => (
                    <li key={categoryName} className={`category-item ${activeCategory === categoryName ? "active" : ""}`}>
                        {/* 각 카테고리명에 대한 버튼을 생성하고 클릭 이벤트를 바인딩합니다. */}
                        <button className="category-btn" onClick={() => handleCategoryClick(categoryName)}>
                            {categoryName}
                        </button>
                        {/* 조건부 렌더링을 사용하여 활성화된 카테고리의 하위 항목들을 표시합니다. */}
                        <ul className="subcategory-list">
                            {/* 하위 항목 역시 map을 사용하여 리스트로 생성합니다. */}
                            {categories[categoryName].map((subcategory) => (
                                <li key={subcategory} className="subcategory-item" onClick={() => handleSubCategoryClick(subcategory)}>
                                    {subcategory}
                                </li>
                            ))}
                        </ul>
                    </li>
                ))}
            </ul>
        </aside>
    );
};

export default Sidebar;
