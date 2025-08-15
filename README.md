📝 Git Tips I Learned During This Project
1. Removing files from a newly initialized repo after committing

If you just initialized the repo and accidentally committed files you didn’t want, you can run:

git rm --cached -r .


Note: git reset --soft HEAD~1 won’t work here because you’re already at the first commit (HEAD) and there’s no previous commit to reset to.

2. Unstaging files before committing

If you have staged files but haven’t committed yet:

Unstage a specific file:

git restore --staged 'filename'


Unstage all files:

git restore --staged .
