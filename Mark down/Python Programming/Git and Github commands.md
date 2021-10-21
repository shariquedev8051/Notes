***Reference links:***

1. [Bitbucket](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html)
2. [.gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore )
3. [Code with harry youtube](https://www.youtube.com/watch?v=evknSAkUIvs&list=PLu0W_9lII9agwhy658ZPA0MTStKUJTWPi)
4. [Code With Harry official website](https://www.codewithharry.com/videos/complete-git-tutorials-in-hindi-1)  
5. [Atlassian](https://www.atlassian.com/git/tutorials/what-is-git )

# Git usfull Commands  
## Initial setup:-
1. **`git config --global user.name`**
   **`git config --global user.email`** :-For user name and email.
   
1.  **`git config --list`** :- For finding the lists:  
    
1. **`git status`** :- For getting the status of tracked and untracked files.  
   
1. **`git init`** :- For initializing the git directory:  
   
1. **`git status`** :- Type again 
   
1. **`git add file_name`** :- To add untracked single file in staging area.

1. **`git add --a` or `git add .`** :- To add all untracked file in staging area.

1. **`git commit -m 'Message'`** :- To commit all staged files with message

1. **`git log`** :- To see logs of commits.

1. **`rm -rf .git`** :- Warning it will clear the git all files..

## Clone repository

1. **`git clone repository_address folder_name`** :- To clone the repository..

1. **`touch .gitingnore`** :- To create .gitignore file.(add file there to make them untrackable by git)
1. **`git diff`** :- Returns difference between staging area and working directory .
1. **`git diff --staged`** :- compares previous commit and stagging area.
1. **`git commit -m "direct commit"`** :-  commiting all tracked files into  staging area..

1. **`git rm fourth.txt`** :- To remove file using git so you do not have run git add.

1. **`git mv first.txt first_renamed.txt`**:- To rename the files using git.
1. When we add tracked file in .gitignore . It should not track it but it does so we have to clear cheche: **`git rm -chached file_name `**

## Git Log
1. **`git log -p`**:- git log with diffs.  
1. **`git log -p -3`** :- git log with last 3 diff
1. **`git log --stash `** :- Short summery
1. **`git log --pretty=short `** :- Short printable summary
1. **`git log --pretty=full `** :- full printable summary 
    Author - who created file
    commit - who changed something in file

1. **`git log --since=2.weeks`**:- All commits within 2 weeks  
1. **`git log --since= 2.months`** :- All commits within 2 months
1. **`git log --since= 2.years`** :- All commits within 2 years
1. **`git log --pretty=format:“%h --an”`**:- we can use this format to print just the author name and the hash  . [Git](https://git-scm.com/)
1. **`git commit --amend`** to change or add commit message
1. To use vim :
   - **i**(insert) - to edit
   - **escape** then **:wq** (write and quit)

## Git branch manage
1. **`git restore --staged file.ext`** : To unstage a file
1. **`git checkout -- file.ext`**:Now git will restore that file to its last commit state.
1. **`git checkout -f`** To restore your entire working directory to the previous commit. 
1. **`git checkout -b branchname`** :- To create new branch.
1. **`git checkout master`**:- To switch back to master branch.
1. **`git checkout branchname`**:- To check out a branch.


### To merge the branches:
1. **`git checkout master`**:- To checkout master branch  
1. **`git merge branchname`**:- To merge a branch with master.  
1. **`git add .`** :- To save all changes in master branch after merge.  
1. **`git commit -m "commit message"`**

### Git branch management:
1. **`git branch`**:- To see all the branches
1. **`git branch -v`**:- To see Branches and that branch’s last commit along with it’s message type
1. **`git branch --merged`**:-To see which branches were merged
1. **`git branch --unmerged`**:- To see branches those were not merged
1. **`it branch -d branchname`**:- To delete a branch
1. **`git branch -D branchname`**:- To delete a branch forcefully.
1. **`git rm --cached file.extension`**:- To untrack file which is being tracked before adding them into gitignore.
<p style="page-break-after:always;"></p>

# GitHub

## Accessing remote repository
1. **`git remote add origin git@github.com:yourusername/repositoryname.git`**:- add origin.
1. **`git remote -v`**:- To show you that Origin has been added.

## Cloning repository from GitHub
1. **git clone "repository url"**

## Signing in using SSH key
1. [Help is here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

## Pull command 
1. **git pull origin master**

## Fork command
1. [fork pull request](https://www.youtube.com/watch?v=e3bjQX9jIBk)

## Push command 
1. **`git push -u origin master`** :- Push git directory into GitHub.
1. **`git push -d origin branchname`**:- To delete remote GitHub directory.

# Bitbucket 

1. Add name whatever you need for e.g upload

   ```
   $ git remote add upload <link_gitbucket>
   ```

   

# How to configure multiple remote repsository

For example 

```python
$ git remote add origin repository_name(github)
```

so we have add GitHub repository with name **origin**.

```git
$ git remote add upload repository_name(bitbucket)
```

git won't allow push before pull

```
$ git pull upload <branch_name> --allow-unrelated-histories
```

if you get histories related error then type this

And bitbucket repository with name **upload**.

```git
$ git push origin master
```

 will push master branch to **GitHub**

```git
$ git push upload master
```

and will push code to bitbucket

using alias 

```git
$ alias gpob="git push origin master && git push bitbucket master"
```

or you can do this also

```
$ cd myproject
$ git remote set-url --add origin ssh://git@bitbucket.org/user/myproject.git
$ git push origin master
Everything up-to-date
Everything up-to-date
```



You can not use **pull all** command in git...



# Adding .gitignore

1. **`*.log`**:- Ignore all file having extension of.log .  
1. **`dir/`**:- Ignore content of a folder and its sub folder.  
1. **!log.log** :- will note be ignored as it has negation operator "!".

![](D:\Note in pdf\Mark down\Python Programming\index.png)


## Some useful Linux commands:
1. **`q`** :- To quit Linux , like ctrl+c.
2. **`pwd`** :- present working directory
3. **`ls`** :- lists all file in directory
4. **`cd`**:- change directory
5. **`touch file_name`** :- To create a file using Linux .
6.  - **`vim file_name`**:- open it in vim editor
    - press **i** to edit the contents.
    - hit : and then wq to quit the vim.
6. **Shit+insert** to past in gitbash
8. **ctrl + '+'** for zoom in and **ctrl + '-'**  vice versa


Some tips:
1. If you rename the file in the same directory. Git will consider it as it was deleted.

2. Never write in commit message "changed dir" or "modified file" commit means you have changed something.

3. Don't write date and time also...


# Errors

   #### <span style = "color:red"> Error :1 </span>

  when try to push file **Local repository** into **GitHub repository**

   ![](D:\Note in pdf\Mark down\Python Programming\error1.png)

solution :

We have to rebase the repository type following code in gitbash

````powershell
git pull --rebase origin main
git push origin main
````

FYI default branch name of **GitHub** is **main ** so if you use type **`git push origin master`** in **gitbash** than you are pushing master branch in **GitHub** repository ..

This error occurred because I renamed my main branch to master. But it will not create an extra branch.





created_by = **Mohammad Sharique**

