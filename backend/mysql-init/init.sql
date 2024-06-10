-- 데이터베이스와 사용자 계정 생성
CREATE DATABASE IF NOT EXISTS lemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 사용자 계정 생성 또는 업데이트
CREATE USER IF NOT EXISTS 'lemon'@'%' IDENTIFIED BY '081908';

-- 'lemon' 사용자의 인증 플러그인을 'caching_sha2_password'로 설정
ALTER USER 'lemon'@'%' IDENTIFIED WITH mysql_native_password BY '081908';

-- 'lemon' 사용자에게 모든 데이터베이스에 대한 모든 권한 부여
GRANT ALL PRIVILEGES ON *.* TO 'lemon'@'%' WITH GRANT OPTION;

-- 변경 사항 적용
FLUSH PRIVILEGES;
