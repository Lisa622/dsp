# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pwd: print working directory  
    cd: change directory  
    CRTL + c:  abort  
    find . -name:  find file  
    man: information on commands  
    exit  
    touch: creates a file  
    nkdir: makes a directory  
    mv:  renames a file  
    cp: copy file  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  lists contents of current directory
`ls -a`  includes all hidden files
`ls -l`  use long list format
`ls -lh`  displays file size
`ls -lah`  the above three commands combined
`ls -t`  sorts by last edited
`ls -Glp`  

> > `ls`  lists contents of current directory  
`ls -a`  includes all hidden files  
`ls -l`  use long list format  
`ls -lh`  displays file size  
`ls -lah`  the above three commands combined  
`ls -t`  sorts by last edited  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -c` displays files by timestamp  
    `ls -R` displays subdirectories  
    `ls -x` displays files as rows  
    `ls -d` displays only directories  
    `ls -u` displays files by access time   
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Divides lists of arguments into sublists of acceptable length.  
find . -name "*abcd*" | xargs
 

