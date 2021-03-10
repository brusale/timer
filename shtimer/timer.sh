echo "How long will this timer last?"
read time

#for ((i=time; i>0; i--)) 
#    do
#    sleep 1
#    done

python ../pytimer/timer.py --time $time
