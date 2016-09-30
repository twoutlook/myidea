# Create a new project on Gibhub and choose SSH, not HTTPS

    (myvenv) twoutlook:~/workspace (master) $ pwd
    /home/ubuntu/workspace

    echo "# myidea" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:twoutlook/myidea.git
    git push -u origin master