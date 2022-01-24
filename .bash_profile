# added by Anaconda3 2019.10 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/Users/ericc/opt/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/Users/ericc/opt/anaconda3/etc/profile.d/conda.sh" ]; then
# . "/Users/ericc/opt/anaconda3/etc/profile.d/conda.sh"  # commented out by conda initialize
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/Users/ericc/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/ericc/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/ericc/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/ericc/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/ericc/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


##
# Your previous /Users/ericc/.bash_profile file was backed up as /Users/ericc/.bash_profile.macports-saved_2021-03-17_at_14:21:20
##

# MacPorts Installer addition on 2021-03-17_at_14:21:20: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.


# MacPorts Installer addition on 2021-03-17_at_14:21:20: adding an appropriate DISPLAY variable for use with MacPorts.
export DISPLAY=:0
# Finished adapting your DISPLAY environment variable for use with MacPorts.

export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
. "/Users/ericc/.new_local/env"


alias c="clear"
# git commit / update
alias gc="bash git_commit.sh"
alias n="nano"
alias py="/Users/ericc/anaconda3/bin/python"
alias π="source .bash_profile"
alias ∫="bash"
# make file
alias mkf="touch"
alias mkd="mkdir"