# tree by Greg 
### <i> my take on the 'tree' command line tool for MacOS </i>



## Installation Guide 
1. Clone Repository 

```git clone https://github.com/Greg4268/tree.git```

2. Set alias in bashrc / zshrc 

```alias tree="python3 /path/to/script.py"```

3. (Optional) make alias including arguments 

```alias rtree="python3 /path/to/script.py --root"```

4. Reload terminal with new config 

5. run your script! 

## Command Line Arguments 
Exclude Dotfiles 
Description: When included, will exclude dotfiles from tree 
```bash
--exclude-dotfiles 
``` 
Max Depth 
Description: When added with integer following, will set a max depth of subtrees 
```bash
--max-depth {integer}
``` 
Root
Description: true = run tree from Users/{username}/ | false = run tree from current working directory 
```bash
--root 
``` 