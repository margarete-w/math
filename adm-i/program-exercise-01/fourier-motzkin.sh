#!/bin/bash#
if [ "$1" == "compute_x_or_y" ]; then
  #echo "Run compute_x_or_y"
  python3 compute_x_or_y.py $2
else
  echo ''
  echo '_        __        ______  _____          _______    _____    ____
  (__    __) \    ___)    /  \    |        |      /   |    / _  \
    |  |     |  (__     /    \   |  |\/|  |     /    |_  (_/ )  )
    |  |     |   __)   /  ()  \  |  |  |  |    (__    _)    /  /
    |  |     |  (___  |   __   | |  |  |  |      _|  |_    /  /__
 ___|  |____/       )_|  (__)  |_|  |__|  |_____(      )__(      )_'
 echo ""
 echo ""
 echo "~ˁ˚ᴥ˚ˀ~"
 echo "Hello Sven"
 echo "How are you?"
 echo ""
 echo "---------------------"
 echo ""

 if [ "$1" == "project" ]; then
   # echo "Run project"
   python3 project.py $2 $3 $4
 elif [ "$1" == "image" ]; then
   #echo "Run image"
   python3 image.py $2 $3 $4
 elif [ "$1" == "H_representation" ]; then
   #echo "Run H_representation"
   python3 H_representation.py $2 $3
 else
   echo 'Unknown parameter given. Try
   ./fourier-motzkin.sh project inputfile k outputfile
   ./fourier-motzkin.sh image polyhedron matrix outputfile
   ./fourier-motzkin.sh H_representation inputfile outputfile
   ./fourier-motzkin.sh compute_x_or_y inputfile'
   echo ""
   echo ""
 fi

 echo ""
 echo "https://www.instagram.com/official_team42/"
 echo ""
 echo ""

 echo "Wish you all the best"
 echo '     / \
    / _ \
   | / \ |
   ||   || _______
   ||   || |\     \
   ||   || ||\     \
   ||   || || \    |
   ||   || ||  \__/
   ||   || ||   ||
    \\_/ \_/ \_//
   /   _     _   \
  /               \
  |    O     O    |
  |   \  ___  /   |
 /     \ \_/ /     \
/  -----  |  -----  \
|     \__/|\__/     |
\       |_|_|       /
 \_____       _____/
       \     /
       |     |
'
fi
