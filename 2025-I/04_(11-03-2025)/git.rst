Git Cheat Sheet
===============

This cheat sheet provides a quick reference to basic Git commands and concepts.

Setup
-----

- **Configure user information**:
  ::

    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

- **Check configuration**:
  ::

    git config --list

Creating Repositories
---------------------

- **Initialize a new repository**:
  ::

    git init

- **Clone an existing repository**:
  ::

    git clone <repository_url>

Basic Workflow
--------------

- **Check the status of the repository**:
  ::

    git status

- **Stage changes**:
  ::

    git add <file>          # Stage a specific file
    git add .              # Stage all changes

- **Commit changes**:
  ::

    git commit -m "Commit message"

- **View commit history**:
  ::

    git log

Branching and Merging
---------------------

- **Create a new branch**:
  ::

    git branch <branch_name>

- **Switch to a branch**:
  ::

    git checkout <branch_name>

- **Create and switch to a new branch**:
  ::

    git checkout -b <branch_name>

- **Merge a branch into the current branch**:
  ::

    git merge <branch_name>

- **Delete a branch**:
  ::

    git branch -d <branch_name>

Remote Repositories
-------------------

- **Add a remote repository**:
  ::

    git remote add <name> <repository_url>

- **View remote repositories**:
  ::

    git remote -v

- **Fetch changes from a remote repository**:
  ::

    git fetch <remote_name>

- **Pull changes from a remote repository**:
  ::

    git pull <remote_name> <branch_name>

- **Push changes to a remote repository**:
  ::

    git push <remote_name> <branch_name>

Undoing Changes
---------------

- **Unstage a file**:
  ::

    git reset <file>

- **Revert changes in a file**:
  ::

    git checkout -- <file>

- **Amend the last commit**:
  ::

    git commit --amend

- **Revert a commit**:
  ::

    git revert <commit_hash>

Stashing
--------

- **Stash changes**:
  ::

    git stash

- **Apply stashed changes**:
  ::

    git stash apply

- **List stashes**:
  ::

    git stash list

- **Clear stashes**:
  ::

    git stash clear

Tagging
-------

- **Create a tag**:
  ::

    git tag <tag_name>

- **Push tags to remote**:
  ::

    git push --tags

- **List tags**:
  ::

    git tag

Advanced
--------

- **Rebase a branch**:
  ::

    git rebase <branch_name>

- **Interactive rebase**:
  ::

    git rebase -i <commit_hash>

- **View differences**:
  ::

    git diff                  # Unstaged changes
    git diff --cached         # Staged changes

- **View remote branches**:
  ::

    git branch -r

- **Delete a remote branch**:
  ::

    git push <remote_name> --delete <branch_name>

Glossary
--------

- **Repository**: A directory where Git tracks changes.
- **Commit**: A snapshot of changes in the repository.
- **Branch**: A parallel version of the repository.
- **Merge**: Combining changes from different branches.
- **Remote**: A shared repository on a server or another location.

