# Git Tutorial
How to import a new project into Git, make changes to it, and share changes with other developers

## Introduce yourself to Git
```
$ git config --global user.name "Your Name Comes Here"
$ git config --global user.email you@yourdomain.example.com
```
## Importing a new project
Initialized the working directory.
```
$ git init
```
Take a snapshot of the contents of all files under the current directory. This snapshot is stored in a temporary staging area which Git calls the "index".
```
$ git add .
```
Permanently store the contents of the index in the repository
```
$ git commit
```
## Making changes
Add updated contents to the index.
``` 
$ git add file1 file2 file3
```
A brief summary of what is about to be committed.
```
$ git status
```
Commit your changes.
```
$ git commit
```
## Viewing project history
View the history of your changes
```
$ git log
```

## References
1.  https://git-scm.com/docs/gittutorial
2. 