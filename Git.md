# Git Fundamentals – Quick Reference Guide

This document covers the essential Git commands required for day-to-day development and collaboration using Git and GitHub.

---

## 1. Initial Setup (Run Once Per Machine)

### Install Git

**macOS**

```bash
brew install git
```

*or install Xcode Command Line Tools*

**Windows**
Install Git for Windows from the official site.

Verify installation:

```bash
git --version
```

---

## 2. Configure Git Identity

Set your global username and email (used in commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --global init.defaultBranch main
```

Check configuration:

```bash
git config --list
```

---

## 3. SSH Setup (Recommended for GitHub)

### Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter to accept default location.

### Copy Public Key

**macOS**

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

**Windows (Git Bash)**

```bash
clip < ~/.ssh/id_ed25519.pub
```

Add this key to:
GitHub → Settings → SSH and GPG Keys → New SSH Key

### Test SSH Connection

```bash
ssh -T git@github.com
```

---

## 4. Creating or Cloning a Repository

### Initialize a New Repository

```bash
git init
```

### Clone an Existing Repository

```bash
git clone git@github.com:username/repository.git
```

---

## 5. Basic Workflow Commands

### Check Current Status

```bash
git status
```

### Add Files to Staging Area

Add specific file:

```bash
git add file.txt
```

Add all changes:

```bash
git add .
```

### Commit Changes

```bash
git commit -m "Clear and meaningful message"
```

### View Commit History

```bash
git log
git log --oneline --graph --all
```

---

## 6. Working with Branches

### Create New Branch

```bash
git branch feature-name
```

Or create and switch:

```bash
git switch -c feature-name
```

### Switch Branch

```bash
git switch branch-name
```

### Merge Branch

```bash
git merge feature-name
```

### Delete Branch

```bash
git branch -d feature-name
```

---

## 7. Working with Remote Repositories

### Check Remote

```bash
git remote -v
```

### Add Remote (if not already set)

```bash
git remote add origin git@github.com:username/repository.git
```

### Push Changes

First push:

```bash
git push -u origin main
```

Subsequent pushes:

```bash
git push
```

### Pull Latest Changes

```bash
git pull origin main
```

---

## 8. Checking Differences

### View Unstaged Changes

```bash
git diff
```

### View Staged Changes

```bash
git diff --staged
```

---

## 9. Undoing Changes

### Unstage File

```bash
git restore --staged file.txt
```

### Discard Local Changes

```bash
git restore file.txt
```

### Reset Last Commit (Local Only)

```bash
git reset --hard HEAD~1
```

---

## 10. Good Practices

* Write clear commit messages.
* Commit small, logical changes.
* Use branches for new features.
* Pull before pushing.
* Never commit secrets or private keys.
* Avoid rewriting history on shared branches.

---

## Summary Workflow

1. `git pull`
2. Create branch
3. Make changes
4. `git add .`
5. `git commit -m "..."`
6. `git push`
7. Create Pull Request (on GitHub)

---

This guide covers the commands needed for foundational Git usage in individual and team environments.
