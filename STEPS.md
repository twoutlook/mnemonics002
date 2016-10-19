
# Create a new Github project
  including .gitignore with Java, so far
  LICENSE
  README.md

# Create a new C9 project
  clone Github project
  
# Edit .gitignore
  Follow DjangoGirls' guideline
  https://tutorial.djangogirls.org/en/deploy/
 
# Install python3.5 and python3.5-venv
    sudo apt-get install python3.5 python3.5-venv -y

# Create virtual environment
    python3.5 -m venv myvenv

# Activate virtual environment
    twoutlook:~/workspace (master) $ source myvenv/bin/activate
    (myvenv) twoutlook:~/workspace (master) $ 
    
# Upgrade pip
    pip freeze
    pip install --upgrade pip
    
# Install Django
    pip install django
    
 
# Create a new Django project    
   django-admin startproject mysite 
    
# Create a new project appplication app001
    cd mysite   
    python manage.py startapp app001
    
# Create a DB script
    python manage.py makemirgrations
    python manage.py migrate
    
# Sync DB
    source db.py
    
# Create a superuser
    source db.py
    
# Create script of run development server
    python manage.py runserver $IP:$PORT
    
# Visit mysite and admin    
    https://taichi-mnemonics-twoutlook.c9users.io/    
    https://taichi-mnemonics-twoutlook.c9users.io/admin  
    
    
# Run development server
    source db.py
    
# New terminal and activate virtual environment
    source myvenv/bin/activate

# Markdown
- [link to Mastering Markdown!](https://guides.github.com/features/mastering-markdown/)


# Git and Github
    git add.
    git status
    
    // When something is wrong, before commit, to reset
    git reset
    
    git commit -m"mysite with app001 in blank"
    
    git push -u origin master
    
# Git and Github - Tag
vogella http://www.vogella.com/tutorials/Git/article.html#tagging_createlightweight    
[link to Vogella's Git](http://www.vogella.com/tutorials/Git/article.html#tagging_createlightweight)

    git tag --help
    git tag -a v0.1 -m"blank mysite and app001 with superuser ubuntu"
    git show v0.1q
    
    git push origin v0.1

# check/add/delete local/remote tag
http://stackoverflow.com/questions/5480258/how-to-delete-a-remote-tag
    
    // check local tags
    git tag
    
    // check remote tags
    git ls-remote --tags origin
    
    
    // add a local tag
    git tag -a v0.1 -m"blank mysite and app001 with superuser ubuntu"
    
    // add a remote tag, by push
    git push origin v0.1 
    
    
    // delete a local tag
    git tag --delete v0.1

    // delte a remote tag, by push with --delete option
    git push --delete origin v0.1
    
    
    
    
    
    



    