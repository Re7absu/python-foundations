# Git Notes

## Basic Git Commands

### Check repository status
git status

### Create a feature branch
git checkout -b feature/branch-name

### Switch branches
git checkout main

### Pull changes from GitHub
git pull origin main

### Add changes
git add <file>

### Create a commit
git commit -m "Commit message"

### Push a branch to GitHub
git push -u origin feature/branch-name

## Git Recovery Commands

### Temporarily save changes
git stash

### Restore stashed changes
git stash pop

### Undo the latest commit while keeping changes staged
git reset --soft HEAD~1

### Create a new commit that reverses a previous commit
git revert HEAD

### Fix the latest commit message
git commit --amend -m "New commit message"

## GitHub Pull Request Workflow

1. Create a feature branch.
2. Make the required changes.
3. Stage the changes.
4. Create a commit.
5. Push the feature branch to GitHub.
6. Open a Pull Request.
7. Review the changes.
8. Merge the Pull Request into main.
9. Switch back to main.
10. Pull the latest changes from GitHub.