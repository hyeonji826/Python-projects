# pyisntaller
# pip install pyinstaller
# 위 명령어로 설치
# 사용 :
# cmd 창에서
# pyinstaller 독립실행한 스크립트 파일.py

# 옵션
# --onefile : 하나의 exe파일로만 내보내는 옵션

# --noconsole : GUI 프로그램은 cmd창이 필요 없으므로 
#               해당 옵션으로 cmd창을 지울 수 있다.

# -- icon : --icon=아이콘 파일 경로
#                  위와 같이 사용하며, 전달된 이미지 파일로 실행파일의 아이콘을
#                  바꿀 수 있다. (옵션 미사용시 기본 이미지로 설정)

# --add-data : 추가 파일이나 폴더를 포함시킨다.

# cx_freeze
# 설치
# pip install xc_Freeze
# 사용
# cxfreeze 스크립트파일.py --target-dir 파일이 생성될 폴더명
# --target-dir : 뒤에 생성된 독립실행혈파일이
# 만들어질 폴더명을 폴더이름만 적으면 해당 폴더 내에 실행파일이 생성된다.

# pyexe
# 현재 작동 안됨
# from distutils.core import setup
# import py2exe
# setup(console=['program.py])

# unitka
# 설치
# pip install nuitka
# 사용
# nuitka --standalone --onefile --enable-plugin=pyqt5 program.py
# --standalone : 독립실행형으로 만든다는 옵션
# 파이썬 설치나 필요한 다른 파일들을 모두 포함
# --onfile : 실행파일 하나로 압축
# --enable-plugin=pyqt5 : pyqt5를 프로그램이 사용하고 있다면
# 해당 옵션을 추가하여 정상적으로 파일로 내보낼 수 있도록 해야한다.
# 