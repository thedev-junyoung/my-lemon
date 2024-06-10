import logging
from colorlog import ColoredFormatter
import os


# NOTICE 레벨을 정의합니다.
NOTICE_LEVEL_NUM = 25
logging.addLevelName(NOTICE_LEVEL_NUM, 'NOTICE')

def notice(self, message, *args, **kws):
    if self.isEnabledFor(NOTICE_LEVEL_NUM):
        self._log(NOTICE_LEVEL_NUM, message, args, **kws)

# NOTICE 메소드를 Logger 클래스에 추가합니다.
logging.Logger.notice = notice
def setup_logging():
    # 커스텀 Formatter 생성
    colored_formatter = ColoredFormatter(
        "%(log_color)s[%(levelname)s][%(asctime)s] %(filename)s :%(lineno)d, %(funcName)s(), %(message)s ",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
            'NOTICE': 'white'  # NOTICE 레벨
        },
        reset=True,
        style='%'
    )

    # 로거 생성
    
    # 로그 파일의 절대 경로를 구성합니다.
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'log'))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # 로그 디렉토리가 없으면 생성합니다.
    log_file_path = os.path.join(log_dir, 'application.log')
    file_handler = logging.FileHandler(log_file_path)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # 로깅 레벨 설정
    logger.handlers.clear()  # 기존 핸들러 제거
    #file_handler = logging.FileHandler('../../log/application.log')
    file_handler.setFormatter(colored_formatter)
    logger.addHandler(file_handler)
    # 로그 핸들러 생성 및 Formatter 설정
    handler = logging.StreamHandler()
    handler.setFormatter(colored_formatter)

    # 로거에 핸들러 추가
    logger.addHandler(handler)

    # Werkzeug의 로깅 레벨 변경
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)  # 또는 logging.CRITICAL 등

    return logger

logger = setup_logging()