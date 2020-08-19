# mv *.md markdownfiles/
# mv *.html htmlfiles/
# https://stackoverflow.com/questions/16864259/how-to-run-bash-script-after-git-push/16866281

# if test __pycache__/; then
# 	echo "File Exists"
# else
# 	echo "False"
# fi

# if test -f *.md; then
# 	echo "Organizing Markdown Files"
# 	mv *.md markdownfiles/
# else
# 	echo "No Markdown Files"
# fi


# if test -f *.html; then
# 	echo "Organizing HTML Files"
# 	mv *.html htmlfiles/
# else
# 	echo "No HTML Files"
# fi

python move.py
git add .
# Remove __pycache__ folder


# Git Hook Code
# Create file 'pre-commit' in directory .git/hooks

# #!/bin/sh
# bash format.sh