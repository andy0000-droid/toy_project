# toy_project
# Development branch

## Toy project Repository   
https://www.notion.so/choi-study/Toy-Project-e2064d9d482f4fb38f474944427989d9?pvs=4   

# Explain about branch
## 각 브랜치는 각각의 역할을 수행해야하며, 브랜치가 꼬이는 일 없도록 주의해서 개발바랍니다.

### 필요에 따라 각 브랜치를 임의로 생성하고, 브랜치에 대한 설명을 작성하셔도 됩니다.
master: 전체 개발이 완료된 이후 release되는 버전   
dev: 각 기능 구현이 완료된 이후, 기존 구현물과 병합하는 버전   
feature: 각 기능의 세부 사항을 구현   
release: 배포 준비 (master 브랜치의 다음 버전)   
hotfix: 현재 서비스에서 긴급하게 수정해야 되는 부분에 대하여 사용되는 임시 브랜치   


Commit Message Example

Notion에 Commit version 항목 참조하여 Commit message 제목과 내용 분리
VSCode 상에서 제목 내용 분리는 엔터 2번으로 가능함

# Git Command
## git checkout (branch name)
해당 브랜치로 이동   

## git branch (branch name)
새로운 브랜치 생성

## git add (스테이징할 파일)
파일들을 스테이징 상태로 올림

## git commit -m "커밋 메세지"
스테이징한 파일들에 대한 커밋

## git push
커밋한 내용 반영

## git pull
최신 상태의 레포지토리 가져오기