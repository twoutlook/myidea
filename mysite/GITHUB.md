# Create a new project on Gibhub and choose SSH, not HTTPS

    (myvenv) twoutlook:~/workspace (master) $ pwd
    /home/ubuntu/workspace

    echo "# myidea" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:twoutlook/myidea.git
    git push -u origin master
    
# Make sure .gitignore is working well as expected
    (myvenv) twoutlook:~/workspace (master) $ git add .
    (myvenv) twoutlook:~/workspace (master) $ git status    
    
myvenv is the same level as mysite, but we don't put myvenv to Github    
__pacache__ is not necessary to transfer to other computers as well
    