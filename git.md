local repo<----->remote repo

workflow:  
(Working Directory)---git init---> (ininitzation)--git add .->
-> (Staging Area)--git commit->(LocalRepository)----git push--->(github)

(Staging Area) ---reset(commit)--->(Working Directory)<---reset(add)--- (ininitzation)
(LocalRepository)<----git fetch--- (github)--git pull->(Working Directory)

+local:
echo "hoang github" >>READMDE.md
git config --global user.name "deobong"
git config --global user.email phamquochoang@gmail.com
#kiem tra lai
git config --list
git init
git add READMDE.md (file cụ thể), git add . (tất cả các file đã thay đổi ) #add file vào repo
git diff e34342 323254
git commit -m "thay doi lenh xy,za " snapshot version
git commit --amend -m "thay doi xxxxxxxx"

+remote repo
#dang nhap github tao rep copy link repo
#sau do lien ket
git remote add origin https://github.com/deobong/test.git
#dong bo vơi github
git push -u origin master(main1,main...)

+++plus
git branch [new_branch] taoj branh moi
git checkout [new_branch] chuyen branch// git checkout -b python
muốn xóa nhánh chuyển tới nhanh master và xóa nhanh đó
git checkout master
git branch -d main 1 chỉ xoa được local LENH PUSH MOI DONG BO VE remote

keo xuong
git clone
git fetch
git status
git pull
