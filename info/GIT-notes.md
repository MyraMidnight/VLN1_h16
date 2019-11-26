# Using Git

**Git** is a version control tool, very handy when doing any writing or programming that allows you to keep track of all modifications.
Since you need to save all changes in order to view them when programming, git becomes an essential tool to create _check points_ 
that you can go back to whenever you might want to cancel your latest changes. 

You will need to open a new terminal to interact with `git` if the given terminal is already running something (such as a development server or sass compiler, things that keep running until told to stop).

> There is also the `Git Bash` that is a terminal specially designed for git (comes with the git install), lets you `left-click` in the working folder and choose to run Git Bash. 



## Version control 

### `git status`
> Will tell you the current status of your git

This command will show you a list of all modified files since last commit, 
as well as your working branch. `master` branch should be reserved for the latest stable version
while keeping all deviations and work on separate branches. They can be merged later on or scrapped.


 while all _modified_ (since last commit) and _untracked_ (when you make new files/folders) are listed in red
```
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   src/index.js

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   src/screens/Login.js
```
The two lists are very clearly separated, so the font color isn't required to see the difference.


## The 'Working Branch' is your zone
>The `master branch` is the default starting branch, and the center of the project. 

 **The master branch is the center of the project**, the latest stable version that all other branches should be using as a base.

That is why you should never work directly on the master, but create your own separate branches to test your changes until they can be `merged` to the master once more.

Each branch is a different version of the master where you can develop your changes without fear of breaking the master branch,
as well as causing minimal `merge conflicts`

* You cannot move between branches without doing a commit or canceling all your modifications, this protects you from accidentally loosing progress.
* You do not loose your committed progress when moving between branches, git will simply change all files to represent the selected branch. 


### Creating a **new branch** 

To create a new branch, you simply write the following command
```
git branch <new-branch-name>
```
You can also create a new branch and simultaneously move into it with the following command
```
git checkout -b <new-branch-name>
```


### Moving between branches

You use `git checkout` to move between existing local branches

```
git checkout <branch-name>
```
* These are _local_ branches which are not automatically connected to the _remote repository_ 
* To connect a branch to the _remote repository_ simply do a `git push` and you will be provided with instructions how to create the remote branch if it doesn't already exist.
* The name of the _remote branch_ does not need to be identical, but it does help to keep things consistant.

But be sure to **commit your work before moving between branches**


### Merging branches
> `git merge` combines your current branch with another local branch that you specify, for example `git merge master`. 

```
git merge <branch-name>
```
* This command is merging local branches and has no effect on the _remote repository_ until you push the changes.

**Guide for updating your branches**
1. **commit your changes** before moving onto the _master branch_
2. **pull** the latest master version 
3. move back into the branch you wanted to update
4. use `git merge master` to merge _working branch_ with _master branch_ 
5. **solve any merge conflicts** if any, 
6. **commit** and you're done (unless you wish to push the merge as well)
 
* Easy way to keep your branch updated is to move to the _master branch_, pull the latest version and then move back into the branch you were working on and `git merge master`
* If you wish to push your changes to the _master branch_, then first update your branch (explained previously) and then go onto the master



##  Commit your changes 
* I recommend that you **commit often**, whenever you are happy with your progress. 
* It saves your progress locally and will allow you to revert the code back to last commited version. 
* You can commit even without internet, these are local actions.

 You can use `git status` at any time to see a list of all modified files that haven't been committed yet.


### 1. `git add` to stage
* to protect your work, git will not allow you to move between branches unless you've committed all modifications with `git commit` or reset them with `git checkout -- .` 

```
git add <filename>
```
* git will only commit files that have been added to the _staging area_
*  `git add .` will add all modified files to the _staging area_
* Else you should tell it what file you wish to commit with `git add file-name`

### 2. `git commit`, create your checkpoint.

```
git commit -m "your message here"
```
* Once you have staged some (or all) files, then you can commit them to git as a backup that you can revert back to.
* You cannot commit without giving a short explanation of what you changed. **The message should be short and still able to tell others what was done.**
* If you forget to add the message then you can get semi-stuck in the terminal depending on your settings as it will still want you to add a message.



## Reverting to latest commit, cancel any modifications
> `git checkout` is very important when it comes to git versioning.

* `git checkout -- <filename>` resets the specified file to the last commited version, removing all modifications that haven't been committed without effecting other files.

**Create a new branch when working on the project**, 
while the `master` branch should be the latest stable version of the project (it is basically the root branch).

Use `git branch` to confirm your working branch ("_you are here_") indicated by a `*` infront of the branch name. 


## Remote Repository ( share your changes )
>The _remote repository_ is your online backup and shared codebase when working with others. 
You mainly communicate with it through `git pull` and `git push`.

* To prevent endless merge conflicts, it is best to be working on separate branch, and then make merge-requests when your work is stable enough to add to the `master`
* It is a good habit to at least do a `git push` at the end of the day, it secures your progress and allows your team to see what you've been working on.
* It is important to keep an eye on the `remote master branch` and pull those changes to your working branch when needed so you don't fall too far behind


### `git push` 
> This will push all your commits onto a **remote branch/repository** (think of it as a online backup).
>
> It is fine if you only `push` all your commits at the end of the day at least (or whenever you stop working for the day)

### `git pull`
> This will pull the latest changes from the _remote branch_ onto your computer.  
>
> You should `pull` before you `push`. 

## Solving conflicts
There will be conflicts when your working branch does not match the _remote branch_ . 

1. `pull` the remote version
2. open the conflicting files
3. the conflicting code (your changes vs. the current remote version)
4. solve the conflicts by combining the code and cleaning it up and save the files.
5. **commit the changes**
6. now you can try to `push`again 


### Updating your branch 
I recommend that you update your working branch regularily so that you don't fall too far behind the `master branch`.
* `git pull origin master` lets you pull the latest master branch directly onto your working branch from the remote repository.
* if you are having problems with conflicts, you can cancel everything with `git checkout -- .`, it will revert the branch to yur latest commited version
