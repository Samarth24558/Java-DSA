read -p "Enter the limit: " limit
sum=0

while [ $limit -ne 0 ];
do
	sum=$((sum+limit))
	limit=$((limit-1))
done
echo "Sum is:$sum"
