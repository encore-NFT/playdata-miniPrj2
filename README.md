# PlayData-MiniPrj2

**엔코아 플레이데이터 빅데이터 엔지니어 교육과정**에서 진행한 두 번째 미니 프로젝트입니다.

</br>

### 💻 프로젝트 주제

- 어린이 뉴스 핫 토픽
- Hadoop Ecosystem 의 이해
- MongoDB에 신문 웹크롤링 데이터 적재 및 Hadoop MapReduce를 이용한 wordcount

> 수집 : MongoDB 수집 (비정형 빅데이터의 형태) </br>
> 적재 : MongoDB에서 추출된 json 데이터  Hadoop HDFS에 적재 </br>
> 처리 및 탐색 : Hive SQL로 csv 추출, csv를 MySQL에 적재 </br>
> 분석 및 응용 : Word Cloud (csv), Django (Mysql) - 데이터 전처리 및 시각화 </br>

</br>

### ✨ 팀 소개

**Not Fungible Team(NFT)**

👩‍💻 김은옥 : 웹 크롤링,  Docker을 이용한 환경 구축, Django 구축 </br>
👨‍💻 한지웅 : 웹 크롤링, 자연어 처리, 몽고DB 연동 및 적재 </br>
👨‍💻 박지수 : 웹 크롤링, 자연어 처리, MySQL 연동 및 적재 </br>
👨‍💻 정승헌 : 웹 크롤링, HIVE metadata mapping, HDFS </br>

</br>


### 💡 개발 환경 & 기술 스택

<p>
OS : <img src="https://img.shields.io/badge/macOS-000000?style=flat-square&logo=macOS&logoColor=white"/> <img src="https://img.shields.io/badge/Debian-A5915F?style=flat-square&logo=Debian&logoColor=white"/></br>
Communication : <img src="https://img.shields.io/badge/Slack-4A154B?style=&logo=Slack&logoColor=white"/> <img src="https://img.shields.io/badge/Zoom-2D8CFF?style=flat-square&logo=Zoom&logoColor=white"/> </br>
Tools : <img src="https://img.shields.io/badge/Visual Studio-007ACC?style=flat-square&logo=Visual Studio&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/></br>
</p>
<p>
DB : <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/> </br>
Web Crawling : <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>  </br>
적재 및 처리 : <img src="https://img.shields.io/badge/Apache Hive-FDEE21?style=flat-square&logo=Apache-Hive&logoColor=black"/> <img src="https://img.shields.io/badge/Apache Hadoop-66CCFF?style=flat-square&logo=Apache-Hadoop&logoColor=black"/> </br>
분석 : <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=Pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
</p>

</br>


###  Hadoop Architecture

![캡처](https://user-images.githubusercontent.com/44595181/152994014-80deddab-102f-468b-9b8a-77270edeba0b.PNG)

</br>

### Data Flow

![캡처2](https://user-images.githubusercontent.com/44595181/152994049-20c85dab-3960-44af-8327-09657f1e5540.PNG)

</br>

### 💻 Version

Python 3.8.8 </br>
Docker 20.10.12 </br>
Hdoop 3.2.1 </br>
Hive 2.3.2 </br>
mysql 5.7 </br>
mongo 5.0.6 </br>
