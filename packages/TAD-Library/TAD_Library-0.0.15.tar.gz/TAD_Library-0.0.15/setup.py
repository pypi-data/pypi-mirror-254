import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='TAD_Library',# 프로젝트 명을 입력합니다.
      version='0.0.15',      # 프로젝트 버전을 입력합니다.
      url='',      # 홈페이지 주소를 입력합니다.
      author='CHAKOON',      # 프로젝트 담당자 혹은 작성자를 입력합니다.
      author_email='yhkim@chakoon.com',      # 프로젝트 담당자 혹은 작성자의 이메일 주소를 입력합니다.
      description='TAD API',      # 프로젝트에 대한 간단한 설명을 입력합니다.
      packages=setuptools.find_packages(),      # 기본 프로젝트 폴더 외에 추가로 입력할 폴더를 입력합니다.
      long_description=open('README.md').read(),      # 프로젝트에 대한 설명을 입력합니다. 보통 README.md로 관리합니다.
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ],
      python_requires='>=3.10',
)