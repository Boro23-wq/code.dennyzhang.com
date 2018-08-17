#!/usr/bin/env bash
function my_test() {
    cd problems
    for f in $(ls -1t */README.org); do
        dirname=$(basename $(dirname $f))
            echo "Update blog $f"
sed -ie 's/Similar Problems:/#+BEGIN_HTML\'$'\nSimilar Problems:/g' $f
sed -ie 's/Similar Problems:/<a href="https:\/\/github.com\/dennyzhang\/code.dennyzhang.com"><img align="right" width="200" height="183" src="https:\/\/www.dennyzhang.com\/wp-content\/uploads\/denny\/watermark\/github.png" \/><\/a>\'$'\nSimilar Problems:/g' $f
sed -ie 's/Similar Problems:/#+END_HTML\'$'\nSimilar Problems:/g' $f
            rm -rf $dirname/README.orge
    done
}

function refresh_wordpress() {
    echo "Use emacs to update README.org"
    for d in "problems" "series" "review"; do
    # for d in "series" "review"; do
        cd "$d"
        for f in $(ls -1t */README.org); do
            echo "Update $f"
            dirname=$(basename $(dirname $f))
            cd $dirname
            /Applications/Emacs.app/Contents/MacOS/Emacs-x86_64-10_10 --batch -l ../../emacs-update.el
            cd ..
        done
        cd ..
    done
}

function refresh_link() {
    echo "refresh link"
    cd problems
    for f in $(ls -1t */README.org); do
        dirname=$(basename $(dirname $f))
        if ! grep "Blog link: https:\/\/code.dennyzhang.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update blog url for $f"
            sed -ie "s/Blog link: https:\/\/code.dennyzhang.com\/.*/Blog link: https:\/\/code.dennyzhang.com\/$dirname/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "tree\/master.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update GitHub url for $f"
            sed -ie "s/tree\/master\/.*/tree\/master\/$dirname][challenges-leetcode-interesting]]/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep -i lintcode.com $f 1>/dev/null 2>&1; then
            if ! grep "leetcode.com.*$dirname" $f 1>/dev/null 2>&1; then
                echo "Update Leetcode url for $f"            
                sed -ie "s/https:\/\/leetcode.com\/problems\/.*/https:\/\/leetcode.com\/problems\/$dirname\/description\/][leetcode.com]]/g" $f
                rm -rf $dirname/README.orge
            fi
        fi
    done
}

cd .

action=${1?}
case "$action" in 
    refresh_wordpress)
        refresh_wordpress
        ;;
    refresh_link)
        refresh_link
        ;;
    my_test)
        my_test
        ;;
        *) 
        echo "no matched action. Supported: refresh_link|my_test"
        ;;
esac
