#!/bin/bash
FILE='map.json'
ID=1
OBJECT='NULL'


while getopts "hi:f:o:" opt; do
  case $opt in
     i)
      ID=$OPTARG
      ;;
     f)
      FILE=$OPTARG
      ;;
     o)
      IFS=','
      OBJECT=($OPTARG)
      ;;
     h)
      python main.py -h	     
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
  
done
#shift $((OPTIND - 1))


#echo $OBJECT
#echo "Number of arguments: ${#OBJECT[@]}"
#echo -n "Arguments are:"
#for i in "${OBJECT[@]}"; do
#  echo -n " ${i},"
#  OUT=${OUT:+$OUT}"'$i' "
#done

#echo $OUT
#printf "\b \n"

python main.py -f $FILE -i $ID -o "${OBJECT[@]}"
