from setuptools import setup, find_packages

setup(
    name='sysmet',  # 패키지 이름
    version='0.1',  # 패키지 버전
    packages=find_packages(),  # 패키지 포함 디렉토리 자동 찾기
    include_package_data=True,
    license='Apache License 2.0',  # 라이선스
    description='Log System Metrics',  # 짧은 설명
    long_description=open('README.md').read(),  # README 파일을 긴 설명으로 사용
    long_description_content_type='text/markdown',  # 마크다운 형식 지정
    author='The Protein',  # 작성자 이름
)

